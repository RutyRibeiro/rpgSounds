from sqlalchemy import Column, Integer, String, Delete, Select
from sqlalchemy.orm import declarative_base, sessionmaker 
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

databaseUrl = 'sqlite+aiosqlite:///db.db'

engine = create_async_engine(databaseUrl)

session = sessionmaker(
    engine,
    expire_on_commit = False,
    class_= AsyncSession
)

Base = declarative_base()

class Song(Base):
    __tablename__ = 'song'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    link = Column(String)
    tags = Column(String)
    classification = Column(String)

    def __repr__(self):
        return f'Song({self.name})'
    
async def createDatabase():
    async with engine.begin() as conn:
        # conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def createSong(name, link, tags, classification):
    async with session() as s:
        s.add(Song(name = name, link = link, tags = tags, classification = classification))
        await s.commit()

async def selectSong(id):
    async with session() as s:
        response = await s.execute(
            Select(Song).where(
                Song.id == id
            )
        )
    return response.all()

async def deleteSong(id):
    async with session() as s:
        await s.execute(
            Delete(Song).where(
                Song.id == id
            )
        )
        await s.commit()

# run(createDatabase()) 
# run(createSong('seila','seila.com.br', 'Forró, Animado, Dança, Feliz', 'Forró')) 
# print (run(selectSong(1)) )
# run(deleteSong(2))
