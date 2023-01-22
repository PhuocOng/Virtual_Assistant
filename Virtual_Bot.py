import speech_recognition
import pyttsx3
from datetime import date, datetime
from gtts import gTTS
import os
import playsound
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re

#Common Variable for Both Vietnamese and English Code
you=""
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
robot_mouth = pyttsx3.init()

print("Which Languages do you want to use: Vietnamese - English")
option = input()



def listening_EngLish():
    global robot_ear
    global you
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=5)

    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio, show_all=False)
    except:
        you = ""
    print("You: "+ you)

def understanding_English():
    global robot_brain
    global you
    if you=="":
        robot_brain = "I can't hear you, try again"
    elif "hello" in you:
        robot_brain = "Hello Peter"
    elif "time" in you:
        now=datetime.now()
        robot_brain = now.strftime("%H hours %M minutes")
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    
    elif "president" in you:
        robot_brain = "Joe Biden"
    elif "software" in you:   #When we add a function in brain of English => we need to change robot_brain="_" at the end
        open_application_EN()
        robot_brain = ""
    elif "website" in you:
        open_website_EN()
        robot_brain= ""

    elif "stop" in you:
        robot_brain="I will stop the program"
    else:
        robot_brain = "I'm fine thank you and you"

    print(robot_brain)

def speaking_EngLish(robot_brain):
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()

def open_website_EN():
    speaking_EngLish("Which website do you want to access")
    print("We have: ")
    print("1. Facebook")
    print("2. New York Times")
    print("3. Github")
    print("4. StackOverFlow")
    print("5. Youtube")
    website = input("Website's name: ")

    if website == "1":
        webbrowser.open("https://www.facebook.com/")
        
    elif website=="2":
        webbrowser.open("https://www.nytimes.com/")
    elif website=="3":
        webbrowser.open("https://github.com/")
    elif website=="4":
        webbrowser.open("https://stackoverflow.com/")
    elif website=="5":
        webbrowser.open("https://www.youtube.com/")

    speaking_Vietnamese("Trang web bạn yêu cầu đã được mở.")
    
    
def open_application_EN():
    speaking_EngLish("Which software do you want to open")
    application = input("Software Name: ")
    if "Google" in application:
        speaking_EngLish("Open Google Chrome")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk')
    elif "Word" in application:
        speaking_EngLish("Open Microsoft Word")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
    elif "Excel" in application:
        speaking_EngLish("Open Microsoft Excel")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
    else:
        speaking_EngLish("Software wasn't dowloaded. Please dowload it")    
#____________________________________________________Divide Betwwen English and Vietnamese Code
def listening_Vietnamese():
    global robot_ear
    global you
    with speech_recognition.Microphone() as mic:
        print("Robot: Tôi Đang Nghe")
        audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=5)

    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio, language="vi-VN", show_all=False)
    except:
        you = ""
    print("Bạn: "+ you)

def understanding_Vietnamese():
    global robot_brain
    global you
    if you=="":
        robot_brain = "Tôi không thể nghe được, hãy nói lại"
    elif "chào" in you:
        robot_brain = "Xin chào Phước"
    elif "giờ" in you:
        now=datetime.now()
        robot_brain = now.strftime("%H giờ %M phút")
    elif "Hôm nay" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "tổng thống" in you:
        robot_brain = "Joe Biden"
    elif "dừng" in you:
        robot_brain="Tôi sẽ dừng chương trình"
    elif "phần mềm" in you:
        open_application_VN()
    elif "trang web" in you:
        open_website_VN()
    else:
        robot_brain = "Xin cảm ơn bạn"
        

    print(robot_brain)

def speaking_Vietnamese(text):
    print("Robot: " + text)
    tts = gTTS(text=text, lang='vi', slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3")
    os.remove("sound.mp3")

def open_application_VN():
    speaking_Vietnamese("Bạn muốn mở phần mềm nào")
    application = input("Tên Ứng Dụng: ")
    if "Google" in application:
        speaking_Vietnamese("Mở Google Chrome")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk')
    elif "Word" in application:
        speaking_Vietnamese("Mở Microsoft Word")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk')
    elif "Excel" in application:
        speaking_Vietnamese("Mở Microsoft Excel")
        os.startfile(
            'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk')
    else:
        speaking_Vietnamese("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")

def open_website_VN():
    speaking_Vietnamese("Bạn muốn mở trang web nào")
    print("Chúng tôi có: ")
    print("1. Facebook")
    print("2. New York Times")
    print("3. Github")
    print("4. StackOverFlow")
    print("5. Youtube")
    website = input("Tên Website: ")

    if website == "1":
        webbrowser.open("https://www.facebook.com/")
        
    elif website=="2":
        webbrowser.open("https://www.nytimes.com/")
    elif website=="3":
        webbrowser.open("https://github.com/")
    elif website=="4":
        webbrowser.open("https://stackoverflow.com/")
    elif website=="5":
        webbrowser.open("https://www.youtube.com/")

    speaking_Vietnamese("Trang web bạn yêu cầu đã được mở.")

def send_email_VN():
    speaking_Vietnamese('Bạn gửi email cho ai nhỉ')
    recipient = input("Email của người bạn muốn gửi")
    if 'yến' in recipient:
        speaking_Vietnamese('Nội dung bạn muốn gửi là gì')
        print("Nội Dung: ")
        content = input()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('phuocdn2008@gmail.com', 'onggiaphuoc20082004')
        mail.sendmail('phuocdn2008@gmail.com',
                      'phuocdn2008@gmail.com', content.encode('utf-8'))
        mail.close()
        speaking_Vietnamese('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speaking_Vietnamese('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')

#If Choose Option EngLish
if option=="English":
    while "stop" not in robot_brain :
        listening_EngLish()
        understanding_English()
        speaking_EngLish(robot_brain)
elif option=="Vietnamese":
    while "dừng" not in robot_brain:
        listening_Vietnamese()
        understanding_Vietnamese()
        speaking_Vietnamese(robot_brain)





#If Choose Option Vietnameses

    

