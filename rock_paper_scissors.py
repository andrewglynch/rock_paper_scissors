# Game to play Rock Paper Scissors against the computer
# Computer guesses based on a random integer, compares to player guesses

# import relevant libraries

from random import randint

# startup sequence

print("Welcome to Rock Paper Scissors! (c) Andrew Lynch 2019")
time.sleep(1)
print("Would you like to play? Enter Y/N")
start_game = input()
if start_game == 'N':
    print("Thanks for coming!")
    break
elif start_game != 'Y':
    print("I don't understand. Would you like to play? Enter Y/N")
else print("Great! Let's play Rock Paper Scissors!")
time.sleep(1)


# Define different computer guesses

rps = ['Rock', 'Paper', 'Scissors']

# Randomly generate an element from the list of possible computer guesses
computer_guess = rps[randint(0,2)]

# Get player input

player_guess = input()
