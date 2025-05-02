from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from src.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    # telegram_id = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    todos = relationship("Todo", back_populates="owner")

class ToDo:
    pass