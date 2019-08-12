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


# set up 'play again' variable that decides if game will be repeated
play_again = 'Y'

# initialise scores
computer_score = 0
player_score = 0

# Define different computer guesses
rps = ['Rock', 'Paper', 'Scissors']

# Set up continuous play loop
while play_again == 'Y':

    # Randomly generate an element from the list of possible computer guesses
    computer_guess = rps[randint(0,2)]

    # Get player input
    print("What do you want to play? Rock, Paper or Scissors?")
    print("Enter your turn: ")
    player_guess = input()
    time.sleep(2)
    print("ooooo.......")
    time.sleep(1)

    # return result

    if computer_guess == player_guess:
        print("It's a tie! What are the odds?!")
    elif computer_guess == 'Rock' and player_guess == 'Paper':
        print("You win!")
        print()

    print("Play again? (Y/N)")
