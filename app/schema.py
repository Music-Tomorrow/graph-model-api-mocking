from typing import List, Optional


from pydantic import BaseModel


class Artist(BaseModel):
    artist_name: str
    artist_spotify_id: str

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
