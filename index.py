import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')
# print(voice[1].id)
engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():

    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour <= 12:
        speak("Goodmorning!")

    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")

    speak("I am Jarvis, How may i help you")


def takeCommand():
    # takes microphone input and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source)

    try:
        print("Recorgnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")

    except Exception as e:
        print(e)
        print("Parden me, Say that again please")
        return "None"
    return query


def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("terminuskraken18@gmail.com", "#gamingbeastterminus#@18")
    server.sendemail('terminuskraken18@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
   # greeting()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching in Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\risal\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\risal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'email to Ankit' in query:
            try:
                content = takeCommand()
                to = 'ankritrisal2002@gmail.com'
                sendEmail(to, content)
                speak("Email sent")

            except Exception as e:
                print(e)
                speak('Got a problem sir, Please retry the process')
