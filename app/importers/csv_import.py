from sqlalchemy import Column, String, Date,Integer
from sqlalchemy.ext.declarative import declarative_base
from models.database import BaseSQL,engine


#Base = declarative_base()
#BaseSQL.metadata.create_all(engine)

class MusicVideo(BaseSQL):
    __tablename__ = 'music_videos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date)
    artist = Column(String)
    song_name = Column(String)
    korean_name = Column(String)
    director = Column(String)
    video = Column(String)
    type = Column(String)
    release = Column(String)

    def __repr__(self):
        return f"<MusicVideo(artist={self.artist}, song_name={self.song_name})>"
    
    


    

