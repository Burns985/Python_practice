import pymongo
from pymongo.errors import DuplicateKeyError

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client['Hospital']
collection = db['Person']

projection = {'_id': 0}

doctors = list(collection.find({}, projection))

for doctor in doctors:
    print(doctor.items())

try:
    new_doc = {
        "_id": "01",
        'name': 'Ali Qadir',
        'specialty': 'Management Sciences',
        'experience': 13
    }

    if new_doc in doctors:
        query = {'name': new_doc['name']}
        collection.update_one(query, {'$set': new_doc}, upsert=True)
        print("Doctors Updated!")
    else:
        query = {'name': new_doc['name']}
        collection.insert_one(new_doc)
        print("Doctors Appended!")

except DuplicateKeyError:
    new_doc = {
        "_id": "02",
        'name': 'Varis Qadir',
        'specialty': 'Software Engineering',
        'experience': .1
    }
    collection.insert_one(new_doc)
    print("Doctors Appended!")

client.close()
