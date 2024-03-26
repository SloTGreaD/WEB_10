import json 
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb+srv://bayonetttt74:Chibeurnyna74@cluster0.mjfoeks.mongodb.net/')

db = client.hm

with open('quotes.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'name': quote['author']})
    if author:
        db.quotes.insert_one({
            'text': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
        })
