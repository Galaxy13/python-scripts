import datetime

from pymongo import MongoClient

cluster = 'mongodb+srv://retroider:btgmupzZFu9H7lGB@cluster0.bofqv.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(cluster)

print(client.list_database_names())

db = client["test"]

print(db.list_collection_names())

todo1 = {"name": "Patrick",
         "text": "My first todo!",
         "status": "open",
         "tags": ["python", "coding"],
         "date": str(datetime.datetime.utcnow())}

todos = db.todos

# todos.insert_one(todo1)

todo2 = [{
    "name": "Gennadiy",
    "text": "My second todo!",
    "status": "open",
    "tags": ["pytnon", "coding"], "date": datetime.datetime.utcnow()
},
    {
        "name": "Frol",
        "text": "Sakharok",
        "status": "open",
        "tags": ["pidor", "gachi"],
        "date": datetime.datetime.utcnow()
    }]
# db.todos.insert_many(todo2)

from bson.objectid import ObjectId

# get_from_db = db.todos.find({"status": "open"})
# print(get_from_db)
# print(db.todos.count_documents({"tags": 0}))
# for table in get_from_db:
#     print(table)

# d = datetime.datetime(2021, 2, 1)
# get_from_db = db.todos.find({"date": {"$gt": d}}).sort("name")
# for doc in get_from_db:
#     print(doc)

# db.todos.delete_one({"name": "Patrick"})
#
# get_from_db = db.todos.find({})
# db.todos.count_documents({})
# for doc in get_from_db:
#     print(doc)

db.todos.update_one({"tags": "pidor"}, {"$setOnInsert": {"tags": ["van"]}})