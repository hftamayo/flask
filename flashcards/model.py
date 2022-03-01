"""

read the json content

"""

import json

def load_data():
    with open("flashcards_db.json") as f:
        return json.load(f)

data = load_data()

