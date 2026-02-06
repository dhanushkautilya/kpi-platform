from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, ForeignKey, Boolean
from sqlalchemy.sql import func
from .db import Base

class Integration(Base):
    __tablename__ = "integrations"
    
    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String, index=True) # stripe, ga4, hubspot
    name = Column(String)
    credentials = Column(JSON) # Mock tokens/keys
    is_active = Column(Boolean, default=True)
    last_sync = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class RawEvent(Base):
    __tablename__ = "raw_events"
    
    id = Column(Integer, primary_key=True, index=True)
    provider = Column(String, index=True)
    payload = Column(JSON)
    received_at = Column(DateTime(timezone=True), server_default=func.now())

class Event(Base):
    __tablename__ = "events"
    
    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True) # payment_succeeded, session, deal_won
    timestamp = Column(DateTime(timezone=True), index=True)
    amount = Column(Float, nullable=True)
    currency = Column(String, nullable=True)
    user_id = Column(String, nullable=True)
    source = Column(String, index=True) # stripe, ga4, hubspot
    attributes = Column(JSON) # flexible extra data
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class KPIDefinition(Base):
    __tablename__ = "kpi_definitions"
    
    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True) # daily_revenue, mrr, cac
    name = Column(String)
    description = Column(String)
    formula_type = Column(String) # sql_sum, python_rule
    query_template = Column(String, nullable=True)
    frequency = Column(String) # daily, monthly

class KPIValue(Base):
    __tablename__ = "kpi_values"
    
    id = Column(Integer, primary_key=True, index=True)
    kpi_id = Column(Integer, ForeignKey("kpi_definitions.id"))
    timestamp = Column(DateTime(timezone=True), index=True)
    value = Column(Float)
    dimensions = Column(JSON, nullable=True) # e.g. {"region": "US"}

class AlertRule(Base):
    __tablename__ = "alert_rules"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    kpi_key = Column(String)
    threshold = Column(Float)
    operator = Column(String) # >, <, ==
    is_active = Column(Boolean, default=True)

class AlertEvent(Base):
    __tablename__ = "alert_events"
    
    id = Column(Integer, primary_key=True, index=True)
    rule_id = Column(Integer, ForeignKey("alert_rules.id"))
    triggered_at = Column(DateTime(timezone=True), server_default=func.now())
    value_at_trigger = Column(Float)
    message = Column(String)
