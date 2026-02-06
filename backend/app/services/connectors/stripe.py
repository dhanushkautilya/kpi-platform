import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class StripeConnector:
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def fetch_events(self, days: int = 7) -> List[Dict[str, Any]]:
        """Mock fetching Stripe events."""
        events = []
        for i in range(days * 2): # Mock 2 events per day
            timestamp = datetime.now() - timedelta(days=random.randint(0, days), hours=random.randint(0, 23))
            event_type = random.choice(["payment_succeeded", "charge.refunded", "customer.subscription.created"])
            
            payload = {
                "id": f"evt_{random.getrandbits(64)}",
                "type": event_type,
                "created": int(timestamp.timestamp()),
                "data": {
                    "object": {
                        "amount": random.randint(1000, 10000) if event_type != "charge.refunded" else random.randint(500, 2000),
                        "currency": "usd",
                        "customer": f"cus_{random.getrandbits(32)}",
                    }
                }
            }
            events.append(payload)
        return events
