#! usr/bin/python3
# ABS_10_debugCoinToss.py -> A coin toss guessing game where the player gets two guesses

import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program.')

import random
guess = []
while guess not in ["0", "1"]:
    print('Guess the coin toss! Enter 1 for heads or 0 for tails:')
    guess = input()
toss = str(random.randint(0, 1)) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    while guess not in ["0", "1"]:
        print('Enter 1 for heads or 0 for tails.')
        guess = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

logging.debug('End of program.')

"""What I learned:
- Practiced initiating & disabling logging messages.
- Need to make types of input and values to check against match up
- Use input validation where needed
- Exceptions are for graceful crashes with user errors
- Assertions are for programmer errors

To learn:
- More about using debugging messages
- Why wasn't I able to step through code when I set breakpoint to first print statement?
"""
