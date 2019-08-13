# Program to simulate Rock Paper Scissors and compare distribution of results
# Computer guesses based on a random integer, compares to player guesses

# import relevant libraries

from random import randint
import time
import matplotlib.pyplot as plt

# Define allowed game variables
rps = ['Rock', 'Paper', 'Scissors']
play_game_responses = ['Y', 'y', 'N', 'n']

# startup sequence
print("Welcome to Rock Paper Scissors! (c) Andrew Lynch 2019")
time.sleep(1)
print("\n" + "Would you like to play? Enter Y/N")
play_game = input()

# loop awaiting acceptable response
while play_game not in play_game_responses:
    print("I don't understand. Would you like to play? Enter Y/N")
    play_game = input()

# initialise game
if play_game == 'Y' or play_game == 'y':
    print("Great! Let's play Rock Paper Scissors!")
    time.sleep(1)

    # Set up continuous play loop as long as the player
    # wants to continue
    while play_game == 'Y' or play_game == 'y':

        # reset game_simulations variable for repeat plays

        game_simulations = 0

        # start game
        print("How many games do you want to play?")

        # validate user input
        try:
            game_simulations = int(input())
        except ValueError:
            print("That's not a number. How many games do you want to play?")

        # start simulation
        print("OK. Simulating games...")
        time.sleep(2)

        # initialise scores
        computer_score = 0
        player_score = 0
        tie_games = 0
        total_games = 0

        # initialise empty list to track on-going results
        score_graph = []

        # set up scores in list and guess indices
        rock = 0
        paper = 1
        scissors = 2

        computer_guesses = [0,0,0]
        player_guesses = [0,0,0]


        # Repeating simulation loop

        for x in range(game_simulations):

            # Randomly generate a computer guess and a player guess
            # from the list of possible computer guesses
            computer_guess = rps[randint(0,2)]
            player_guess = rps[randint(0,2)]

            # track the results of the computer and player guesses in the
            # appropriate list item

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
            score = player_score - computer_score
            score_graph.append(score)

        print("\n")
        print("The results are in...")
        time.sleep(1)
        print("\n")
        print("Computer: " + str(computer_score))
        print("Player: " + str(player_score))
        print("Tied games: " + str(tie_games))
        print("\n")
        print("Win percentage: " + '{:.1%}'.format(player_score/total_games))
        print("\n")
        print("Computer guesses: ")
        print("Rock: " + '{:.2%}'.format(computer_guesses[rock]/total_games))
        print("Paper: " + '{:.2%}'.format(computer_guesses[paper]/total_games))
        print("Scissors: " + '{:.2%}'.format(computer_guesses[scissors]/total_games))
        print("\n")
        print("player guesses: ")
        print("Rock: " + '{:.2%}'.format(player_guesses[rock]/total_games))
        print("Paper: " + '{:.2%}'.format(player_guesses[paper]/total_games))
        print("Scissors: " + '{:.2%}'.format(player_guesses[scissors]/total_games))

        print("\n")
        print("Do you want to see a graph of the results? Enter Y/N.")
        show_graph = input()
        while show_graph not in play_game_responses:
            print("I don't understand. Would you like to play? Enter Y/N")
            play_game = input()
        if show_graph == 'Y' or show_graph == 'y':
            plt.plot(score_graph)
            plt.show()
        else:
            continue

        # Set up repeat games
        print("Play again? (Y/N)")
        play_game = input()

        # while loop awaits valid user input
        while play_game not in play_game_responses:
            print("I don't understand. Do you want to play again? Y/N")
            play_game = input()
        if play_game == 'Y' or play_game == 'y':
            continue
        # end point
        else:
            print("Thanks for playing!")
            break

else:
    print("Thanks for coming! See you soon.")
