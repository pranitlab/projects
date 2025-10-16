import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLiberary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "4bf228d62ec84a55820eb0c43c56ab05"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")  # corrected spelling
    
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLiberary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])


if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        print("Waiting for wake word 'Jarvis'...")

        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
                word = recognizer.recognize_google(audio)
                print("Heard:", word)

                if "jarvis" in word.lower():
                    speak("Ya")
                    
                    with sr.Microphone() as source:
                        print("Listening for command...")
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        print("Command:", command)
                        processCommand(command)

        except Exception as e:
            print("Error:", e)
