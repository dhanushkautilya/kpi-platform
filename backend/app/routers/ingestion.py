from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Integration as IntegrationModel, RawEvent, Event
from ..services.connectors.stripe import StripeConnector
from ..services.connectors.ga4 import GA4Connector
from ..services.connectors.hubspot import HubSpotConnector
from ..services.normalize import NormalizationService
from ..settings import settings

router = APIRouter(prefix="/ingest", tags=["ingestion"])

async def perform_sync(provider: str, db: Session):
    # Determine connector
    connector = None
    if provider == "stripe":
        connector = StripeConnector(settings.STRIPE_API_KEY)
    elif provider == "ga4":
        connector = GA4Connector(settings.GA4_PROPERTY_ID)
    elif provider == "hubspot":
        connector = HubSpotConnector(settings.HUBSPOT_ACCESS_TOKEN)
    
    if not connector:
        return

    # Fetch events
    raw_payloads = await connector.fetch_events()
    
    # Store raw and normalized
    for payload in raw_payloads:
        # Store raw
        db_raw = RawEvent(provider=provider, payload=payload)
        db.add(db_raw)
        
        # Normalize
        normalized = NormalizationService.normalize(provider, payload)
        if normalized:
            db.add(normalized)
    
    db.commit()

@router.post("/pull/{provider}")
async def trigger_pull(provider: str, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    background_tasks.add_task(perform_sync, provider, db)
    return {"message": f"Sync started for {provider}"}

@router.get("/events")
def list_events(source: str = None, db: Session = Depends(get_db)):
    query = db.query(Event)
    if source:
        query = query.filter(Event.source == source)
    return query.all()
