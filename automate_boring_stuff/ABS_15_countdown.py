#! /usr/bin/python3
# ABS_15_countdown.py > a simple countdown script

import subprocess
import time

timeLeft = 10

while timeLeft > 0:
    print(timeLeft)  
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file
subprocess.Popen(['open','231-freelancing.mp3'])

'''
Question:
- Why does making print(timeLeft) into print(timeLeft, end= ' ') result in
no numbers being printed until end of countdown?
'''
