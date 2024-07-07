# Jarvis Voice Assistant

Jarvis is a voice-activated assistant that can perform various tasks such as searching the web, opening social media, playing music, and performing calculations. It uses speech recognition and text-to-speech to interact with the user.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Features

- **Voice Recognition**: Uses Google Speech Recognition to recognize voice commands.
- **Text-to-Speech**: Uses `pyttsx3` to provide spoken responses.
- **Web Search**: Searches the Google Knowledge Graph for information.
- **Social Media Access**: Opens specified social media platforms.
- **Music Playback**: Plays specified songs from a predefined list.
- **Calculations**: Performs simple mathematical calculations.

## Requirements

- Python 3.6+
- `speech_recognition`
- `webbrowser`
- `pyttsx3`
- `google-api-python-client`
- `socialmedia` (custom module)
- `music` (custom module)
- `config` (custom module containing `GOOGLE_API_KEY`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/jarvis-voice-assistant.git
    ```
2. Navigate to the project directory:
    ```bash
    cd jarvis-voice-assistant
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

1. Obtain a Google API key and add it to a `config.py` file in the following format:
    ```python
    GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY'
    ```

2. Create `socialmedia.py` and `music.py` modules with your social media links and music links respectively. For example:

    `socialmedia.py`:
    ```python
    socialmedias = {
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        // Add more social media links as needed
    }
    ```

    `music.py`:
    ```python
    songs = {
        "song1": "https://link-to-song1",
        "song2": "https://link-to-song2",
        // Add more songs as needed
    }
    ```

## Usage

1. Run the script:
    ```bash
    python jarvis.py
    ```

2. Speak the command "Jarvis" to activate the assistant.
3. Give commands such as:
    - "Open Facebook"
    - "Play song1"
    - "Search for Python programming"
    - "Calculate 2 + 2"

## Commands

Jarvis supports the following types of commands:

- **Open Social Media**: Opens a social media platform in your web browser.
    - Example: "Open Facebook"
- **Play Music**: Plays a song from a predefined list in your web browser.
    - Example: "Play song1"
- **Search the Web**: Searches for information on a given topic using Google Knowledge Graph.
    - Example: "Search for Python programming"
- **Perform Calculations**: Performs basic mathematical calculations.
    - Example: "Calculate 2 + 2"

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request.


## Acknowledgements

- [Google Speech Recognition](https://pypi.org/project/SpeechRecognition/)
- [Pyttsx3](https://pypi.org/project/pyttsx3/)
- [Google API Client](https://github.com/googleapis/google-api-python-client)

## Author
Ankit Kumar Dam

Github Profile Link: https://github.com/myself-ankit18

