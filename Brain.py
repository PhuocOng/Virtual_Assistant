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

