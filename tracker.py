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


add_place("Italy", "Rome", "Not Visited", "Want to see the Colosseum")     
list_places()