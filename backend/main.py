"""
Starts the server
Contains HTTP communication config 
Sets up routes
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  #cors = cross origin resource sharing

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)
from model import Todo

# create App object
app = FastAPI()


# Set cross origin permissions and other http communication configs
origins = ['https://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# static (?) roots

@app.get("/")
def read_root():
    return {"Ping":"Pong"}

# api routes 

@app.get("/api/todo")
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/todo{title}", response_model=Todo)       # use response_model=Todo because we are expecting it to return an instance of Todo class
async def get_todo_by_id(title):
    response = fetch_one_todo(title)
    if response:
        return response
    else:
        raise HTTPException(404, f"There is no TODO item with this title: {title}")

@app.post("/api/todo", response_model=Todo)
async def post_todo(todo:Todo):
    response = await create_todo(todo.model_dump()) # use model_dump to make sure the given todo is converted to right format for Todo class (?)
    if response:
        return response
    else:
        raise HTTPException(400, "Bad request")

@app.put("/api/todo{title}", response_model=Todo)
async def put_todo(title:str, desc:str):
    response = await update_todo(title, desc)
    if response:
        return response
    else:
        raise HTTPException(404, f"There is no TODO item with this title: {title}")

@app.delete("/api/todo{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return f"Successfully deleted todo item: {title}"
    else:
        raise HTTPException(404, f"There is no TODO item with this title: {title}")
