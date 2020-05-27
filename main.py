# Do this in python shell in command prompt

from pymongo import MongoClient

my_client = MongoClient()
# Create database
db = my_client.my_database
# Variable, collection can be accessed with . or as dictionary
users = db.users
# Create user object, for inserting doc into db
user1 = {"username": "Kari", "password": "dkdjhg", "fav_number": 11, "hobbies": ["xbox", "art", "reading"]}
# Insert, will return ID, create method of collection
user_id = users.insert_one(user1).inserted_id
# Insert multiple docs, create list objects
users = [{"username": "user2", "password": "12345"}, {"username": "user3", "password": "23456"}]
Users = db.users
inserted = Users.insert_many(users)
inserted.inserted_ids







