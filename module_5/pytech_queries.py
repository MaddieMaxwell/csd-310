#create a pymongo client
client = MongoClient("localhost", 27107)

#get the database
db = client["mydb"]

#db collection
pytech = db[PyTech]

#insert 3 students
records = [
    {
        "student_id": "1007",
        "first_name": "John",
        "last_name": "Ham"
    },
    {
        "student_id": "1008",
        "first_name": "Leah",
        "last_name": "Brown"
    },
    {
        "student_id": "1009",
        "first_name": "Eli",
        "last_name": "Green"
    }
]