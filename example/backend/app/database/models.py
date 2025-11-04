from sqlalchemy import Column, Integer, String
from example.backend.app.database.session import Base

class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
