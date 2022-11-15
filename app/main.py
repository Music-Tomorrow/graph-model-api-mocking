import uvicorn
from fastapi import FastAPI
import os
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from models import (
    User as ModelUser,
    Artist as ModelArtist,
    UserArtists as ModelUserArtists,
)
from schema import (
    User as SchemaUser,
    Artists as SchemaArtists,
    UserArtists as SchemaUserArtists,
)
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])


@app.get("/home")
def home():
    return {"message": "it works"}


@app.post("/user/", response_model=SchemaUser)
def create_user(user: SchemaUser):
    db_user = ModelUser(username=user.username, password=user.password)
    db.session.add(db_user)
    db.session.commit()
    return db_user


@app.post("/artists/", response_model=SchemaArtists)
def create_artists(artists: SchemaArtists):
    db_artists = []
    for artist in artists.artists:
        db_artists.append(
            ModelArtist(
                artist_name=artist.artist_name,
                artist_spotify_id=artist.artist_spotify_id,
                image_url=artist.image_url,
            )
        )
    db.session.bulk_save_objects(db_artists)
    db.session.commit()
    return artists


@app.post("/user_artists/")
def create_user_artists(user: SchemaUser, artists: SchemaArtists):
    user_id = (
        db.session.query(ModelUser).filter_by(username=user.username).first()
    ).id

    for artist in artists.artists:
        print(artist)
        artist_id = (
            db.session.query(ModelArtist)
            .filter_by(artist_spotify_id=artist.artist_spotify_id)
            .first()
            .id
        )
        db_user_artist = ModelUserArtists(
            artist_id=artist_id,
            user_id=user_id,
        )
        db.session.add(db_user_artist)
    db.session.commit()
    return True


@app.get("/user_artists_roster")
def get_user_artists_roster(user_email: str):
    query = f"""
    SELECT artists.* from users
    left join user_artists on user_artists.user_id = users.id
    left join artists on user_artists.artist_id = artists.id
    where username='{user_email}'
    """
    results_list = db.session.execute(query).fetchall()
    return results_list


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
