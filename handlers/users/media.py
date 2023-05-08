from loader import dp
from aiogram.types import ContentType, Message, MediaGroup

@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_id(message: Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_id(message:Message):
    await message.reply(message.video.file_id)

@dp.message_handler(text="/photo")
async def send_photo(message:Message):
    chat_id= message.from_user_id
    photo_file_id="ID"
    photo_url="URL"
    photo_bytes="path or bytes"
    video_file_id="ID"
    video_url="URL"
    video_bytes="path or url"
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id, caption="Описание")
    await dp.bot.send_video(chat_id=chat_id, video=video_file_id)

@dp.message_handler(text="/album")
async def send_album(message: Message):
    album= MediaGroup()
    photo_file_id="ID"
    video_file_id="ID"
    album.atach_photo(photo=photo_file_id, caption="Описание")
    album.atach_video(video=video_file_id)
    await message.answer_media_group(media=album)
