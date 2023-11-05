import DatabaseHandler
import requests
from numpy.random import randint

TOP_X_TRACKS = 5
TOP_X_GENRES = 5
TOP_X_ARTISTS = 5
TOP_X_ALBUMS = 5
def find_all_listening_data(access_token: str) -> dict:
    """Retrieve's the user's listening data and computes their
    listening data that will be used in matching calculation"""
    headers = {"Authorization": f"Bearer {access_token}"}

    url = 'https://api.spotify.com/v1/me/top/tracks?limit=30'
    response = (requests.get(url, headers = headers)).json()
    result = dict()

    top_30_tracks = list()
    top_tracks = list()
    top_albums = list()
    top_artists = list()
    top_genres = list()

    iteration_number = 0
    for x in response['items']:
        top_30_tracks.append(x['name'])
        if(iteration_number<TOP_X_TRACKS):
            top_tracks.append(x['name'])
        if (iteration_number < TOP_X_ALBUMS):
            top_albums.append(x['album']['name'])
        iteration_number += 1

    url2 = 'https://api.spotify.com/v1/me/top/artists?limit=' + str(TOP_X_ARTISTS)
    response2 = (requests.get(url2, headers = headers)).json()

    iteration_number = 0
    for x in response2['items']:
        if (iteration_number < TOP_X_ARTISTS):
            top_artists.append(x['name'])
        if(iteration_number < TOP_X_GENRES):
            top_genres.extend(x['genres'])
        iteration_number+=1

    result["top_30_tracks"] = top_30_tracks
    result["top_tracks"] = top_tracks
    result["top_albums"] = top_albums
    result["top_artists"] = top_artists
    result["top_genres"] = top_genres

    return result


def store_user_data(database: DatabaseHandler, access_token):
    """Given a user's spotify access token, retrieves the user's data from
    Spotify API and stores data in database"""
    #check if user already exists
    headers = {"Authorization": f"Bearer {access_token}"}

    url = 'https://api.spotify.com/v1/me'

    response = requests.get(url, headers = headers)
    user_data_spotify = response.json()
    user_spotify_name = user_data_spotify['display_name']

    listening_data = find_all_listening_data(access_token)
    #user exists
    user_data_db = database.get_data("name",user_spotify_name)
    print(user_data_db)
    if(user_data_db!=None):
        data = {"_id": user_data_db["_id"], "name": user_spotify_name,
                "top_tracks": listening_data["top_30_tracks"],
                "top_artists": listening_data["top_artists"],
                "top_genres": listening_data["top_genres"],
                "top_tracks": listening_data["top_tracks"],
                "top_albums": listening_data["top_albums"]}

    #user doesn't exist, create new user and insert their data
    else:
        data = {"_id": (database.get_max_id())+1, "name": user_spotify_name,
                  "top_tracks": listening_data["top_30_tracks"],
                      "top_artists":listening_data["top_artists"],
                    "top_genres": listening_data["top_genres"],
                    "top_tracks": listening_data["top_tracks"],
                      "top_albums":listening_data["top_albums"]}

        database.insert_data(data)

def get_random_person(users_database: DatabaseHandler, users_id: int) -> dict:
    """Returns a random user's information from database"""
    #AVOID USERS ID
    maxID = users_database.get_max_id()
    randomID = randint(0, maxID)
    while(users_id == randomID):
        randomID = randint(0, maxID)

    # retrieve that person2 data and store as dict
    return users_database.get_data("_id", randomID)

def user_id(database: DatabaseHandler, access_token: str):
    """Return's the user with the access token's id number"""
    url = 'https://api.spotify.com/v1/me'
    headers = {"Authorization": f"Bearer {access_token}"}

    response = requests.get(url, headers = headers)
    user_data_spotify = response.json()
    user_spotify_name = user_data_spotify['display_name']

    return database.get_data("name", user_spotify_name)['_id']


def calculate_match(person1: dict, person2: dict) -> bool:
    """Given two users, calculate their compatibility and return true
    false"""
    #artist compatability
    art1 = person1["top_artists"]
    art2 = person2["top_artists"]
    art  = 0.4 * len(set(art1) & set(art2))

    #genre compatability
    gen1 = person1["top_genres"]
    gen2 = person2["top_genres"]
    gen = 0.3 * len(set(gen2) & set(gen2))

    #song preferences
    song1 = person1["top_songs"]
    song2 = person2["top_songs"]
    song = 0.2 * 0.5 * len(set(song1) & set(song2))

    #album preferences
    alb1 = person1["top_albums"]
    alb2 = person2["top_albums"]
    alb = 0.1 * len(set(alb1) & alb2(2))

    #calculate score
    return (art + gen + song + alb)>=1
