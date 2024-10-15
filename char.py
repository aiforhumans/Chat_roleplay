import json

def load_character():
    global character_cache
    if character_cache is None:
        try:
            with open("character.json", "r") as f:
                character_cache = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            character_cache = {
                "name": "Character",
                "age": "",
                "gender": "",
                "personality_traits": "",
                "description": "",
                "occupation": "",
                "hobbies": "",
                "favorite_quote": "",
                "backstory": ""
            }
    return character_cache

def save_character(name, age, gender, personality_traits, description, occupation, hobbies, favorite_quote, backstory):
    global character_cache
    character_cache = {
        "name": name,
        "age": age,
        "gender": gender,
        "personality_traits": personality_traits,
        "description": description,
        "occupation": occupation,
        "hobbies": hobbies,
        "favorite_quote": favorite_quote,
        "backstory": backstory
    }
    try:
        with open("character.json", "w") as f:
            json.dump(character_cache, f, indent=4)
        character_cache = None  # Clear cache after saving
        return "Character information saved successfully."
    except IOError as e:
        return f"I/O error occurred: {str(e)}"
