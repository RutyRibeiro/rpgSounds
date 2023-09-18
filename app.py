from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base 

Base = declarative_base()


class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    link = Column(String)
    tags = Column(String)
    classification = Column(String)

    def __repr__(self):
        return f'Song({self.name})'