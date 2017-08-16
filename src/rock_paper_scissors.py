"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""

def rock_paper_scissors(player1_input, player2_input):
    if ((player1_input == 'rock' and player2_input == 'scissors') or
            (player1_input == 'scissors' and player2_input == 'paper') or
            (player1_input == 'paper' and player2_input == 'rock')):
        return 1

    return 2

def create_player_time_message(player_name):
    return "{player_name} it is your time. Do you wanna paper, scissors or rock? ".format(player_name=player_name)

def create_result_message(player, winner_play, looser_play):
    return "{player} WON!!! {winner_play} beats {looser_play}".format(player=player, winner_play=winner_play, looser_play=looser_play)

def main():
    player1 = input("Player 1, type your name: ")
    player2 = input("Player 2, type your name: ")

    quit_game = 'y'
    while quit_game == 'y':
        player1_input = input(create_player_time_message(player1))
        player2_input = input(create_player_time_message(player2))

        game_result = rock_paper_scissors(player1_input, player2_input)

        if game_result == 1:
            print(create_result_message(player1, player1_input, player2_input))
        else:
            print(create_result_message(player2, player2_input, player1_input))

        quit_game = input("Do you wanna play again? [y/n] ")

if __name__ == "__main__":
    main()
