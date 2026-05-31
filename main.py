from telethon import TelegramClient
from datetime import datetime
import asyncio
import os

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
phone = os.getenv('PHONE')
target_username = os.getenv('TARGET_USERNAME')
message_text = "Доброе утро принцесса, Хорошего тебе дня, ты обалденная, обожаю тебя."

client = TelegramClient('session', api_id, api_hash)

async def send_message():
    await client.start(phone=phone)
    await client.send_message(target_username, message_text)
    print(f"Сообщение отправлено в {datetime.now()}")
    await client.disconnect()

if name == "__main__":
    asyncio.run(send_message())
