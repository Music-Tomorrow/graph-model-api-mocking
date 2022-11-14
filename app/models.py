from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Artist(Base):
    __tablename__ = "artists"

    id = Column(Integer, primary_key=True, index=True)
    artist_name = Column(String, unique=True, index=True)
    artist_spotify_id = Column(String, unique=True, index=True)

class UserArtists(Base):
    __tablename__ = "user_artists"

    id = Column(Integer, primary_key=True, index=True)
    artist_id = Column(Integer,  index=True)
    user_id = Column(Integer,  index=True)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
