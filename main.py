import speech_recognition as sr
import webbrowser
import pyttsx3
from googleapiclient.discovery import build
import socialmedia
import music
from config import GOOGLE_API_KEY as API_KEY

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def search_google_knowledge_graph(query):
    service = build("kgsearch", "v1", developerKey=API_KEY)
    response = service.entities().search(query=query, limit=1).execute()
    if 'itemListElement' in response:
        result = response['itemListElement'][0]['result']
        name = result.get('name', 'No name available')
        description = result.get('description', 'No description available')
        detailed_description = result.get('detailedDescription', {}).get('articleBody', 'No detailed description available')
        print(query)
        print(f"{name}: {description}. {detailed_description[:1000]}")
        return f"{name}: {description}. {detailed_description[:1000]}"
    else:
        return "Sorry, I couldn't find any information on that topic."

def processCommand(c):
    if "open" in c.lower():
        sm = c.lower().split(" ")[1]
        link = socialmedia.socialmedias.get(sm, "")
        if link:
            webbrowser.open(link)
        else:
            speak("Social media not found")
    elif c.lower().startswith("play"):
        s = c.lower().split(" ")[1]
        lin = music.songs.get(s,"")
        if lin:
            webbrowser.open(lin)
        else:
            speak("music not found")
    else:
        response = search_google_knowledge_graph(command)
        speak(response)

if __name__ == "__main__":
    speak("Hey I am Jarvis, your voice assistant.")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source, timeout=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except Exception as e:
            print(f"Error: {e}")
