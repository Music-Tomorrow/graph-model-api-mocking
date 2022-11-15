from typing import List, Optional


from pydantic import BaseModel


class Artist(BaseModel):
    artist_name: str
    artist_spotify_id: str
    image_url: str

    class Config:
        orm_mode = True


class Artists(BaseModel):
    artists: List[Artist]

    class Config:
        orm_mode = True


class User(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserArtist(BaseModel):
    artist_id: int
    user_id: int

    class Config:
        orm_mode = True


class UserArtists(BaseModel):
    user_artists: List[UserArtist]

    class Config:
        orm_mode = True
