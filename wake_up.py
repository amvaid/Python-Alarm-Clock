import sys
import time
import webbrowser
import random
import os

#Verify the creation of the text file
if os.path.isfile("YT.txt") == False:
    print "Error: YT.txt file not present!"
    sys.exit(1)


print """What time do you want to wake up?
Use this form \n Example: 06:30 (24-Hour time)"""
alarm = raw_input("> ")

Time = time.strftime("%H:%M")

with open("YT.txt") as f:
    content = f.readlines()

print "The time is " + Time

while Time != alarm:
    Time = time.strftime("%H:%M")
    time.sleep(1)

if Time == alarm:
    print "Time to Wake Up!"
    random_video = random.choice(content)
    webbrowser.open(random_video)