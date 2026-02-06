from sqlalchemy.orm import Session
from ..models import AlertRule, AlertEvent, KPIValue, KPIDefinition

class AlertEngine:
    @staticmethod
    def evaluate_rules(db: Session):
        active_rules = db.query(AlertRule).filter(AlertRule.is_active == True).all()
        
        for rule in active_rules:
            # Get latest KPI value
            kpi_def = db.query(KPIDefinition).filter(KPIDefinition.key == rule.kpi_key).first()
            if not kpi_def:
                continue
                
            latest_value = db.query(KPIValue).filter(KPIValue.kpi_id == kpi_def.id).order_by(KPIValue.timestamp.desc()).first()
            if not latest_value:
                continue
            
            triggered = False
            if rule.operator == ">" and latest_value.value > rule.threshold:
                triggered = True
            elif rule.operator == "<" and latest_value.value < rule.threshold:
                triggered = True
            elif rule.operator == "==" and latest_value.value == rule.threshold:
                triggered = True
                
            if triggered:
                # Create alert event
                alert = AlertEvent(
                    rule_id=rule.id,
                    value_at_trigger=latest_value.value,
                    message=f"Alert '{rule.name}' triggered: {rule.kpi_key} is {latest_value.value} (threshold {rule.operator} {rule.threshold})"
                )
                db.add(alert)
        
        db.commit()
