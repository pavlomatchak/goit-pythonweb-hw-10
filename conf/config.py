from pydantic import ConfigDict, EmailStr
from pydantic_settings import BaseSettings

class Config:
  DB_URL = "postgresql+asyncpg://postgres:567234@localhost:5432/contacts_app"
  JWT_SECRET = "your_secret_key" # навчальний ключ
  JWT_ALGORITHM = "HS256"
  JWT_EXPIRATION_SECONDS = 3600

config = Config

class Settings(BaseSettings):
  DB_URL: str
  JWT_SECRET: str
  JWT_ALGORITHM: str = "HS256"
  JWT_EXPIRATION_SECONDS: int = 3600

  MAIL_USERNAME: EmailStr = "example@meta.ua"
  MAIL_PASSWORD: str = "secretPassword"
  MAIL_FROM: EmailStr = "example@meta.ua"
  MAIL_PORT: int = 465
  MAIL_SERVER: str = "smtp.meta.ua"
  MAIL_FROM_NAME: str = "Rest API Service"
  MAIL_STARTTLS: bool = False
  MAIL_SSL_TLS: bool = True
  USE_CREDENTIALS: bool = True
  VALIDATE_CERTS: bool = True

  model_config = ConfigDict(
    extra="ignore", env_file=".env", env_file_encoding="utf-8", case_sensitive=True
  )

settings = Settings()