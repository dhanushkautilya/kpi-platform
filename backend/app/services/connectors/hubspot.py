import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

class HubSpotConnector:
    def __init__(self, access_token: str):
        self.access_token = access_token

    async def fetch_events(self, days: int = 7) -> List[Dict[str, Any]]:
        """Mock fetching HubSpot deals."""
        events = []
        for i in range(days): # Mock 1 deal per day
            timestamp = datetime.now() - timedelta(days=random.randint(0, days), hours=random.randint(0, 23))
            
            payload = {
                "id": f"deal_{random.getrandbits(32)}",
                "properties": {
                    "dealname": f"Deal {random.randint(1, 1000)}",
                    "amount": random.randint(5000, 50000),
                    "dealstage": random.choice(["closedwon", "closedlost", "appointmentscheduled"]),
                    "closedate": timestamp.isoformat()
                }
            }
            events.append(payload)
        return events
