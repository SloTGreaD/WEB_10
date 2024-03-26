from pymongo import MongoClient

def get_mongodb():
    client = MongoClient('mongodb+srv://bayonetttt74:Chibeurnyna74@cluster0.mjfoeks.mongodb.net/')

    db = client.hm
    return db