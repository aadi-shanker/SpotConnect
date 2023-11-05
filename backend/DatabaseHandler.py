import pymongo
from pymongo import MongoClient

#cluster = MongoClient("mongodb+srv://zothacksaccess:GJScvqfVaZqPyOAe@cluster0.trzhtkt.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp")
#db = cluster["SpotConnect"]

class DatabaseHandler:
    def __init__(self, db_name: str, Mongo):
        self.database = db_name
        self.db = Mongo
        #self.attribute = attributes

    def insert_data(self, data: dict) -> None:
        #db.createCollection(self.collection, data)
        self.db[self.database].insert_one(data)

    def get_data(self, attribute: str, value: str) -> dict:
        return self.db[self.database].find_one({attribute: value})

    def get_all(self) -> list[dict]:
        #return db[self.database]
        raise NotImplemented

    def get_max_id(self) -> int:
        return self.db[self.database].find_one(sort = [("_id", pymongo.DESCENDING)])['_id']
