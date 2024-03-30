import os
import django
from pymongo import MongoClient
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hm_project.settings')
django.setup()

from quotes.models import Quote, Tag, Author

client = MongoClient('mongodb+srv://bayonetttt74:Chibeurnyna74@cluster0.mjfoeks.mongodb.net/')
db = client.hm

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        name = author['name'],
        birthday = author['birthday'],
        bio = author['bio']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)
    
    exist_quote = bool(len(Quote.objects.filter(quote=quote['text'])))

    if not exist_quote:
        author = db.authors.find_one({'name': quote['author']})
        a = Author.objects.get(name=author['name'])
        q = Quote.objects.create(
            quote=quote['text'],
            author=a
        )
        for tag in tags:
            q.tags.add(tag)