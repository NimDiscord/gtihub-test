from motor.motor_asyncio import AsyncIOMotorClient

import os 
from dotenv import load_dotenv

load_dotenv()
database_name = os.environ.get("DATABASE_NAME")
database_url = os.environ.get("DATABASE_URL")

db = AsyncIOMotorClient(database_name)[database_url]