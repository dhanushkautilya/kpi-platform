from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from .routers import integrations, ingestion, kpis, alerts
from .db import SessionLocal
from .seed import seed_data

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Seed data on startup
    db = SessionLocal()
    try:
        seed_data(db)
    finally:
        db.close()
    yield

app = FastAPI(title="KPI Intelligence Platform API", lifespan=lifespan)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(integrations.router)
app.include_router(ingestion.router)
app.include_router(kpis.router)
app.include_router(alerts.router)

@app.get("/")
async def root():
    return {"message": "KPI Intelligence Platform API is running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
