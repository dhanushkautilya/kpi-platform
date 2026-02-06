# GrownIntelligence: KPI Intelligence Platform

GrownIntelligence is a comprehensive KPI platform designed to help businesses aggregate, normalize, and visualize data from multiple third-party services like Stripe, Google Analytics 4, and HubSpot.

## 📊 KPI Overview

The platform provides a unified view of your business's critical metrics by:
- **Aggregating Data**: Seamlessly connecting to Stripe, GA4, and HubSpot.
- **Normalizing Events**: Converting disparate data types (payments, sessions, deals) into a standardized format.
- **Calculating Metrics**: Automated logic for tracking Daily Revenue, Active Sessions, and more.
- **Alerting**: Real-time notifications when KPIs breach user-defined thresholds.

## 🎯 Use Cases

- **Revenue Monitoring**: Track MRR, daily revenue, and payment success rates across providers.
- **Marketing Analysis**: Correlation between website traffic (GA4) and sales conversion (HubSpot/Stripe).
- **Proactive Management**: Set alerts for significant traffic spikes or revenue drops to take immediate action.
- **Historical Trends**: Analyze long-term business growth with structured KPI storage.

## 🛠 Tech Stack

- **Backend**: FastAPI, SQLAlchemy, PostgreSQL, Alembic.
- **Frontend**: React (v19), Vite, Tailwind CSS, Recharts.
- **Infrastructure**: Docker, Docker Compose.

## 🚀 Local Setup

### Prerequisites
- Docker & Docker Compose
- Node.js (v18+) & npm (for frontend local development)
- Python 3.10+ (optional for local backend development)

### Step 1: Clone and Configure
```bash
git clone <repository-url>
cd kpi-platform
cp .env.example .env
```
*Edit `.env` to include your actual API keys or keep the mock keys for testing.*

### Step 2: Start the Backend (Docker)
The easiest way to run the database and backend is via Docker:
```bash
docker-compose up --build
```
The API will be available at `http://localhost:8000`. You can view the swagger docs at `http://localhost:8000/docs`.

### Step 3: Start the Frontend
In a new terminal window:
```bash
cd frontend
npm install
npm run dev
```
The dashboard will be available at `http://localhost:5173`.

### Step 4: Seed Data (Optional)
The backend automatically seeds mock data on startup, but you can manually trigger a data pull via the API or UI.

---

## 🏗 Project Structure

- `/backend`: FastAPI application containing the API routes, KPI engine, and database models.
- `/frontend`: Vite-powered React application with the dashboard and integration forms.
- `/docker-compose.yml`: Orchestrates the PostgreSQL database and backend service.
