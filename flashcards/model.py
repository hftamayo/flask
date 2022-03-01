"""

read the json content

"""

import json

def load_data():
    with open("flashcards_db.json") as f:
        return json.load(f)

def save_data():
    with open("flashcards_db.json", 'w') as f:
        return json.dump(data, f)

data = load_data()

