from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database connection URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create the asynchronous engine
engine = create_async_engine(DATABASE_URL, echo=False)  # Set echo to False

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

# Create a Base class for declarative models
Base = declarative_base()

# Dependency to get a session for the database
async def get_db():
    async with SessionLocal() as session:
        yield session
