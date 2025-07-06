from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["Hospital"]
per_col = db["Person"]
doc_col = db["Doctor"]
pat_col = db["Patient"]

per_col.insert_one({
    "_id": 0,
    "Name": "Sohail",
    "Cnic": "01"
})
doc_col.insert_one({
    "_id": 0,
    "Speciality": "General Sergeon",
    "Dcnic": "01"
})

per_col.insert_one({
    "_id": 1,
    "Name": "Sohail",
    "Cnic": "02"
})
pat_col.insert_one({
    "_id": 1,
    "Pcnic": "02",
    "condition": "Broken leg",
    "Dcnic": "01"
})

# Retrieve patient and their doctor and display toString Method
patient = {**per_col.find_one({'Cnic': '02'}), **pat_col.find_one({'Pcnic': '02'})}
doctor = {**per_col.find_one({"Cnic": str(patient['Dcnic'])}), **doc_col.find_one({"Dcnic": str(patient['Dcnic'])})}
print("The Patient details are as follows:")
for i, j in patient.items():
    if not i == 'Dcnic':
        print(i, ":", j)

print("\nHis Corresponding Doctors details are as follows:")
for i, j in doctor.items():
    print(i, ":", j)

client.close()
