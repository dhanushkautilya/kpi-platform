import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class GA4Connector:
    def __init__(self, property_id: str):
        self.property_id = property_id

    async def fetch_events(self, days: int = 7) -> List[Dict[str, Any]]:
        """Mock fetching GA4 events."""
        events = []
        for i in range(days * 10): # Mock 10 sessions per day
            timestamp = datetime.now() - timedelta(days=random.randint(0, days), hours=random.randint(0, 23))
            
            payload = {
                "event_name": "session_start",
                "timestamp_micros": int(timestamp.timestamp() * 1000000),
                "user_id": f"user_{random.getrandbits(32)}",
                "params": {
                    "page_location": random.choice(["/home", "/pricing", "/docs", "/blog"]),
                    "source": random.choice(["google", "direct", "twitter", "linkedin"]),
                    "medium": "organic"
                }
            }
            events.append(payload)
        return events
