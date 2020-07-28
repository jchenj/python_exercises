#! /usr/bin/python3
# ABS_15_stopwatch.py -> A simple stopwatch program with justified output copied
# to clipboard

import pyperclip
import time

lapNumWidth = 2
totalTimeWidth = 6
lapTimeWidth = 6

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to click the stopwatch. Press CTRL-C to quit.')
input()   # Press Enter to begin
print('Stopwatch started.')
startTime = time.time()  # Get the first lap's start time
lastTime = startTime
lapNum = 1
totalLapOutput = []

# Start tracking the lap times
try:
    while True:
        # Keep a lap counter and increment it each time the user presses enter
        input()
        # Calculate the elapsed time by subtracting timestamps
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)        
        lapOutput = 'Lap # %s: %s (%s)' % (str(lapNum).rjust(lapNumWidth),
                                     str(totalTime).rjust(totalTimeWidth),
                                     str(lapTime).rjust(lapTimeWidth))

        print(lapOutput, end= ' ')                 
        totalLapOutput.append(lapOutput)
        lapNum += 1
        lastTime = time.time()   # Reset the last lap time

except KeyboardInterrupt:
    # Handle the KeyboardInterrupt exception so that the user can press CTRL-C to quit without displaying an error message
    print('\nDone.')

formattedTotalLapOutput = '\n'.join(totalLapOutput)
pyperclip.copy(formattedTotalLapOutput)
print('Total lap output copied to clipboard.')

'''
Learning:
- Had to assign lapOutput in order to append to totalLapOutput
- To make list totalLapOutput into string, used str.join, with new line between
each row in the list
'''
