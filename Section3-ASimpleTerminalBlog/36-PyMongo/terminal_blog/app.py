"""
Start mongod server first:
``` sudo systemctl start mongod ```
By default, MongoDB starts at port 27017

The database fullstack was created externally by command-line.
"""

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database["students"]

students = [student for student in collection.find({})]
print(students)
