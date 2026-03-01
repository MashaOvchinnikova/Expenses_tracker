from app.core.database import async_session_maker


def get_db():
    """
    Dependency для FastAPI.
    Создает новую сессию БД для каждого запроса и закрывает её после завершения.
    """
    db = async_session_maker()
    try:
        yield db
    finally:
        db.close()