# Собираем всё важное из core в одном месте
from app.core.config import settings
from app.core.database import SessionLocal, engine, Base
from app.core.dependencies import get_db

# Теперь можно писать: from app.core import settings, SessionLocal