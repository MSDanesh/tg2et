from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer

from .base import Base


class Channel(Base):
    __tablename__ = "channels"

    id = Column(Integer, primary_key=True)

    tg = Column(Integer, unique=True, nullable=False)
    et = Column(Integer, unique=True, nullable=False)

    posts = relationship(
        "Post",
        backref="channel",
        cascade="all, delete-orphan"
    )
