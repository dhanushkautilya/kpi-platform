from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..db import get_db
from ..models import Integration as IntegrationModel
from ..schemas import Integration, IntegrationCreate

router = APIRouter(prefix="/integrations", tags=["integrations"])

@router.get("/", response_model=List[Integration])
def list_integrations(db: Session = Depends(get_db)):
    return db.query(IntegrationModel).all()

@router.post("/", response_model=Integration)
def create_integration(integration: IntegrationCreate, db: Session = Depends(get_db)):
    db_item = IntegrationModel(**integration.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.post("/{integration_id}/test")
def test_integration(integration_id: int, db: Session = Depends(get_db)):
    integration = db.query(IntegrationModel).filter(IntegrationModel.id == integration_id).first()
    if not integration:
        raise HTTPException(status_code=404, detail="Integration not found")
    # Mock testing logic
    return {"status": "success", "message": f"Connection to {integration.provider} verified"}
