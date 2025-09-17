from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from config import settings

engine = create_async_engine(
    url=settings.DB_URL,
    echo=True
)

create_session = async_sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=True,
    class_=AsyncSession
)

async def get_db():
    session = create_session()
    try:
        yield session
        await session.commit()
    except:
        await session.rollback()
        raise
    finally:
        await session.close()


