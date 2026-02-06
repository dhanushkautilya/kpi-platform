from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from typing import List
from ..db import get_db
from ..models import KPIValue, KPIDefinition
from ..services.kpi_engine import KPIEngine

router = APIRouter(prefix="/kpis", tags=["kpis"])

@router.get("/definitions")
def list_kpis(db: Session = Depends(get_db)):
    return db.query(KPIDefinition).all()

@router.post("/compute")
def compute_kpis(db: Session = Depends(get_db)):
    # Run for last 7 days for demo
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        KPIEngine.run_all_kpis(db, date)
    return {"message": "KPIs computed for last 7 days"}

@router.get("/{kpi_key}/timeseries")
def get_timeseries(kpi_key: str, db: Session = Depends(get_db)):
    kpi_def = db.query(KPIDefinition).filter(KPIDefinition.key == kpi_key).first()
    if not kpi_def:
        return []
    
    values = db.query(KPIValue).filter(KPIValue.kpi_id == kpi_def.id).order_by(KPIValue.timestamp).all()
    return [{"timestamp": v.timestamp, "value": v.value} for v in values]
