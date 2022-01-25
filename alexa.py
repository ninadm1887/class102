from urllib.parse import quote, uses_query
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12:
        speak("Good morning sir!")
    elif hour >=12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    
    speak("I am your virtual assistant, you can call me Zira.")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
if __name__ == "__main__":
    
    wishMe()
    while True:
        webbrowser.register('chrome', None)
    #if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching in wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=10)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'your name' in query:
            speak('My name is Zira and I an designed by Khushaal')
        
        elif 'you live' in query:
            speak("I was built in India, Andhra pradesh, visakhapatnam, by a best developer called Khushaal")

        elif 'do you do' in query or 'your work' in query:
            speak('I control this device and I do 24 by 7 discussion with my friends.')
        
        elif 'hi' in query or 'hello' in query:
            speak("Hello")

        elif 'you are smart' in query or 'you are intelligent' in query or 'you are good' in query:
            speak('I know, Thank you')

        elif 'thank you' in query:
            speak("Your welcome")

        elif 'evening' in query:
            speak('Good evening sir!!')

        elif 'afternoon' in query:
            speak('Good afternoon sir!!')
        
        elif 'morning' in query:
            speak('Good Morning sir!!')

        elif 'ok' in query:
            speak('Ok...')

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open code.org' in query:
            webbrowser.open("code.org")

        elif 'open whatsappweb' in query or 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'the time' in query or 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'open code editor' in query or 'open vs code' in query or 'open vs editor' in query or 'open vs' in query:
            code_path = "C:\\Users\hello\\AppData\\Local\\Programs\\Microsoft VS Code\Code.exe"
            os.startfile(code_path)
            print("App opened successfully")

        elif 'open zoom.us' in query or 'open zoom' in query:
            zoom_path = "C:\\Users\\hello\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoom_path)
            print("App opened successfully")

        elif 'open chrome' in query or 'open google chrome' in query or 'open google' in query:
            google_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(google_path)
            print("App opened successfully")

        else:
            speak("Say that again please...")
