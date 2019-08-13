# Program to simulate Rock Paper Scissors and compare distribution of results
# Computer guesses based on a random integer, compares to player guesses

# import relevant libraries

from random import randint
import time
import matplotlib.pyplot as plt

# Define allowed game variables
rps = ['Rock', 'Paper', 'Scissors']
# allowed_player_guesses = ['rock', 'Rock', 'paper', 'Paper', 'scissors', 'Scissors']
# play_game_responses = ['Y', 'y', 'N', 'n']

# startup sequence

print("Welcome to the Rock Paper Scissors Simulator! (c) Andrew Lynch 2019")
print("\n" + "How many games would you like to play? Enter a number.")
play_game = input()


try:
   play_game = int(play_game)
   print("Yes input string is an Integer.")
   print("Input number value is: ", play_game)
except ValueError:
   print("That's not an int!")
   print("No.. input string is not an Integer. It's a string")


while type(play_game) == int:
    # start game
    print("OK, let's go!")
    print("Simulating games...")
    time.sleep(2)

    # initialise scores
    computer_score = 0
    player_score = 0
    tie_games = 0
    total_games = 0

    # set up scores in list and guess indices
    rock = 0
    paper = 1
    scissors = 2

    computer_guesses = [0,0,0]
    player_guesses = [0,0,0]


    # Set up continuous play loop
    for range in range(play_game):

        # Randomly generate a computer guess and a player guess
        # from the list of possible computer guesses
        computer_guess = rps[randint(0,2)]
        player_guess = rps[randint(0,2)]

        # track the results of the computer and player guesses in the
        # appropriate list

        if computer_guess == 'Rock':
            computer_guesses[rock] +=1
        elif computer_guess == 'Paper':
            computer_guesses[paper] +=1
        else:
            computer_guesses[scissors] +=1

        if player_guess == 'Rock':
            player_guesses[rock] +=1
        elif player_guess == 'Paper':
            player_guesses[paper] +=1
        else:
            player_guesses[scissors] +=1

        # return result based on logic flow

        if computer_guess == player_guess:
            tie_games += 1
        elif computer_guess == 'Rock' and player_guess == 'Paper':
            player_score += 1
        elif computer_guess == 'Rock' and player_guess == 'Scissors':
            computer_score += 1
        elif computer_guess == 'Scissors' and player_guess == 'Paper':
            computer_score += 1
        elif computer_guess == 'Scissors' and player_guess == 'Rock':
            player_score += 1
        elif computer_guess == 'Paper' and player_guess == 'Rock':
            computer_score += 1
        elif computer_guess == 'Paper' and player_guess == 'Scissors':
            player_score += 1
        else:
            continue

        # score tracker and display

        total_games += 1

    print("Computer: " + str(computer_score))
    print("Player: " + str(player_score))
    print("Tied games: " + str(tie_games))
    print("\n")
    print("Win percentage: " + '{:.1%}'.format(player_score/total_games))
    print("\n")
    print("Computer guesses: ")
    print("Rock: " + '{:.1%}'.format(computer_guesses[rock]/total_games))
    print("Paper: " + '{:.1%}'.format(computer_guesses[paper]/total_games))
    print("Scissors: " + '{:.1%}'.format(computer_guesses[scissors]/total_games))
    print("\n")
    print("player guesses: ")
    print("Rock: " + '{:.1%}'.format(player_guesses[rock]/total_games))
    print("Paper: " + '{:.1%}'.format(player_guesses[paper]/total_games))
    print("Scissors: " + '{:.1%}'.format(player_guesses[scissors]/total_games))

        # Set up repeat games
    print("Enter how many games you want to simulate, or type \"Quit\" to end.")
    play_game = input()

    if play_game == 'Quit' or play_game == 'quit':
        print("Thanks for playing -- see you next time!")

    else:
        play_game = int(play_game)
