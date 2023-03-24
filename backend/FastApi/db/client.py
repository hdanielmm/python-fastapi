import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Base de datos local

# db_client = MongoClient().local

# Base de datos remota

client = MongoClient("mongodb+srv://" + user + ":" + password + "@cluster0.ypgfhts.mongodb.net/?retryWrites=true&w=majority")
db_client = client.test
