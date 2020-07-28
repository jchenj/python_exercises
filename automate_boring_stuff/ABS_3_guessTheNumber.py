# This is a guess the random number game
import random
secret_number = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

# Ask the player to guess six times
for guessesTaken in range(1,7):
    print("Take a guess.")
    guess = int(input())

    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break  # This condition is the correct guess.


if guess == secret_number:
    print("Congratulations! You guessed my number in " + str(guessesTaken) + " guesses.")
else:
    print("Nope, the number I was thinking of was " + str(secret_number) + ".")
    
