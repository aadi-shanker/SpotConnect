import DatabaseHandler

def store_user_data(database: DatabaseHandler, user_token):
    """Given a user's spotify token, retrieves the user's data from
    Spotify API and stores data in database"""
    #check if user already exists

    #if user doesn't exist, create new user and insert their data


    #store user's name, dob, social media handle, top 30 tracks, top 5 artists, top 5 genres,
    #top 10 songs, top 5 albums


    raise NotImplemented


def retrieve_top_30_tracks(user_token):
    """Given a user's token, retrieves user's top 30 tracks from
    Spotify API"""
    raise NotImplemented

def calculate_match(person1: dict, person2: dict) -> bool:
    """Given two persons, uses their data to calculate compatibility"""
    raise NotImplemented