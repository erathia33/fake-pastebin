import asyncio
from .database import engine

from models.models import Base, PostModel
async def create_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

asyncio.run(create_database())