from scripts.constants.app_constants import Db_database
from pymongo import MongoClient

client = MongoClient(Db_database.db_uri)
db = client[Db_database.db_name]
collection = db[Db_database.db_collection]
