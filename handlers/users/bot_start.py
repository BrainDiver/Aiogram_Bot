from aiogram import types
from loader import dp
from utils.misc import rate_limit
from utils.db_api import quick_commands as commands
from aiogram.utils.deep_linking import get_start_link
from aiogram.dispatcher.filters import Command

@rate_limit(limit=5, key="/start")
@dp.message_handler(Command("start"))
async def command_start(message: types.Message):
    args= message.get_args()
    new_args= await commands.check_args(args, user_id= message.from_user.id)
    try:
        user= await commands.select_user(message.from_user.id)
        if user.status == "active":
            await message.answer(f"Привет {user.first_name}\n"
                                 f"Вы уже подписаны")
        elif user.status == "banned":
            await message.answer("Вы забанены")
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name= message.from_user.last_name,
                                username=message.from_user.username,
                                status="active",
                                referral_id=int(new_args),
                                balance=0)
        try:
            await dp.bot.send_message(chat_id=int(new_args), text=f"По твоей ссылке зарегистрировался {message.from_user.full_name}")
        except:
            pass
        await message.answer("Вы успешно подписались")

@dp.message_handler(text="/ban")
async def get_ban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status="banned")
    await message.answer("Мы вас забанили")

@dp.message_handler(text="/unban")
async def get_unban(message: types.Message):
    await commands.update_status(user_id=message.from_user.id, status="active")
    await message.answer("Мы вас разбанили")

@dp.message_handler(text="/profile")
async def get_profile(message: types.Message):
    user= await commands.select_user(user_id=message.from_user.id)
    await message.answer(f"id:{user.user_id}\n"
                         f"first_name:{user.first_name}\n"
                         f"last_name:{user.last_name}\n"
                         f"username: {user.username}\n"
                         f"user.status:{user.username}")

@dp.message_handler(text="/ref_link")
async def ref(message: types.Message):
    ref_link= await get_start_link(payload=message.from_user.id)
    count_refs= await commands.count_ref(user_id=message.from_user.id)
    await message.answer(f"Твоя реферальная ссылка \n"
                         f"У тебя {count_refs} рефералов\n"
                         f"{ref_link}")

