from telethon.sync import TelegramClient
import asyncio

API_ID = '24410919'
API_HASH = '11a3a20ee4f9e851e35412b0a2eedb3a'
SESSION_NAME = 'account1'

client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

async def keep_online():
    await client.start()
    print("✅ Shaxsiy akkaunt 1 onlayn!")
    
    while True:
        await client.send_message('me', '🟢 2-Server orqali ishga tushurilgan!')
        await asyncio.sleep(35)

if __name__ == "__main__":
    asyncio.run(keep_online())