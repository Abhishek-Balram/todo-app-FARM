"""
This file defines data model for the Todo class 
It is crucial that documents in the MongoDB collection also follow this data model
"""

from pydantic import BaseModel

class Todo(BaseModel):
    title: str
    description: str
    completed: bool = False