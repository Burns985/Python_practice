from pymongo import MongoClient

data = [
    {
        "_id": 1001,
        "Name": "Sohail",
        "Cnic": "01",
        "Type": "Doctor",
        "Speciality": "General Surgeon"
    },
    {
        "_id": 1002,
        "Name": "Sohail",
        "Cnic": "02",
        "Type": "Patient",
        "condition": "Broken leg",
        "Dcnic": "01"
    }
]


# Optimize 1: Use bulk write operations for insertion
with MongoClient("mongodb://localhost:27017") as client:
    db = client["Hospital"]
    col = db["People"]
    col.insert_many(data)

# Optimize 2: Create Indexes for querying
col.create_index("Cnic")
col.create_index("Dcnic")

# Optimize 3: Use projection to retrieve only required fields
patient_doctor_pipeline = [
    {
        "$match": {"Cnic": "02"}
    },
    {
        "$lookup": {
            "from": "People",
            "localField": "Dcnic",
            "foreignField": "Cnic",
            "as": "doctor"
        }
    },
    {
        "$unwind": "$doctor"
    },
    {
        "$project": {
            "_id": 0,
            "Type": 1,
            "Name": 1,
            "Cnic": 1,
            "Speciality": "$doctor.Speciality",
            "condition": 1,
            "Dcnic": 1,
        }
    }
]

# Optimize 4: Combine patient and doctor details printing
with MongoClient("mongodb://localhost:27017") as client:
    db = client["Hospital"]
    col = db["People"]

    result = col.aggregate(patient_doctor_pipeline)

    for person in result:
        if person["Type"] == "Patient":
            print("The Patient details are as follows:")
        elif person["Type"] == "Doctor":
            print("\nHis Corresponding Doctor details are as follows:")

        for key, value in person.items():
            if key == "doctor":
                print(key.title(), ":")
                for doctor_key, doctor_value in value.items():
                    print("  ", doctor_key, ":", doctor_value)
            elif key not in ["Type", "Dcnic"]:
                print(key, ":", value)
