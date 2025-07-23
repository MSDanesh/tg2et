from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String, Integer

from .base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, default=None)
