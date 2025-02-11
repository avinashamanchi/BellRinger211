# bellRinger 2/11 p5
# create a python code that takes the time in your time zone and the output is in minutes and how much time till class ends

from datetime import datetime

class_end_time = datetime.strptime("14:19", "%H:%M")

current_time_str = input("enter the current time (hours:minutes in the 24-hour format): ")
current_time = datetime.strptime(current_time_str, "%H:%M")

time_left = class_end_time - current_time
minutes_left = time_left.total_seconds() / 60

if minutes_left < 0:
    print("the class of computer science has been finished")
else:
    print(f"u have {int(minutes_left)} minutes left until the class ends")

