from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from .base import Base


class Channel(Base):
    __tablename__ = "channels"

    tg = Column(Integer, primary_key=True)
    et = Column(Integer, primary_key=True)

    posts = relationship(
        "Post",
        backref="channel",
        cascade="all, delete-orphan"
    )