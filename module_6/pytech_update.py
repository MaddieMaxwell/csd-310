import pymongo
#establish a connection to the database
connection = pymongo.MongoClient ("mongodb://localhost")

#get handle for the school database

db = connection.school
students = db.students
cursor = collection.find()

for record in cursor:
    print(record)
    result = collection.update_one(
        {"student_id": '1007'},{"$set":{"last_name": "Green"}})
cursor = collection.find()
for record in cursor:
    print(record)