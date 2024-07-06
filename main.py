import speech_recognition as sr
import webbrowser
import pyttsx3
import socialmedia
import music
import wikipediaapi

engine = pyttsx3.init()

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent='Jarvis/1.0'
)

def speak(text):
    engine.say(text)
    engine.runAndWait()


def search_wikipedia(query):
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary[:300]  
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
        response = search_wikipedia(command)
        speak(response)
    

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source,timeout=2)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes how can i help you?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")
    

