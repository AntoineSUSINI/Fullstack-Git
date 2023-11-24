from fastapi import FastAPI,Depends
from models.music_videos import MusicVideo
from models.database import SessionLocal

app = FastAPI(
    title="My title",
    description="My description",
    version="0.0.1",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/music_videos/")
def get_music_videos(db: SessionLocal = Depends(get_db)):
    # Ici, 'db' est une nouvelle session pour cette requête
    music_videos = db.query(MusicVideo).all()
    return music_videos