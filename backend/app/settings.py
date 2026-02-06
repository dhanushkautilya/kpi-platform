from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Database Configuration
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "postgres"
    DB_NAME: str = "kpi_db"
    DB_HOST: str = "db"
    DB_PORT: str = "5432"
    DATABASE_URL: str = "sqlite:///./kpi.db" # Using SQLite for local dev
    
    SECRET_KEY: str = "yoursecretkeyhere"
    
    STRIPE_API_KEY: str = "sk_test_mock"
    GA4_PROPERTY_ID: str = "mock_property_id"
    HUBSPOT_ACCESS_TOKEN: str = "pat-na1-mock"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
