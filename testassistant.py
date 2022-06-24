from __future__ import print_function
import warnings
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from AssistantUI import Ui_MainWindow
import pyttsx3
import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import datetime
import calendar
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import subprocess
import pyjokes
import smtplib
import requests
import json
import time
from twilio.rest import Client
import wolframalpha
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium import webdriver
from time import sleep
import sys



warnings.filterwarnings("ignore")

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)




def talk(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        talk("Good morning")
    elif hour>=12 and hour<18:
        talk("Good Afternoon")
    else:
        talk("Good night")



def today_date(slef):
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."


def say_hello(text):
    greet = ["hi", "hey", "hola", "greetings", "wassup", "hello"]

    response = ["howdy", "whats good", "hello", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response) + "."

    return ""


def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
            return list_wiki[i + 2] + " " + list_wiki[i + 3]


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()

    server.login("royalcsgo18@gmail.com", "agnihotri11400")
    server.sendmail("email", to, content)
    server.close()

def pizza(self):
    driver = webdriver.Chrome(
        r"C:\Users\Anmol\Desktop\chromedriver.exe"
    )
    driver.maximize_window()

    talk("Opening Dominos")
    driver.get('https://www.dominos.co.in/')
    sleep(2)

    talk("Getting ready to order")
    driver.find_element_by_link_text('ORDER ONLINE NOW').click()
    sleep(2)

    talk("Finding your location")
    driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
    sleep(2)

    location = "Shah and Anchor"

    talk("Entering your location")
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
        location)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()
    sleep(2)

    #try:
    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()
    sleep(2)
    #except:
        #talk("Your location could not be found. Please try again later.")
        #exit()

    talk("Logging in")

    phone_num = "7303274392"

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
        phone_num)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
    sleep(2)

    talk("What is your O T P? ")
    sleep(2)

    otp_log = rec_audio()

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
        otp_log)
    sleep(2)

    driver.find_element_by_xpath(
        '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
    sleep(5)

    talk("Do you want me to order from your favorites?")
    query_fav = rec_audio()

    if "yes" in query_fav:
        try:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()
            sleep(1)
        except:
            talk("The entered OTP is incorrect.")
            exit()

        talk("Adding your favorites to cart")

        talk("Do you want me to add extra cheese to your pizza?")
        ex_cheese = rec_audio()
        if "yes" in ex_cheese:
            talk("Extra cheese added")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()
        elif "no" in ex_cheese:
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
        else:
            talk("I dont know that")
            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

        driver.find_element_by_xpath(
            '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()
        sleep(1)

        talk("Would you like to increase the qty?")
        qty = rec_audio()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            talk("Would you like to increase the quantity of pizza?")
            wh_qty = rec_audio()
            if "yes" in wh_qty:
                talk("How many more pizzas would you like to add? ")
                try:
                    qty_pizza = rec_audio()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        talk(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

            talk("Would you like to increase the quantity of pepsi?")
            pep_qty = rec_audio()
            if "yes" in pep_qty:
                talk("How many more pepsis would you like to add? ")
                try:
                    qty_pepsi = rec_audio()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        talk(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element_by_xpath(
                                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                except:
                    talk("I dont know that.")
            else:
                pass

        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        talk(tell_num)
        check_order = rec_audio()
        if "yes" in check_order:
            talk("Checking out")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
            sleep(1)
            total = driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span')
            total_price = f'total price is {total.text}'
            talk(total_price)
            sleep(1)
        else:
            exit()

        talk("Placing your order")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button').click()
        sleep(2)
        try:
            talk("Saving your location")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
            sleep(2)
        except:
            talk("The store is currently offline.")
            exit()

        talk("Do you want to confirm your order?")
        confirm = rec_audio()
        if "yes" in confirm:
            talk("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
            sleep(2)
            talk("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day!")
        else:
            exit()

    else:
        exit()

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()

    def rec_audio(slef):
        recog = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = recog.listen(source)
        try:
            print("Recog......")
            text = recog.recognize_google(audio, language='en-in')
            print(">> ", text)
        except Exception:
            talk("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text

    def response(text,self):
        print(text)

        tts = gTTS(text=text, lang="en")

        audio = "Audio.mp3"
        tts.save(audio)

        playsound.playsound(audio)

        os.remove(audio)

    def call(text,slef):
        action_call = "assistant"

        text = text.lower()

        if action_call in text:
            return True

        return False


    def TaskExecution(self):
        while True:
            wish()
            self.text = self.rec_audio()

            if "date" in self.text or "day" in self.text or "month" in self.text:
                get_today = today_date()
                speak = speak + " " + get_today

            elif "time" in self.text:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

            elif "wikipedia" in self.text or "Wikipedia" in self.text:
                if "who is" in self.text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=2)
                    speak = speak + " " + wiki

            elif "who are you" in self.text or "define yourself" in self.text:
                speak = speak + """Hello, I am  Your Assistant. I am here to make your life easier.  
                You can command me to perform various tasks such as solving mathematical questions or opening 
                applications etcetera."""

            elif "your name" in self.text:
                speak = speak + "My name is Assistant."

            elif "who am I" in self.text:
                speak = speak + "You must probably be a human."

            elif "why do you exist" in self.text or "why did you come" in self.text:
                speak = speak + "It is a secret."

            elif "how are you" in self.text:
                speak = speak + "I am fine, Thank you!"
                speak = speak + "\nHow are you?"

            elif "fine" in self.text or "good" in self.text:
                speak = speak + "It's good to know that you are fine"

            elif "open" in self.text.lower():

                if "chrome" in self.text.lower():
                    #speak = speak + "Opening Google Chrome"
                    talk("Opening google chrome")
                    os.startfile(
                        r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                    )

                elif "word" in self.text.lower():
                    speak = speak + "Opening Microsoft Word"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
                    )

                elif "excel" in self.text.lower():
                    speak = speak + "Opening Microsoft Excel"
                    os.startfile(
                        r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE"
                    )

                elif "vs code" in self.text.lower():
                    speak = speak + "Opening Visual Studio Code"
                    os.startfile(
                        r"C:\Users\Anmol\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                    )

                elif "youtube" in self.text.lower():
                    speak = speak + "Opening Youtube\n"
                    webbrowser.open("https://youtube.com/")

                elif "google" in self.text.lower():
                    speak = speak + "Opening Google\n"
                    webbrowser.open("https://google.com/")

                elif "stack overflow" in self.text.lower():
                    speak = speak + "Opening Stack OverFlow"
                    webbrowser.open("https://stackoverflow.com/")

            elif "youtube" in self.text.lower():
                ind = text.lower().split().index("youtube")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "http://www.youtube.com/results?search_query=" +
                    "+".join(search)
                )
                speak = speak + "Opening " + str(search) + " on youtube"

            elif "search" in self.text.lower():
                ind = text.lower().split().index("search")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "google" in self.text.lower():
                ind = text.lower().split().index("google")
                search = text.split()[ind + 1:]
                webbrowser.open(
                    "https://www.google.com/search?q=" + "+".join(search))
                speak = speak + "Searching " + str(search) + " on google"

            elif "change background" in self.text or "change wallpaper" in self.text:
                img = r"C:/Users/Anmol/Pictures/wallpaper"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                speak = speak + "Background changed successfully"

            elif "play music" in self.text or "play song" in self.text:
                talk("Here you go with music")
                music_dir = r"C:/Users/Anmol/Pictures/Music"
                songs = os.listdir(music_dir)
                d = random.choice(songs)
                random = os.path.join(music_dir, d)
                playsound.playsound(random)

            elif "empty recycle bin" in self.text:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak = speak + "Recycle Bin Emptied"

            elif "note" in self.text or "remember this" in self.text:
                talk("What would you like me to write down?")
                note_text = rec_audio()
                note(note_text)
                speak = speak + "I have made a note of that."

            elif "joke" in self.text:
                speak = speak + pyjokes.get_joke()

            elif "where is" in self.text:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            elif "email to Anmol" in self.text or "gmail to Anmol" in self.text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    to = "anmolagnihotri11@gmail.com"
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    talk("I am not able to send this email")

            elif "mail" in self.text or "email" in self.text or "gmail" in self.text:
                try:
                    talk("What should I say?")
                    content = rec_audio()
                    talk("whom should i send")
                    to = input("Enter To Address: ")
                    send_email(to, content)
                    speak = speak + "Email has been sent !"
                except Exception as e:
                    print(e)
                    speak = speak + "I am not able to send this email"

            elif "weather" in self.text:
                key="23e5952755212a7f628bed61bffe6c7a"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = text.split().index("in")
                location = text.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weather_response = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                        humidity) + " and The weather description is " + str(desc)
                    speak = speak + weather_response
                else:
                    speak = speak + "City Not Found"

            elif "news" in self.text:
                url = ('http://newsapi.org/v2/top-headlines?'
                       'country=in&'
                       'apiKey=51874a981c5247db98303c069bdb765f')

                try:
                    response = requests.get(url)
                except:
                    talk("Please check your connection")

                news = json.loads(response.text)

                for new in news["articles"]:
                    print(str(new["title"]), "\n")
                    talk(str(new["title"]))
                    engine.runAndWait()

                    print(str(new["description"]), "\n")
                    talk(str(new["description"]))
                    engine.runAndWait()
                    time.sleep(2)

            elif "send message" in self.text or 'send a message' in self.text:
                account_sid = "AC8371c21284ab44afda966b6c8110f119"
                auth_token = "dfca8f822c30b5008369d7b766e7d6fd"
                client = Client(account_sid, auth_token)

                talk("What should i send")
                message = client.messages.create(
                    body=rec_audio(), from_="+17605732317", to="+917303274392"
                )

                print(message.sid)
                speak = speak + "Message sent successfully"

            elif "calculate" in self.text:
                app_id = "G2842E-RGP9A57LW6"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("calculate")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + "The answer is " + answer

            elif "what is" in self.text or "who is" in self.text:
                app_id = "G2842E-RGP9A57LW6"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text
                speak = speak + answer

            elif "don't listen" in self.text or "stop listening" in self.text or "do not listen" in self.text:
                talk("for how many seconds do you want me to sleep")
                a = int(rec_audio())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"

            elif "exit" in self.text or "quit" in self.text:
                exit()

            elif "order a pizza" in self.text or "pizza" in self.text:
                pizza()

                response(speak)



startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("A:/PythonMiniProject/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("A:/PythonMiniProject/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()


    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        lable_time = current_time.toString('hh:mm:ss')
        lable_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(lable_date)
        self.ui.textBrowser_2.setText(lable_time)

app = QApplication(sys.argv)
VoiceAssistant = Main()
VoiceAssistant.show()
exit(app.exec_())