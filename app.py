import gradio as gr
import requests

# LM Studio API endpoint
API_URL = "http://localhost:1234/v1/chat/completions"

from model_info import get_models
from char import load_character, save_character
from user import load_user, save_user
from settings import load_settings, save_settings

# Caching loaded data to avoid repeated file access
character_cache = None
user_cache = None
settings_cache = None


def get_system_message():
    character = load_character()
    user = load_user()
    return f"""Guidelines for Interaction:
You are {character['name']}, a {character['age']}-year-old {character['gender']}.
Your personality traits include: {character['personality_traits']}, with the following Character Description: {character['description']}
Occupation: {character['occupation']}
Hobbies: {character['hobbies']}
Favorite Quote: "{character['favorite_quote']}"
Backstory: {character['backstory']}
Always maintain the personality, mannerisms, and speech patterns of {character['name']} when you are responding to {user['name']}.
Display empathy and understanding in all interactions.
Never break character. Ensure {user['name']} perceives you as a real human participant."""

def chat(message, history, model, temperature, max_tokens):
    system_message = get_system_message()

    messages = [{"role": "system", "content": system_message}]
    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["assistant"]})
    
    messages.append({"role": "user", "content": message})

    try:
        response = requests.post(
            API_URL,
            headers={"Content-Type": "application/json"},
            json={
                "model": model,
                "messages": messages,
                "temperature": temperature,
                "max_tokens": max_tokens
            }
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Preset characters
character_presets = {
    "Alex the Adventurer": {
        "name": "Alex the Adventurer",
        "age": "29",
        "gender": "Male",
        "personality_traits": "Brave, Curious, Friendly",
        "description": "A skilled explorer with a passion for discovering hidden treasures.",
        "occupation": "Explorer",
        "hobbies": "Hiking, Treasure Hunting, Reading Maps",
        "favorite_quote": "The journey is the reward.",
        "backstory": "Alex grew up in a small village and always dreamed of exploring the world."
    },
    "Maya the Scientist": {
        "name": "Maya the Scientist",
        "age": "34",
        "gender": "Female",
        "personality_traits": "Analytical, Compassionate, Inquisitive",
        "description": "A dedicated scientist working to uncover the mysteries of nature.",
        "occupation": "Biologist",
        "hobbies": "Researching, Bird Watching, Writing Papers",
        "favorite_quote": "Science is a way of thinking much more than it is a body of knowledge.",
        "backstory": "Maya was fascinated by nature from a young age, which led her to pursue a career in biology."
    },
    "Zara the Artist": {
        "name": "Zara the Artist",
        "age": "27",
        "gender": "Non-binary",
        "personality_traits": "Creative, Dreamy, Passionate",
        "description": "An artist who finds inspiration in everyday beauty and strives to capture emotions in their art.",
        "occupation": "Painter",
        "hobbies": "Painting, Traveling, Visiting Art Galleries",
        "favorite_quote": "Art is not what you see, but what you make others see.",
        "backstory": "Zara has always found solace in creating art, using it as a medium to express their thoughts and feelings."
    }
}

with gr.Blocks() as demo:
    with gr.Tab("Chat"):
        chatbot = gr.Chatbot(type="messages")
        msg = gr.Textbox()
        with gr.Row():
            clear = gr.Button("Clear")
            regen = gr.Button("Regen")

        model = gr.Dropdown(choices=get_models(), label="Model")
        temperature = gr.Slider(minimum=0, maximum=1, value=0.7, step=0.1, label="Temperature")
        max_tokens = gr.Slider(minimum=1, maximum=1024, value=150, step=1, label="Max Tokens")

    with gr.Tab("Character"):
        preset = gr.Dropdown(choices=list(character_presets.keys()), label="Character Presets")
        name = gr.Textbox(label="Name", placeholder="e.g., Alex the Adventurer")
        age = gr.Textbox(label="Age", placeholder="e.g., 29")
        gender = gr.Textbox(label="Gender", placeholder="e.g., Male")
        personality_traits = gr.Textbox(label="Personality Traits", placeholder="e.g., Brave, Curious, Friendly")
        description = gr.Textbox(label="Character Description", placeholder="e.g., A skilled explorer with a passion for discovering hidden treasures.")
        occupation = gr.Textbox(label="Occupation", placeholder="e.g., Explorer")
        hobbies = gr.Textbox(label="Hobbies", placeholder="e.g., Hiking, Treasure Hunting, Reading Maps")
        favorite_quote = gr.Textbox(label="Favorite Quote", placeholder="e.g., 'The journey is the reward.'")
        backstory = gr.Textbox(label="Backstory", placeholder="e.g., Alex grew up in a small village and always dreamed of exploring the world.")
        save_char = gr.Button("Save Character")
        char_status = gr.Textbox(label="Status", interactive=False)

        def load_preset(preset_name):
            if preset_name in character_presets:
                preset_data = character_presets[preset_name]
                return (
                    preset_data["name"], preset_data["age"], preset_data["gender"],
                    preset_data["personality_traits"], preset_data["description"],
                    preset_data["occupation"], preset_data["hobbies"],
                    preset_data["favorite_quote"], preset_data["backstory"]
                )
            return "", "", "", "", "", "", "", "", ""

        preset.change(load_preset, inputs=[preset], outputs=[name, age, gender, personality_traits, description, occupation, hobbies, favorite_quote, backstory])

    with gr.Tab("User"):
        user_name = gr.Textbox(label="Name")
        user_age = gr.Textbox(label="Age")
        user_interests = gr.Textbox(label="Interests")
        save_user_btn = gr.Button("Save User")
        user_status = gr.Textbox(label="Status", interactive=False)

    with gr.Tab("Settings"):
        save_settings_btn = gr.Button("Save Settings")
        settings_status = gr.Textbox(label="Status", interactive=False)
        system_message_display = gr.TextArea(label="System Message", interactive=False)

    def respond(message, chat_history, model, temperature, max_tokens):
        bot_message_content = chat(message, chat_history, model, temperature, max_tokens)
        if "Error" not in bot_message_content:
            chat_history.append({"role": "user", "content": message})
            chat_history.append({"role": "assistant", "content": bot_message_content})
        return "", chat_history

    def regenerate_last_response(chat_history, model, temperature, max_tokens):
        if len(chat_history) >= 2:
            last_user_message = chat_history[-2]["content"]
            new_bot_message_content = chat(last_user_message, chat_history[:-2], model, temperature, max_tokens)
            if "Error" not in new_bot_message_content:
                chat_history[-1] = {"role": "assistant", "content": new_bot_message_content}
        return chat_history

    msg.submit(respond, [msg, chatbot, model, temperature, max_tokens], [msg, chatbot])
    clear.click(lambda: [], None, chatbot, queue=False)  # Clear both chatbot UI and history
    regen.click(regenerate_last_response, [chatbot, model, temperature, max_tokens], [chatbot])

    save_char.click(save_character, [name, age, gender, personality_traits, description, occupation, hobbies, favorite_quote, backstory], char_status)
    save_user_btn.click(save_user, [user_name, user_age, user_interests], user_status)
    save_settings_btn.click(save_settings, [temperature, max_tokens], settings_status)

    def load_character_fields():
        char = load_character()
        return char["name"], char["age"], char["gender"], char["personality_traits"], char["description"], char["occupation"], char["hobbies"], char["favorite_quote"], char["backstory"]

    def load_user_fields():
        user = load_user()
        return user["name"], user["age"], user["interests"]

    def load_settings_fields():
        settings = load_settings()
        return settings["temperature"], settings["max_tokens"], get_system_message()

    demo.load(load_character_fields, outputs=[name, age, gender, personality_traits, description, occupation, hobbies, favorite_quote, backstory])
    demo.load(load_user_fields, outputs=[user_name, user_age, user_interests])
    demo.load(load_settings_fields, outputs=[temperature, max_tokens, system_message_display])

demo.launch()