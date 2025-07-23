from sqlalchemy.sql.schema import Column, ForeignKey, UniqueConstraint
from sqlalchemy.sql.sqltypes import Integer

from .base import Base


class Post(Base):
    __tablename__ = "posts"

    tg = Column(Integer, ForeignKey("channels.tg"), nullable=False)

    tg_id = Column(Integer, primary_key=True)
    et_id = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("tg", "tg_id", name="uq_channel_post"),
    )
