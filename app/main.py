from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenID
from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED
from models.music_videos import MusicVideo
from models.database import SessionLocal
import os
import logging
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse

# Configuration de Keycloak
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL", "http://localhost:8080") 
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM", "master")  
KEYCLOAK_CLIENT_ID = os.getenv("KEYCLOAK_CLIENT_ID", "test")  
KEYCLOAK_CLIENT_SECRET = os.getenv("KEYCLOAK_CLIENT_SECRET", "0TWNpMXZdduaI0sbrH7LPm6TLSiYglIn") 

# Initialisation du client Keycloak
keycloak_openid = KeycloakOpenID(server_url=KEYCLOAK_URL,
                                 client_id=KEYCLOAK_CLIENT_ID,
                                 realm_name=KEYCLOAK_REALM,
                                 client_secret_key=KEYCLOAK_CLIENT_SECRET)

# Initialisation de FastAPI
app = FastAPI(title="Projet FullStack", version="0.0.1")

# Configuration de OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token")

# Configuration de l'authentification
logging.basicConfig(level=logging.INFO)

def get_current_user(token: str = Depends(oauth2_scheme)):
    logging.info(f"Receiving token: {token}")
    try:
        user_info = keycloak_openid.decode_token(token, key=KEYCLOAK_CLIENT_SECRET)
        logging.info(f"User info from token: {user_info}")
        return user_info
    except Exception as e:
        logging.error(f"Error decoding token: {e}")
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")

app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

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
#def get_music_videos(db: SessionLocal = Depends(get_db), user: dict = Depends(get_current_user)): # L'utilisateur doit être authentifié pour accéder à cette route
def get_music_videos(db: SessionLocal = Depends(get_db)):
    music_videos = db.query(MusicVideo).all()
    return music_videos

@app.get("/front/")
async def read_root():
    return FileResponse('static/index.html')