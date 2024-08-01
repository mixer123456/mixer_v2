from pprint import pprint
from pymongo.mongo_client import MongoClient
import certifi

from config import PASSWORD, USER_NAME

uri = f"mongodb+srv://{USER_NAME}:{PASSWORD}@myfirstworkwithclusters.dxbkrcp.mongodb.net/?retryWrites=true&w=majority&appName=myfirstworkwithclusters"

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where())

db = client['Books']

genre_fantasy = db['genre_fantasy']
genre_fantasy.insert_one({'title': 'Гра престолів', 'price': 925, 'year': 2019, 'count_of_pages': 800})

schools_books = db['schools_books']
list_of_schools_books = [
    {'title': 'Історія України', 'class': 6, 'count_of_pages': 59},
    {'title': 'Математика', 'class': 6, 'count_of_pages': 85},
    {'title': 'Географія', 'class': 6, 'count_of_pages': 40},
    {'title': 'Біологія', 'class': 6, 'count_of_pages': 46},
    {'title': 'Фізика', 'class': 6, 'count_of_pages': 39},
]
schools_books.insert_many(list_of_schools_books)

query = {'title': {'$regex': 'Історія*'}}
find_book = list(schools_books.find(query))
pprint(find_book)


