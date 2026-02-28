from typing import Optional, Any

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
       Настройки приложения.

       Все значения автоматически загружаются из .env файла
       или из переменных окружения системы.
    """
    # Telegram
    BOT_TOKEN: str

    # Database - либо готовая строка, либо компоненты
    DATABASE_URL: Optional[str] = None
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str = "expense_tracker"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    # App
    DEBUG: bool = False
    SECRET_KEY: str = "default-secret-key"
    API_V1_PREFIX: str = "/api/v1"

    # Асинхронный URL (опционально)
    DATABASE_URL_ASYNC: Optional[str] = None

    model_config = SettingsConfigDict(
        env_file=".env",  # загружаем из .env
        env_file_encoding="utf-8",
        case_sensitive=False,  # имена переменных не чувствительны к регистру
        extra="ignore"  # игнорировать лишние переменные
    )

    def __init__(self, **values: Any):
        super().__init__(**values)
        # Если DATABASE_URL не указан, собираем из компонентов
        if not self.DATABASE_URL:
            self.DATABASE_URL = (
                f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
                f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
            )

        # Создаем асинхронный URL для будущих задач
        if not self.DATABASE_URL_ASYNC:
            self.DATABASE_URL_ASYNC = self.DATABASE_URL.replace(
                'postgresql://',
                'postgresql+asyncpg://'
            )

def get_settings() -> BaseSettings:
    """Возвращает объект настроек"""
    return Settings()

# Глобальный объект настроек
settings = get_settings()

# Для отладки
if settings.DEBUG:
    print("Настройки загружены:")
    print(f"BOT_TOKEN: {'*' * 10}{settings.BOT_TOKEN[-5:] if settings.BOT_TOKEN else 'не указан'}")
    print(f"DATABASE_URL: {settings.DATABASE_URL}")
    print(f"POSTGRES_USER: {settings.POSTGRES_USER}")
    print(f"POSTGRES_DB: {settings.POSTGRES_DB}")
    print(f"DEBUG: {settings.DEBUG}")