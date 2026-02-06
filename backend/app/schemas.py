from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any, List

# Integration Schemas
class IntegrationBase(BaseModel):
    provider: str
    name: str
    credentials: Dict[str, Any]
    is_active: bool = True

class IntegrationCreate(IntegrationBase):
    pass

class Integration(IntegrationBase):
    id: int
    last_sync: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True

# Event Schemas
class EventBase(BaseModel):
    event_type: str
    timestamp: datetime
    amount: Optional[float] = None
    currency: Optional[str] = None
    user_id: Optional[str] = None
    source: str
    attributes: Dict[str, Any] = {}

class Event(EventBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# KPI Schemas
class KPIDefinitionBase(BaseModel):
    key: str
    name: str
    description: Optional[str] = None
    formula_type: str
    query_template: Optional[str] = None
    frequency: str

class KPIDefinition(KPIDefinitionBase):
    id: int

    class Config:
        from_attributes = True

class KPIValue(BaseModel):
    kpi_id: int
    timestamp: datetime
    value: float
    dimensions: Optional[Dict[str, Any]] = None

    class Config:
        from_attributes = True

# Alert Schemas
class AlertRuleBase(BaseModel):
    name: str
    kpi_key: str
    threshold: float
    operator: str
    is_active: bool = True

class AlertRule(AlertRuleBase):
    id: int

    class Config:
        from_attributes = True

class AlertEvent(BaseModel):
    id: int
    rule_id: int
    triggered_at: datetime
    value_at_trigger: float
    message: str

    class Config:
        from_attributes = True
