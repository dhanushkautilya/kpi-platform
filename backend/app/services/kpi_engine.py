from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from ..models import Event, KPIValue, KPIDefinition

class KPIEngine:
    @staticmethod
    def compute_daily_revenue(db: Session, date: datetime):
        """Sum of all stripe payment_succeeded amount for a specific day."""
        start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timedelta(days=1)
        
        result = db.query(func.sum(Event.amount)).filter(
            Event.source == "stripe",
            Event.event_type == "payment_succeeded",
            Event.timestamp >= start_of_day,
            Event.timestamp < end_of_day
        ).scalar()
        
        return result or 0.0

    @staticmethod
    def compute_sessions(db: Session, date: datetime):
        """Count of sessions from GA4."""
        start_of_day = date.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_day = start_of_day + timedelta(days=1)
        
        result = db.query(func.count(Event.id)).filter(
            Event.source == "ga4",
            Event.event_type == "session_start",
            Event.timestamp >= start_of_day,
            Event.timestamp < end_of_day
        ).scalar()
        
        return float(result or 0)

    @classmethod
    def run_all_kpis(cls, db: Session, date: datetime = None):
        if date is None:
            date = datetime.now()
        
        # 1. Daily Revenue
        rev = cls.compute_daily_revenue(db, date)
        kpi_def = db.query(KPIDefinition).filter(KPIDefinition.key == "daily_revenue").first()
        if kpi_def:
            val = KPIValue(kpi_id=kpi_def.id, timestamp=date, value=rev)
            db.add(val)
        
        # 2. Daily Sessions
        sessions = cls.compute_sessions(db, date)
        kpi_def = db.query(KPIDefinition).filter(KPIDefinition.key == "daily_sessions").first()
        if kpi_def:
            val = KPIValue(kpi_id=kpi_def.id, timestamp=date, value=sessions)
            db.add(val)
        
        db.commit()
