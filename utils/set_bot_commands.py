from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запуск бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("menu", "Текстовое меню"),
        types.BotCommand("inline_menu", "Инлайн меню"),
        types.BotCommand("register", "Регистрация"),
        types.BotCommand("profile", "Получить данные профиля"),
        types.BotCommand("subscribe", "Подписаться")
    ])
