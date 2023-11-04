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
