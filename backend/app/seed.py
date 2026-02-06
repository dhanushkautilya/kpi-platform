from sqlalchemy.orm import Session
from .models import KPIDefinition, AlertRule

def seed_data(db: Session):
    # KPI Definitions
    kpis = [
        KPIDefinition(
            key="daily_revenue",
            name="Daily Revenue",
            description="Total revenue from Stripe payments",
            formula_type="sql_sum",
            frequency="daily"
        ),
        KPIDefinition(
            key="daily_sessions",
            name="Daily Sessions",
            description="Total sessions from GA4",
            formula_type="sql_count",
            frequency="daily"
        )
    ]
    
    for k in kpis:
        exists = db.query(KPIDefinition).filter(KPIDefinition.key == k.key).first()
        if not exists:
            db.add(k)
            
    # Alert Rules
    rules = [
        AlertRule(
            name="Low Growth Alert",
            kpi_key="daily_sessions",
            threshold=10.0,
            operator="<"
        )
    ]
    
    for r in rules:
        exists = db.query(AlertRule).filter(AlertRule.name == r.name).first()
        if not exists:
            db.add(r)
            
    db.commit()
