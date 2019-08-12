# Game to play Rock Paper Scissors against the computer
# Computer guesses based on a random integer, compares to player guesses

# import relevant libraries

from random import randint
import time

# Define allowed game variables
rps = ['Rock', 'Paper', 'Scissors']
allowed_player_guesses = ['rock', 'Rock', 'paper', 'Paper', 'scissors', 'Scissors']
play_game_responses = ['Y', 'y', 'N', 'n']

# startup sequence

print("Welcome to Rock Paper Scissors! (c) Andrew Lynch 2019")
time.sleep(1)
print("Would you like to play? Enter Y/N")
play_game = input()
while play_game not in play_game_responses:
    print("I don't understand. Would you like to play? Enter Y/N")
    play_game = input()

if play_game == 'Y' or play_game == 'y':
    print("Great! Let's play Rock Paper Scissors!")
    time.sleep(1)

    # initialise scores
    computer_score = 0
    player_score = 0
    tie_games = 0
    total_games = 0

    # Set up continuous play loop
    while play_game == 'Y' or play_game == 'y':

        # Randomly generate an element from the list of possible computer guesses
        computer_guess = rps[randint(0,2)]

        # Get player input
        print("What do you want to play? Rock, Paper or Scissors?")
        print("Enter your turn: ")
        player_guess = input()
        if player_guess not in allowed_player_guesses:
            print("I don't understand. Do you want to play Rock, Paper or Scissors?")
            player_guess = input()
        else:
            time.sleep(1)
            print("ooooo.......")
            time.sleep(1)
            print("\n")

        # convert lower case to capitalised

        if player_guess == 'rock':
            player_guess = 'Rock'
        elif player_guess == 'paper':
            player_guess = 'Paper'
        elif player_guess == 'scissors':
            player_guess = 'Scissors'
        else:
            continue

        print("You played " + player_guess + ".")
        print("Computer played...")
        time.sleep(1)
        print(computer_guess)
        print("\n")
        time.sleep(1.5)

        # return result

        if computer_guess == player_guess:
            print("It's a tie! What are the odds?!")
            tie_games += 1
        elif computer_guess == 'Rock' and player_guess == 'Paper':
            print("You win!")
            player_score += 1
        elif computer_guess == 'Rock' and player_guess == 'Scissors':
            print("You lose...")
            computer_score += 1
        elif computer_guess == 'Scissors' and player_guess == 'Paper':
            print("You lose...")
            computer_score += 1
        elif computer_guess == 'Scissors' and player_guess == 'Rock':
            print("You win!")
            player_score += 1
        elif computer_guess == 'Paper' and player_guess == 'Rock':
            print("You lose...")
            computer_score += 1
        elif computer_guess == 'Paper' and player_guess == 'Scissors':
            print("You win!")
            player_score += 1
        else:
            continue

        total_games += 1
        time.sleep(1)
        print("\n")
        print("Computer: " + str(computer_score))
        print("Player: " + str(player_score))
        print("Tied games: " + str(tie_games))
        print("\n")
        print("Win percentage: " + '{:.1%}'.format(player_score/total_games))
        print("\n")
        print("Play again? (Y/N)")
        play_game = input()
        while play_game not in play_game_responses:
            print("I don't understand. Do you want to play again? Y/N")
            play_game = input()
        if play_game == 'Y' or play_game == 'y':
            continue
        else:
            print("Thanks for playing!")
            break

else:
    print("Thanks for playing!")
