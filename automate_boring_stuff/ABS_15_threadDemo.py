#! /usr/bin/python3
# ABS_15_threadDemo.py

import threading
import time

print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End of program')

