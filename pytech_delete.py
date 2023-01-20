#!usr/bin/env python

import pymongo
#establish a connection to the database
connection = pymongo.MongoClient ("mongodb://localhost")

#get handle for the school database

db = connection.school
students = db.students

def find():
    print("find, reporting for duty")

def find_one(): 
    print("find one, reporting for duty")

def delete_one(): 
    print("delere one, reporting for duty")

def delete_multiple():
    print(" delete multiple, reporting for duty")


if _name_ == '_main_':
    find()
    find_one()
    delete_one()
    delete_multiple()

query = {'last_name': "Green"}

students.delete_multiple(query)

query = {'last_name': 'Green'}

cursor = students.find(query)

for doc in cursor:
    print(doc)

query = {'last_name': 'Green'}

result = students.delete_multiple(query)
print(result.deleted_count)