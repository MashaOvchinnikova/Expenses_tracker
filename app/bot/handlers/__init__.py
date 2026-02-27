# Собираем все обработчики команд
from app.bot.handlers.start import cmd_start, cmd_help
from app.bot.handlers.add import cmd_add
from app.bot.handlers.today import cmd_today
from app.bot.handlers.categories import cmd_categories

# Указываем, что экспортируем
__all__ = [
    "cmd_start",
    "cmd_help",
    "cmd_add",
    "cmd_today",
    "cmd_categories"
]