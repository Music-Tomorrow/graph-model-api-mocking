import requests
import json

url = "http://localhost:8000/user/"
user = {"username": "max", "password": "max"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(user), headers=headers)
# print(response)

artists = [
    {
        "artist_name": "Drake",
        "artist_spotify_id": "3TVXtAsR1Inumwj472S9r4",
        "image_url": "https://i.scdn.co/image/ab6761610000e5eb4293385d324db8558179afd9",
    },
    {
        "artist_name": "Yung Lean",
        "artist_spotify_id": "67lytN32YpUxiSeWlKfHJ3",
        "image_url": "https://i.scdn.co/image/ab6761610000e5eb33c1ea8922687859aa413547",
    },
]

data = {"artists": artists}
url = "http://localhost:8000/artists/"
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers)
# print(response.json())

url = "http://localhost:8000/user_artists/"
headers = {"Content-Type": "application/json"}
data = {"user": user, "artists": {"artists": artists}}
print(data)
response = requests.post(url, data=json.dumps(data), headers=headers)
