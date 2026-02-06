from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..db import get_db
from ..models import AlertRule, AlertEvent
from ..services.alert_engine import AlertEngine

router = APIRouter(prefix="/alerts", tags=["alerts"])

@router.get("/rules")
def list_rules(db: Session = Depends(get_db)):
    return db.query(AlertRule).all()

@router.get("/events")
def list_alert_events(db: Session = Depends(get_db)):
    return db.query(AlertEvent).all()

@router.post("/evaluate")
def evaluate_alerts(db: Session = Depends(get_db)):
    AlertEngine.evaluate_rules(db)
    return {"message": "Alert rules evaluated"}
