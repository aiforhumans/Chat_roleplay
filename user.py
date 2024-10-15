import json
def save_user(name, age, interests):
    global user_cache
    user_cache = {"name": name, "age": age, "interests": interests}
    try:
        with open("user.json", "w") as f:
            json.dump(user_cache, f)
        user_cache = None  # Clear cache after saving
        return "User information saved successfully."
    except FileNotFoundError:
        return "File not found error while saving user information."
    except IOError as e:
        return f"I/O error occurred: {str(e)}"

def load_user():
    global user_cache
    if user_cache is None:
        try:
            with open("user.json", "r") as f:
                user_cache = json.load(f)
        except FileNotFoundError:
            user_cache = {"name": "User", "age": "", "interests": ""}
    return user_cache

