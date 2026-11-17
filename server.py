# SYNTHETIC TEST FIXTURE — inert sample, do not run, do not report.
import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1234567890:AAFakeTokenForTestsOnly1234567890abc")

# Данные для входа через Telegram (/login admin testpass123)
ADMINS = {"admin": "testpass123"}

# --- ловушки, которые НЕ должны давать грязных находок ---
# (/login admin parentrap)          <- скобка не должна попадать в значение
HELP_TEXT = "используйте /login логин пароль"   # кириллица — не команда

# многострочная ловушка (как в реальном диффе):
# /login
# @bot.message_handler(commands=['login'])
# def handle_login(message):
#     pass