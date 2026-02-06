from datetime import datetime
from typing import Dict, Any, Optional
from ..models import Event

class NormalizationService:
    @staticmethod
    def normalize_stripe(payload: Dict[str, Any]) -> Event:
        """Map Stripe event to canonical Event model."""
        data_obj = payload.get("data", {}).get("object", {})
        return Event(
            event_type=payload.get("type"),
            timestamp=datetime.fromtimestamp(payload.get("created")),
            amount=data_obj.get("amount", 0) / 100.0, # Stripe uses cents
            currency=data_obj.get("currency"),
            user_id=data_obj.get("customer"),
            source="stripe",
            attributes=payload
        )

    @staticmethod
    def normalize_ga4(payload: Dict[str, Any]) -> Event:
        """Map GA4 event to canonical Event model."""
        return Event(
            event_type=payload.get("event_name"),
            timestamp=datetime.fromtimestamp(payload.get("timestamp_micros") / 1000000.0),
            amount=None,
            currency=None,
            user_id=payload.get("user_id"),
            source="ga4",
            attributes=payload.get("params", {})
        )

    @staticmethod
    def normalize_hubspot(payload: Dict[str, Any]) -> Event:
        """Map HubSpot deal to canonical Event model."""
        props = payload.get("properties", {})
        return Event(
            event_type=f"deal_{props.get('dealstage')}",
            timestamp=datetime.fromisoformat(props.get("closedate").replace("Z", "+00:00")),
            amount=float(props.get("amount", 0)),
            currency="usd",
            user_id=None, # HubSpot deals might not have a simple user_id
            source="hubspot",
            attributes=props
        )

    @classmethod
    def normalize(cls, provider: str, payload: Dict[str, Any]) -> Optional[Event]:
        if provider == "stripe":
            return cls.normalize_stripe(payload)
        elif provider == "ga4":
            return cls.normalize_ga4(payload)
        elif provider == "hubspot":
            return cls.normalize_hubspot(payload)
        return None
