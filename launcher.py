from core.bot import Pokecord
import asyncio

async def run_bot():
    bot = Pokecord()

    async with bot:
        await bot.start()

if __name__ == "__main__":   
    asyncio.run(run_bot())


