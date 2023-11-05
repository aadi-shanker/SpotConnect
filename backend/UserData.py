import DatabaseHandler
import requests

TOP_X_TRACKS = 5
TOP_X_GENRES = 5
TOP_X_ARTISTS = 5
TOP_X_ALBUMS = 5
def find_all_listening_data(access_token: str) -> dict:
    headers = {"Authorization": f"Bearer {access_token}"}

    url = 'https://api.spotify.com/v1/me/top/tracks?limit=30'

    response = (requests.get(url, headers = headers)).json()
    result = dict()

    top_30_tracks = list()
    top_tracks = list()
    top_artists = list()
    top_genres = list()
    top_albums = list()

    for x in response['items']:
        print(x)

    # iteration_number = 0
    # for x in response['items']:
    #     print(x)
    #     for k in x:
    #         print(k)
    #     if(iteration_number<TOP_X_TRACKS):
    #         top_tracks.append(x['name'])
    #     if (iteration_number < TOP_X_GENRES):
    #         top_tracks.append(x['genres'])
    #     if (iteration_number < TOP_X_ALBUMS):
    #         top_tracks.append(x['name'])
    #     ++iteration_number
    #     top_30_tracks.append(x['name'])
    #     print(x['type'])

    #print(top30)
    return result


def store_user_data(database: DatabaseHandler, access_token):
    """Given a user's spotify token, retrieves the user's data from
    Spotify API and stores data in database"""
    #check if user already exists
    headers = {"Authorization": f"Bearer {access_token}"}

    url = 'https://api.spotify.com/v1/me'

    response = requests.get(url, headers = headers)
    user_data = response.json()
    user_spotify_name = user_data['display_name']

    #user exists
    if(database.get_data("spotify_name",user_spotify_name)==None):
        pass
    #user doesn't exist, create new user and insert their data
    else:
        sampleData = {"_id": 0, "name": "Bob Smith", "spotify_name": "Han Seo", "date of birth": "23/01/2001",
                  "top 30 tracks": [], "top 5 artists":[], "top 5 genres":[],
                  "top 10 tracks": [], "top 5 albums":[]}

        database.insert_data(sampleData)

    #store user's name, dob, social media handle, top 30 tracks, top 5 artists, top 5 genres,
    #top 10 songs, top 5 albums



def retrieve_top_30_tracks(access_token) -> list[str]:
    """Given a user's token, retrieves user's top 30 tracks from
    Spotify API"""

    headers = {"Authorization": f"Bearer {access_token}"}

    url = 'https://api.spotify.com/v1/me/top/tracks?limit=30'

    response = requests.get(url, headers = headers)
    top30tracks = response.json()
    result = list()
    for x in top30tracks['items']:
        result.append(x['name'])

    return result

def calculate_match(person1: dict, person2: dict) -> bool:
    """Given two persons, uses their data to calculate compatibility"""
    raise NotImplemented
    """Given two users, calculate their compatibility and return true
    false"""
     
    #artist compatability
    art1 = person1["top 5 artists"]
    art2 = person2["top 5 artists"]
    art  = 0.4 * len(set(art1) & set(art2))

    #genre compatability
    gen1 = person1["top 5 genres"]
    gen2 = person2["top 5 genres"]
    gen = 0.3 * len(set(gen2) & set(gen2))

    #song preferences
    song1 = person1["top 10 songs"]
    song2 = person2["top 10 songs"]
    song = 0.2 * 0.5 * len(set(song1) & set(song2))

    #album preferences
    alb1 = person1["top 5 albums"]
    alb2 = person2["top 5 albums"]
    alb = 0.1 * len(set(alb1) & alb(2))

    #calculate score
    score = art + gen + song + alb

    returnValue = False

    if score >= 1:
        returnValue = True

    return returnValue
