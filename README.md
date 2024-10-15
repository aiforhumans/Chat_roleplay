# Chat Application with Character Customization

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

This project is a chat application built using [Gradio](https://gradio.app/), allowing for interactive conversations with customizable character personalities. The app leverages a local language model hosted via LM Studio's API. Users can define character details, user information, and adjust settings to customize the interaction dynamics.

## Explanation

This chat application is designed to provide an interactive experience with AI-driven characters. Users can create and customize characters, personalize user details, and adjust chat settings for a more engaging conversation. The main features include real-time chatting with consistent character behavior, dynamic system messages, and integration with a local language model through LM Studio.

The project is built using Gradio, a powerful tool for building machine learning and data science demos, which makes it easy to interact with the local language model via a graphical interface. This allows users to engage in a roleplay-like conversation while maintaining character consistency, enhancing the interactive experience.

## Features

### 1. **Character Customization**
   - Choose a character preset or create your own with attributes like name, age, gender, personality traits, hobbies, and backstory.
   - Save your customized characters to maintain continuity across sessions.

### 2. **User Personalization**
   - Enter details such as user name, age, and interests to personalize the interaction.
   - Save user information for persistent interactions.

### 3. **Chat Settings**
   - Set chat-specific parameters such as temperature and max tokens.
   - Adjust model settings for a more controlled or creative response.

### 4. **Real-Time Chatting**
   - Chat with your character in a real-time interface using Gradio's `Chatbot`.
   - Custom buttons allow you to clear the conversation or regenerate the latest response.

### 5. **System Message for Character Consistency**
   - The app uses a system message to ensure that the character maintains consistent personality traits and speech patterns throughout the conversation.

## Installation

### Prerequisites
- Python 3.8 or higher
- LM Studio (running locally at `http://localhost:1234`)

### Create a Virtual Environment
1. **Create and Activate a Virtual Environment**
   It is recommended to use a virtual environment to manage dependencies.
   ```bash
   python -m venv venv
   ```

   On Windows, activate the virtual environment:
   ```bash
   venv\Scripts\activate
   ```
   On macOS/Linux, activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

2. **Clone the Repository**
   ```bash
   git clone https://github.com/aiforhumans/Chat_roleplay
   cd Chat_roleplay
   ```

3. **Install Dependencies**
   Make sure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the Gradio interface by running:
   ```bash
   python app.py
   ```

5. **Ensure LM Studio API is Running**
   - Make sure the LM Studio API server is running locally at `http://localhost:1234/v1/chat/completions` to connect to the app.

## How to Use

1. **Select a Character or Create One**
   - Use the "Character" tab to choose a preset character or create a new one with specific details.
   - Click "Save Character" to save the character.

2. **Enter User Information**
   - Use the "User" tab to input personal details to enhance the interaction.
   - Click "Save User" to store the information.

3. **Customize Settings**
   - Adjust the model and chat settings in the "Settings" tab, such as temperature and max tokens.
   - Save settings to maintain your preferences.

4. **Chat Away!**
   - Go to the "Chat" tab to start interacting with the character.
   - Use the text box to send messages and receive responses.
   - You can clear the chat or regenerate the last response for better continuity.

## Character File Format

Characters are stored in a JSON-like format with the following fields:

```json
{
  "name": "<Character Name>",
  "age": "<Character Age>",
  "gender": "<Character Gender>",
  "personality_traits": "<Personality Traits>",
  "description": "<Character Description>",
  "occupation": "<Occupation>",
  "hobbies": "<Hobbies>",
  "favorite_quote": "<Favorite Quote>",
  "backstory": "<Backstory>"
}
```

- **name**: The name of the character (e.g., "Alex the Adventurer").
- **age**: The character's age (e.g., "29").
- **gender**: The character's gender (e.g., "Male").
- **personality_traits**: A comma-separated list of personality traits (e.g., "Brave, Curious, Friendly").
- **description**: A brief description of the character (e.g., "A skilled explorer with a passion for discovering hidden treasures.").
- **occupation**: The character's occupation (e.g., "Explorer").
- **hobbies**: A comma-separated list of hobbies (e.g., "Hiking, Treasure Hunting, Reading Maps").
- **favorite_quote**: A quote that represents the character (e.g., "The journey is the reward.").
- **backstory**: A short backstory of the character (e.g., "Alex grew up in a small village and always dreamed of exploring the world.").

## Preset Characters

- **Alex the Adventurer**: A brave and curious explorer with a passion for discovering hidden treasures.
- **Maya the Scientist**: A compassionate biologist working to uncover the mysteries of nature.
- **Zara the Artist**: A creative painter who strives to capture emotions in their art.

## API Integration

The chat functionality is integrated with a local language model hosted via LM Studio. Requests are sent to the endpoint `http://localhost:1234/v1/chat/completions`, which allows real-time interactions.

## Project Structure

```bash
Chat_roleplay/
├── app.py             # Main application file
├── model_info.py      # Fetches available models from the API
├── char.py            # Handles loading and saving character information
├── user.py            # Handles user data
├── settings.py        # Manages chat settings
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
└── assets/            # Images and other assets for README
```

- `app.py`: Main application file.
- `model_info.py`: Fetches available models from the API.
- `char.py`: Handles loading and saving character information.
- `user.py`: Handles user data.
- `settings.py`: Manages chat settings.

## Requirements
- **Python 3.8+**: Required to run the scripts.
- **Gradio**: Used to create the graphical interface for interacting with the model.
- **Requests**: Library to handle HTTP requests to the LM Studio API.
- **LM Studio**: A local language model backend running on `localhost:1234` to process chat completions.

## Notes
- Ensure LM Studio API is up and running before launching the application.
- Characters and settings are cached for quick access and to minimize repeated file access.

## Contributing

Contributions are welcome! If you have suggestions or would like to add new features, please create a pull request. Make sure your changes are well documented and tested.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Gradio](https://gradio.app/) for providing the interactive UI.
- [LM Studio](https://lmstudio.com) for the local language model API support.

Feel free to contribute or raise issues if you find bugs or have suggestions for new features.
