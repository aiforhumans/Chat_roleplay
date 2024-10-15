import requests
def get_models():
    response = requests.get("http://localhost:1234/v1/models")
    if response.status_code == 200:
        models = response.json()
        return [model["id"] for model in models["data"]]
    else:
        return [f"Error fetching models: {response.status_code} - {response.text}"]