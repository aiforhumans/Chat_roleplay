import json

def load_settings():
    global settings_cache
    if settings_cache is None:
        try:
            with open("settings.json", "r") as f:
                settings_cache = json.load(f)
        except FileNotFoundError:
            settings_cache = {"temperature": 0.7, "max_tokens": 150}
    return settings_cache



def save_settings(temperature, max_tokens):
    global settings_cache
    settings_cache = {"temperature": temperature, "max_tokens": max_tokens}
    try:
        with open("settings.json", "w") as f:
            json.dump(settings_cache, f)
        settings_cache = None  # Clear cache after saving
        return "Settings saved successfully."
    except FileNotFoundError:
        return "File not found error while saving settings."
    except IOError as e:
        return f"I/O error occurred: {str(e)}"