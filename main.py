from telethon.sync import TelegramClient
import asyncio
import os
from flask import Flask

API_ID = '24410919'  # O'zingizning API_ID ni qo'ying
API_HASH = '11a3a20ee4f9e851e35412b0a2eedb3a'  # O'zingizning API_HASH ni qo'ying
SESSION_NAME = 'account1'  # Sessiya nomi

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Telegram bot ishga tushdi!"

async def keep_online():
    await client.start()
    print("✅ Shaxsiy akkaunt onlayn!")

    while True:
        await client.send_message('me', '🟢 Ishga tushurilgan!')  # Har 35 soniyada xabar yuboradi
        await asyncio.sleep(35)  # 35 sekund kutadi

async def main():
    await asyncio.gather(
        keep_online(),
        asyncio.to_thread(app.run, host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))  # Portni sozlash
    )

if __name__ == "__main__":
    asyncio.run(main())
