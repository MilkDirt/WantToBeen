from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

class Place(BaseModel):
    name: str
    city: str
    status: str
    note: str

app = FastAPI()

""" Sql code """

sqlite3.connect("Tracker.db")


""" Fast API code"""

@app.get("/places")
def get_places():
    return places

@app.post("/places")
def create_place(place: Place):
    add_place(place.name, place.city, place.status, place.note)
    return {"message": "Place added"}

@app.patch("/places/{name}")
def visit_place(name: str):
    mark_visited(name)
    return {"message": f"{name} marked as visited"}

""" Table """

places = [
    {
    "name": "Japan", 
    "city": "Tokyo", 
    "status": "Not Visited",
    "note": "I want to visit"
},
{
    "name": "Poland", 
    "city": "Warsaw", 
    "status": "Visited",
    "note": "Very cool place, would like to go again"
}
]

""" Functions """

def list_places():
    for place in places:
        print(place)

def add_place(name, city, status, note):
    new_place = {
        "name": name,
        "city": city,
        "status": status,
        "note": note
    }
    places.append(new_place)

def mark_visited(name):
    for place in places:
        if place["name"]==name:
            place["status"] = "Visited"
            return


add_place("Italy", "Rome", "Not Visited", "Want to see the Colosseum") 
mark_visited("Italy")    
list_places()