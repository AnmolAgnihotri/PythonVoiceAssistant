# Author- Anmol
import warnings
import pyttsx3
import speech_recognition as sr
import datetime
import os
import random
import winshell
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyjokes
import requests
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import calendar
from selenium import webdriver
import time
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from AssistantUI import Ui_MainWindow

warnings.filterwarnings("ignore")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[len(voices) - 1].id)


# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am jarvis sir. please tell me how may i help you")



# to send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("royalcsgo18@gmail.com", "agnihotri11400")
    server.sendmail("royalcsgo18@gmail.com", to, content)
    server.close()


def today_date():
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


# for news updates
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=51874a981c5247db98303c069bdb765f'

    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        # print(f"today's {day[i]} news is: ", head[i])
        speak(f"today's {day[i]} news is: {head[i]}")


def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        self.TaskExecution()

    
    def pizza(self):

        driver = webdriver.Chrome(
            r"C:\Users\Anmol\Desktop\chromedriver.exe"
        )
        driver.maximize_window()

        speak("Opening Dominos")
        driver.get('https://www.dominos.co.in/')
        time.sleep(2)

        speak("Getting ready to order")
        driver.find_element_by_link_text('ORDER ONLINE NOW').click()
        time.sleep(2)

        speak("Finding your location")
        driver.find_element_by_class_name('srch-cnt-srch-inpt').click()
        time.sleep(2)

        location = "Shah and Anchor"

        speak("Entering your location")
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div/div[1]/input').send_keys(
            location)
        speak(2)

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/div/ul/li[1]').click()
        time.sleep(2)

        # try:
        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[1]/div[2]').click()
        time.sleep(2)
        # except:
        # talk("Your location could not be found. Please try again later.")
        # exit()

        speak("Logging in")

        phone_num = "7303274392"

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input').send_keys(
            phone_num)
        time.sleep(2)

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input').click()
        time.sleep(2)

        speak("What is your O T P? ")
        time.sleep(2)

        otp_log = self.takecommand()

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input').send_keys(
            otp_log)
        time.sleep(2)

        driver.find_element_by_xpath(
            '//*[@id="__next"]/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span').click()
        time.sleep(5)

        speak("Do you want me to order from your favorites?")
        query_fav = self.takecommand()

        if "yes" in query_fav:
            try:
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[6]/div/div/div[2]/div[3]/div/button/span').click()
                time.sleep(1)
            except:
                speak("The entered OTP is incorrect.")
                exit()

            speak("Adding your favorites to cart")

            speak("Do you want me to add extra cheese to your pizza?")
            ex_cheese = self.takecommand()
            if "yes" in ex_cheese:
                speak("Extra cheese added")
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[2]/button').click()
            elif "no" in ex_cheese:
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()
            else:
                speak("I dont know that")
                driver.find_element_by_xpath(
                    '//*[@id="mn-lft"]/div[6]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span').click()

            driver.find_element_by_xpath(
                '//*[@id="mn-lft"]/div[16]/div/div[1]/div/div/div[2]/div[2]/div/button').click()
            time.sleep(1)

            speak("Would you like to increase the qty?")
            qty = self.takecommand()
            qty_pizza = 0
            qty_pepsi = 0
            if "yes" in qty:
                speak("Would you like to increase the quantity of pizza?")
                wh_qty = self.takecommand()
                if "yes" in wh_qty:
                    speak("How many more pizzas would you like to add? ")
                    try:
                        qty_pizza = self.takecommand()
                        qty_pizza = int(qty_pizza)
                        if qty_pizza > 0:
                            talk_piz = f"Adding {qty_pizza} more pizzas"
                            speak(talk_piz)
                            for i in range(qty_pizza):
                                driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div/div/div[2]').click()
                    except:
                        speak("I dont know that.")
                else:
                    pass

                speak("Would you like to increase the quantity of pepsi?")
                pep_qty = self.takecommand()
                if "yes" in pep_qty:
                    speak("How many more pepsis would you like to add? ")
                    try:
                        qty_pepsi = self.takecommand()
                        qty_pepsi = int(qty_pepsi)
                        if qty_pepsi > 0:
                            talk_pep = f"Adding {qty_pepsi} more pepsis"
                            speak(talk_pep)
                            for i in range(qty_pepsi):
                                driver.find_element_by_xpath(
                                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]').click()
                    except:
                        speak("I dont know that.")
                else:
                    pass

            elif "no" in qty:
                pass

            total_pizza = qty_pizza + 1
            total_pepsi = qty_pepsi + 1
            tell_num = f"This is your list of order. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
            speak(tell_num)
            check_order = self.takecommand()
            if "yes" in check_order:
                speak("Checking out")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button').click()
                time.sleep(1)
                total = driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span')
                total_price = f'total price is {total.text}'
                speak(total_price)
                time.sleep(1)
            else:
                exit()

            speak("Placing your order")
            driver.find_element_by_xpath(
                '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button').click()
            time.sleep(2)
            try:
                speak("Saving your location")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input').click()
                time.sleep(2)
            except:
                speak("The store is currently offline.")
                exit()

            speak("Do you want to confirm your order?")
            confirm = self.takecommand()
            if "yes" in confirm:
                speak("Placing your order")
                driver.find_element_by_xpath(
                    '//*[@id="__next"]/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button').click()
                time.sleep(2)
                speak("Your order is placed successfully. Wait for Dominos to deliver your order. Enjoy your day!")
            else:
                exit()

        else:
            exit()


    def searchindrive(self):
        driver = webdriver.Chrome(
            r"C:\Users\Anmol\Desktop\chromedriver.exe"
        )
        driver.maximize_window()
        email_id = "deltawingdevlopers@gmail.com"
        gmail_password = "agnihotri1"

        speak("Opening Google Drive")
        driver.get('https://drive.google.com/drive/my-drive')
        driver.implicitly_wait(60)
        speak("Logging in")
        driver.find_element_by_id('identifierId').send_keys(email_id)
        driver.find_element_by_id('identifierNext').click()
        driver.implicitly_wait(60)
        driver.find_element_by_name('password').send_keys(gmail_password)
        driver.find_element_by_id('passwordNext').click()
        time.sleep(7)
        speak("What you want to search?")
        time.sleep(3)
        search_drive = self.takecommand()
        driver.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]').send_keys(search_drive)
        time.sleep(5)
        driver.find_element_by_id('aso_search_form_anchor').click()
        speak("Here is what your looking for")


    def searchinmail(self):
        driver = webdriver.Chrome(
            r"C:\Users\Anmol\Desktop\chromedriver.exe"
        )
        driver.maximize_window()
        email_id = "deltawingdevlopers@gmail.com"
        gmail_password = "agnihotri1"

        speak("Opening Gmail")
        driver.get('http://mail.google.com/')
        driver.implicitly_wait(60)
        speak("Logging in")
        driver.find_element_by_id('identifierId').send_keys(email_id)
        driver.find_element_by_id('identifierNext').click()
        driver.implicitly_wait(60)
        driver.find_element_by_name('password').send_keys(gmail_password)
        driver.find_element_by_id('passwordNext').click()
        time.sleep(7)
        speak("What you want to search?")
        time.sleep(3)
        search_drive = self.takecommand()
        driver.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]').send_keys(search_drive)
        time.sleep(5)
        driver.find_element_by_id('aso_search_form_anchor').click()
        speak("Here is what your looking for")


    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            global query 
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return "none"
        return query

    def TaskExecution(self):
        wish()
        while True:
            global speak
            self.query = self.takecommand().lower()

            # logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif "date" in self.query or "day" in self.query or "month" in self.query:
                get_today = today_date()
                speak(get_today)

            elif 'hi' in self.query or 'hello' in self.query:
                speak('Hello sir, how may I help you?')

            elif "open command prompt" in self.query:
                os.system("start cmd")


            elif "play music" in self.query:
                music_dir = r"C:/Users/Anmol/Pictures/Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))



            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stack overflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")


            elif "song on youtube" in self.query:
                kit.playonyt("see you again")

            elif 'timer' in self.query or 'stopwatch' in self.query:
                speak("For how many minutes?")
                timing = self.takecommand()
                timing = timing.replace('minutes', '')
                timing = timing.replace('minute', '')
                timing = timing.replace('for', '')
                timing = float(timing)
                timing = timing * 60
                speak(f'I will remind you in {timing} seconds')

                time.sleep(timing)
                speak('Your time has been finished sir')

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("thanks for using me sir, have a good day.")
                break;

            # to close any application
            elif "close notepad" in self.query:
                speak("okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            # to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")


            elif "tell me news" in self.query:
                speak("please wait sir, fetching the latest news")
                news()

            elif "empty recycle bin" in self.query:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )
                speak("Recycle Bin Emptied")

            elif "where is" in self.query:
                ind = self.query.lower().split().index("is")
                location = self.query.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak("Here is waht your looking for")
                webbrowser.open(url)

            elif "weather" in self.query.lower():
                key = "23e5952755212a7f628bed61bffe6c7a"
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = self.query.split().index("in")
                location = self.query.split()[ind + 1:]
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
                    speak(weather_response)
                else:
                    speak = speak + "City Not Found"

            elif "note" in self.query or "remember this" in self.query:
                speak("What would you like me to write down?")
                note_text = self.takecommand()
                note(note_text)
                speak("I have made a note of that.")

            elif "order a pizza" in self.query or "pizza" in self.query:
                self.pizza()

            elif "where i am" in self.query or "where we are" in self.query:
                speak("Wait sir let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd + '.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    country = geo_data['country']
                    speak(f"Sir I am not sure, but I think we are in {city} city in  {country} country")
                except Exception as e:
                    speak("Sorry sir, due to network issue i cannot find your location right now")
                    pass




            elif "send email" in self.query:

                speak("sir what should i say")
                query = self.takecommand().lower()
                if "send a file" in query:
                    email = "royalcsgo18@gmail.com"  # Your email
                    password = "agnihotri11400"  # Your email account password
                    send_to_email = "anmolagnihotri11@gmail.com"  # Whom you are sending the message to
                    speak("okay sir, what is the subject for this email")
                    query = self.takecommand().lower()
                    subject = query  # The Subject in the email
                    speak("and sir, what is the message for this email")
                    query2 = self.takecommand().lower()
                    message = query2  # The message in the email
                    speak("sir please enter the correct path of the file into the shell")
                    file_location = input("please enter the path here")  # The File attachment in the email

                    speak("please wait,i am sending email now")

                    msg = MIMEMultipart()
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

                    msg.attach(MIMEText(message, 'plain'))

                    # Setup the attachment
                    filename = os.path.basename(file_location)
                    attachment = open(file_location, "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

                    # Attach the attachment to the MIMEMultipart object
                    msg.attach(part)

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login("royalcsgo18@gmail.com", "agnihotri11400")
                    text = msg.as_string()
                    server.sendmail(email, send_to_email, text)
                    server.quit()
                    speak("email has been sent to anmol")

                else:
                    email = "royalcsgo18@gmail.com"  # Your email
                    password = "agnihotri11400"  # Your email account password
                    send_to_email = "anmolagnihotri11@gmail.com"  # Whom you are sending the message to
                    message = query  # The message in the email

                    server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
                    server.starttls()  # Use TLS
                    server.login("royalcsgo18@gmail.com", "agnihotri11400")  # Login to the email server
                    server.sendmail(email, send_to_email, message)  # Send the email
                    server.quit()  # Logout of the email server
                    speak("email has been sent to anmol")




            elif "search in google drive" in self.query or "search in drive" in self.query:
                self.searchindrive()
            elif "search in gmail" in self.query or "search email" in self.query:
                self.searchinmail()


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
jarvis = Main()
jarvis.show()
exit(app.exec_())
