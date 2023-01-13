for record in records:
    new_student_Id = pytech.insert_one(record).insert_id
    print(new_student_Id)

#display all document in collections
docs = pytech.find()

for doc in docs:
    print(doc)

#display a single document by student_id
print(pytech.find_one({"student_id": "1008"}))