import speech_recognition
import pyttsx3
from datetime import date, datetime

you=""
robot_ear = speech_recognition.Recognizer()
robot_brain = ""
robot_mouth = pyttsx3.init()

def listening():
    global robot_ear
    global you
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic, timeout=5, phrase_time_limit=5)

    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: "+ you)

def understanding():
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
    elif "stop" in you:
        robot_brain="I will stop the program"
    else:
        robot_brain = "I'm fine thank you and you"

    print(robot_brain)

def speaking():
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    


#Listening Part

while "stop" not in robot_brain :
    listening()
    understanding()
    speaking()

    

