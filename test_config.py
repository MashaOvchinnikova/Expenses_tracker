"""
Тестируем загрузку конфигурации с твоим .env файлом.
Запусти: python test_config.py
"""

import sys
from pathlib import Path

# Добавляем путь к проекту
sys.path.append(str(Path(__file__).parent))

try:
    from app.core.config import settings

    print("=" * 60)
    print("ТЕСТ КОНФИГУРАЦИИ")
    print("=" * 60)

    # Основные настройки
    print(f"\nЗагруженные настройки:")
    print(f"DEBUG: {settings.DEBUG}")
    print(f"BOT_TOKEN: {'указан' if settings.BOT_TOKEN else 'НЕ УКАЗАН!'}")
    if settings.BOT_TOKEN:
        print(f"(первые 5 символов: {settings.BOT_TOKEN[:5]}...)")

    # Информация о БД
    print(f"\nБаза данных:")
    print(f"DATABASE_URL: {settings.DATABASE_URL}")
    print(f"POSTGRES_USER: {settings.POSTGRES_USER}")
    print(f"POSTGRES_DB: {settings.POSTGRES_DB}")
    print(f"POSTGRES_HOST: {settings.POSTGRES_HOST}")
    print(f"POSTGRES_PORT: {settings.POSTGRES_PORT}")

    # Проверка сборки URL из компонентов
    if not settings.DATABASE_URL.startswith('postgresql://'):
        print(f"\nОшибка: DATABASE_URL должна начинаться с postgresql://")
    else:
        print(f"\nDATABASE_URL корректно сформирована")

    print("\n" + "=" * 60)
    print("Тест завершен!")

except ImportError as e:
    print(f"\nОшибка импорта: {e}")
    print("\nПроверь структуру папок:")
    print("  ./")
    print("  ├── test_config.py")
    print("  ├── .env")
    print("  └── app/")
    print("      └── core/")
    print("          └── config.py")

except Exception as e:
    print(f"\nОшибка: {e}")