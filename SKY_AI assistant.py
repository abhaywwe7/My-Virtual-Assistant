'''
Author: Abhay Partap Singh
Dated: 2 jan 2002
'''
import pyttsx3
import datetime
import speech_recognition as spr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib
import json,requests
import subprocess

engine=pyttsx3.init('sapi5') #Speechapi by microsoft
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id) #0 for david and 1 for zira

def speak(audio):
    engine.say(audio)
    engine.runAndWait() #callback your engine operation

def wish_me():
    hour=int(datetime.datetime.now().hour) #taking hour
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    AI_name=("Sky 2.0")
    speak(f"I am {AI_name}. Please tell me how may i help you")
#microphone input
def take_command():
    rec= spr.Recognizer()
    with spr.Microphone() as source:
        print("Listening...")
        rec.pause_threshold=1 #gap of seconds for speaking
        rec.energy_threshold= 350
        audio=rec.listen(source)
    try:
        print("Recognizing your audio...")
        query= rec.recognize_google(audio,language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def usrname():
    speak("What should i call you")
    my_name=take_command()
    speak("Welcome Mister")
    speak(my_name)
    print("Welcome Mr.", my_name)
    speak("How may i help you")

def SendMail(to,content):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    sender_email = "abhaywwe6@gmail.com"
    password = input("enter your password: ")
    s.ehlo()
    s.starttls()
    s.login(sender_email,password)
    s.sendmail(sender_email, to, content)
    s.close()

if __name__ == '__main__':
    clean= lambda: os.system('cls')
    #clear any command before execution of this file
    clean()
    wish_me()
    usrname()
    if True: #Use while to use multiple statements, if if used here for operating only 1 query
        query = take_command().lower() #converting to lower string  for perfect matching
        #logic for doing various task's
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("Here you go to youtube\n")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com/")

        elif 'open hackerrank' in query:
            speak("Here you go to Hackerrank\n")
            webbrowser.open("https://www.hackerrank.com/")

        elif 'play music' in query:
            song_dir='E:\\VIDEOS\\SONGS' #escape sequence
            songs=os.listdir(song_dir) #make list of all song
            # print(songs)
            os.startfile(os.path.join(song_dir,random.choice(songs)))

        elif 'the time' in query:
            str_time=datetime.datetime.now().strftime("%H:%M:%S") #time format
            speak(f"The time is {str_time}")
            print(str_time)

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Abhay")

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")

        elif 'exit' in query or 'close' in query:
            speak("It was lovely to talk to you")
            exit()

        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Abhay Partap Singh")

        elif 'joke' in query:
            joking=speak(pyjokes.get_joke())

        elif 'who i am' in query:
            speak("If you are talking then definately you are human")

        elif 'search' in query or 'play' in query:
            query=query.replace("search","")
            query=query.replace("play","")
            webbrowser.open(query)

        elif 'who are you' in query:
            speak("I am your assistant")

        elif 'i love you' in query:
            speak("I am very glad to hear that")

        elif 'send mail' in query:
            try:
                speak("What should i say!")
                content= take_command()
                to="abhaywwe6@gmail.com"
                SendMail(to,content)
                speak("Email successfully sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email")

        elif 'news' in query:
            url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=945b50bc62b34fe9be39a1fd9e6ff506"
            news1 = requests.get(url).text
            news1 = json.loads(news1)
            for i in range(0, 11):
                speak(news1['articles'][i]['title'])
                print(news1['articles'][i]['title'])

        elif 'sleep' in query:
            speak("Sleeping")
            subprocess.call("shutdown / h")

        elif 'sky' in query:
            speak("How may i help you")

        elif 'will you be my gf' in query:
            speak("I am not sure about that, may be you should give me some time to think")

        elif 'where is' in query:
            query=query.replace("where is","")
            location=  query
            speak("You asked to locate")
            speak(location)
            webbrowser.open("https://www.google.co.in/maps/place/" +location+"")