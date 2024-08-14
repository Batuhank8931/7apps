import asyncio
from app.database import engine
from app.models import Base

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Run the table creation
if __name__ == "__main__":
    asyncio.run(create_tables())
