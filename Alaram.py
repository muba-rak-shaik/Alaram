import datetime
from playsound import playsound

alarmHour = int(input("Enter Hour (24-hour format): "))
alarmMin = int(input("Enter Minutes: "))

while True:
    if alarmHour == datetime.datetime.now().hour and alarmMin == datetime.datetime.now().minute:
        print("Playing...")
        playsound("alaram.mp3")
        break
