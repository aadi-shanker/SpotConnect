"""
app.py

This one file is all you need to start off with your FastAPI server!
"""

from typing import Optional

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel
from pymongo import MongoClient

from DatabaseHandler import DatabaseHandler
import UserData

# Initializing and setting configurations for your FastAPI application is one
# of the first things you should do in your code.
app = FastAPI()


# The line starting with "@" is a Python decorator. For this tutorial, you
# don't need to know exactly how they work, but if you'd like to read more on
# them, see https://peps.python.org/pep-0318/.

# In short, the decorator declares the function it decorates as a FastAPI route
# with the path of the provided route. This line declares that a new GET route
# called "/" so that if you access "http://localhost:5000/", the below
# dictionary will be returned as a JSON response with the status code 200.

# For any other routes you declare, like the `/home` route below, you can access
# them at "http://localhost:5000/home". Because of this, we'll be omitting the
# domain portion for the sake of brevity.
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/home")
def home():
    return {"message": "This is the home page"}


# The routes that you specify can also be dynamic, which means that any path
# that follows the format `/items/[some integer]` is valid. When providing
# such path parameters, you'll need to follow this specific syntax and state
# the type of this argument.
#
# This path also includes an optional query parameter called "q". By accessing
# the URL "/items/123456?q=testparam", the JSON response:
#
# { "item_id": 123456, "q": "testparam" }
#
# will be returned. Note that if `item_id` isn't an integer, FastAPI will
# return a response containing an error statement instead of our result.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient("mongodb+srv://zothacksaccess:GJScvqfVaZqPyOAe@cluster0.trzhtkt.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
    app.database = app.mongodb_client["SpotConnect"]
    print("done with stratup")

class main(BaseModel):
    access_token: str
    handle: str

@app.post("/main")
async def main(item: main):
    users_database = DatabaseHandler("Users", app.database)
    print(f"ASKJDNJKASNDASKJND {item.access_token}")

    #store/update user's data
    UserData.store_user_data(users_database, item.access_token, item.handle)
    users_id = UserData.user_id(users_database, item.access_token)

    person1 =  users_database.get_data("_id", users_id)
    person2 =  UserData.get_random_person(users_database,users_id)
    print(f"person1: {person1}")
    print(f"person2: {person2}")

    #process both users top 50 tracks and calculate if they are a match
    while not UserData.calculate_match(person1, person2):
        person2 =  UserData.get_random_person(users_database, users_id)

    #now person1 and person 2 is a match
    print("Match found")
    #When match found, send response to front end

    return {"message": "This is the main page"}




@app.post("/main")
def main2(access_token):
    users_database = DatabaseHandler("Users")

    #store/update user's data
    UserData.store_user_data(users_database, access_token, "zot_hack")
    users_id = UserData.user_id(users_database, access_token)

    person1 = users_database.get_data("_id", users_id)
    person2 = UserData.get_random_person(users_database,users_id)
    print(f"person1: {person1}")
    print(f"person2: {person2}")

    #process both users top 50 tracks and calculate if they are a match
    while not UserData.calculate_match(person1, person2):
        person2 = UserData.get_random_person(users_database, users_id)

    #now person1 and person 2 is a match
    print("Match found")
    #When match found, send response to front end

    return {"message": "This is the main page"}



# TODO: Add POST route for demo

#for testing purposes only
if __name__ == "__main__":
    #uvicorn.run("main:app", port=5000, reload=True)

    temp_access_token = 'BQCID2ELCj-SGYZ_QGajat_efic7N87YVi06ohTlV3nfJfxEXqDZEBW7V7ryGJ6Umh6e6ruqcW037sXg8r6DJc3-ng31_lpJL4tvx2lDnvgTxZWLrzRLncMERFxORwl9Ckvv4-fE69XES3p8OO4ewdX-TEGJ9lajhJ-MhMBYCTmHzLZFExcFtHpUnDdrSFUfFNxllFrNTHxzhnx5wetjkGE7'""
    temp_access_token2 = 'BQDZmIlZZpKs6MamQ4dKxqFJA--qcfQpzRr2biqjvjxrHhk6qJsaVXYcsh3Lp7qHcPyFc6YoaAIgpVmq59uEYEWd_gQk9ddu6LcUrSEXYh1GDws9h0MLAv97LdVNUA2vPQE1Lk4puAw7hOl6t13vNLEBi7VxTkz_6Jk2bUpTSGnBjNTjfP1ZALfYj6P6SonWnQ'

    #users_database = DatabaseHandler("Users")

    #users_database.insert_data(sampleData)

    #person1 = users_database.get_data("name","Bob Smith")
    #print(person1)
    #print(type(person1))

    #UserData.store_user_data(users_database,temp_access_token,"@zothacks")

    main2(temp_access_token2)
