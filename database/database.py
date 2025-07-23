from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import async_sessionmaker

from sqlalchemy.dialects.sqlite.aiosqlite import AsyncAdapt_aiosqlite_connection

from sqlalchemy.event.api import listens_for

from .methods import Methods
from .tables import Base

from dotenv.main import dotenv_values


env = dotenv_values()

class Database(Methods):
    _engine = create_async_engine(
        url=URL.create(
            drivername="sqlite+aiosqlite",
            database=env.get("DATABASE_NAME", ":memory:")
        )
    )

    def __init__(self) -> None:
        self.session = async_sessionmaker(bind=self._engine, expire_on_commit=False)

    async def create_base(self) -> None:
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)


@listens_for(Database._engine.sync_engine, "connect")
def on_connect(conn: AsyncAdapt_aiosqlite_connection, _):
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
