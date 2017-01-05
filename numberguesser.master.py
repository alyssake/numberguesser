# This is a guess the number game.
import random  # not explaining this

# Set a minimum and maximum value for the possible range
minimum = 1
maximum = 20

# Chooses a random number between min and max
number = random.randint(minimum, maximum)

# Ask for user's name
print("Hello! What is your name?")

# User writes in their name, code saves input as Username
username = input()

# Tells user the range of numbers to guess from
print(username + ", I am thinking of a number between " +
      str(minimum) + " and " + str(maximum))

# Counts the number of guesses so far
guessesTaken = 0

while (guessesTaken < 6):
    print('Take a guess.')  # providing these three lines
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1   # providing this

    if guess < number:
        print("Your guess is too low.")

    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print("Good job, " + username + "! You guessed my number in " +
          guessesTaken + " guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was " + number)
