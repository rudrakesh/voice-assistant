import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import requests

def speak(str):
    a = pyttsx3.init()
    # id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    a.say(str)
    a.setProperty('rate',170)
    # a.setProperty('voice',id)
    # a.say(str)
    a.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language= 'en-in')
        print("User said : ",query)


    except Exception as e:
        print("Sorry... Please speak again")
        speak("Sorry. Please speak again")
        return 'None'
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        print("Good Morning Sir")
        speak("Good Morning Sir")
    elif 12 < hour < 17:
        print("Good Afternoon Sir")
        speak("Good Afternoon Sir")
    elif hour > 17:
        print("Good Evening Sir")
        speak("Good Evening Sir")

    speak("I am fudge. How may I assist you")



def wb(a):
    dirc = 'C://Users/91797/AppData/Local/Google/Chrome/Application/chrome.exe'
    webbrowser.get(dirc)
    webbrowser.open(f"www.{a}")

def search(a):
    dirc = 'C://Users/91797/AppData/Local/Google/Chrome/Application/chrome.exe'
    webbrowser.get(dirc)
    webbrowser.open("https://google.com/search?q=%s"%a)

def news():
    r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=26b539a95a2d48a88187c03883cb7697").json()
    article = r["articles"]
    results = []
    for ar in article:
        results.append(ar["title"])
        results.append(ar["description"])

    for i in range(len(results)):
        if (i == 0):
            speak("First headline is")
        if (i % 2 == 0) and (i != 0):
            print("\n")
            speak("Next Headline is")
        speak(results[i])



if __name__ == '__main__':
    wish()
    while(True):
        query = takecommand().lower()
        if "wikipedia" in query:
            print("Searching....")
            try:
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=1)
                speak("According to Wikipedia")
                speak(results)
            except Exception as e:
                speak("sorry but i couldn't understand.")
                speak("Please say it like virat kohli wikipedia to get better results.")

        elif "hello fudge" in query:
            speak("Hello sir")
            speak("How's the day running")

        elif 'open youtube' in query:
            a = 'youtube.com'
            wb(a)

        elif 'open google' in query:
            a = "google.com"
            wb(a)

        elif 'search on google' in query:
            query = query.replace("search on google","")

            search(query)

        elif 'play music' in query:
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            choice = random.choice(songs)
            os.startfile(os.path.join(music_dir,choice))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,The Time is {strTime}")

        elif "open visual code" in query:
            path = "C:\\Users\\91797\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)

        elif "open workbench" in query:
            path = "C:\\Program Files\\MySQL\\MySQL Workbench 8.0\\MySQLWorkbench.exe"
            os.startfile(path)

        elif "news" in query:
            news()


        elif "exit" in query:
            speak("Thankyou sir. Hope i helped you.")
            print("Goodbye...")
            speak("Goodbye")
            exit()
