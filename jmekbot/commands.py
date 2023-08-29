from aiogram import Dispatcher, types


async def set_default_commands(dp: Dispatcher) -> None:
    await dp.bot.set_my_commands(
        [
            types.BotCommand("anekdot", "Случайный анекдот с 'anekdot.ru'"),
        ]
    )