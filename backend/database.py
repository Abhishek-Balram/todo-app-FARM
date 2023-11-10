"""
This file contains logic for interacting with database. 
All CRUD operations are asynchronous - requiring the motor library
It is crucial that documents in the MongoDB collection have the same data model as the Todo class
"""
from model import Todo

# Import an asynchronous MongoDB driver - The official MongoDB driver for Python (PyMongo) does not support asynchronous
import motor.motor_asyncio

# Client for connection between database.py and MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://abhi:0UwfnG7v9VxnZVNg@cluster0.oauqir0.mongodb.net/?retryWrites=true&w=majority")
database = client.TodoList
collection = database.todo      # collection is the same thing as a Table




# Functions to perform CRUD operations

async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document


async def fetch_all_todos():
    todos = []
    documents = collection.find({})    # gets all documents in collection
    async for document in documents:
        # convert every document into a Todo object - this requires that the data model in the Todo class matches the structure of the documents in the collection
        todos.append(Todo(**document)) 
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(title, desc):
    #Find a document in the collection with a given title, change its description to the given desc
    await collection.update_one({"title":title}, {"$set":{
        "description":desc
    }})

    #find and return the updated document
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True