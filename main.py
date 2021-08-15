from Board_class import Board
from ai import *


def player_turn():
    print("What do you play?")
    has_played = False
    while not has_played:
        # TODO implement try_except block if user does not input an integer
        play_cell = int(input())
        if playing_board.turn(play_cell-1):
            has_played = True
        else:
            print('That square was already taken please choose a new square')
    playing_board.print_board()
    return playing_board.is_winner()


def computer_turn(which_ai):
    play_cell = which_ai(playing_board)
    playing_board.turn(play_cell)
    playing_board.print_board()
    return playing_board.is_winner()


if __name__ == "__main__":
    playing_board = Board()
    print("How do you want to play")
    print("1. Player vs Player")
    print("2. Player vs Computer")
    print("3. Computer vs Computer")
    game_mode = input("I want to play number ")
    # Player vs Player
    if game_mode == "1":
        player1 = input("What is the name of player 1? ")
        player2 = input("What is the name of player 2? ")
        winner = ""
        while winner == "":
            if playing_board.whose_turn == playing_board.ex:
                print(f"it is {player1}'s turn")
            else:
                print(f"it is {player2}'s turn")
            winner = player_turn()
        if winner == playing_board.ex:
            print(f"Congratulations {player1}! You have won!")
        elif winner == playing_board.o:
            print(f"Congratulations {player2}! You have won!")
        else:
            print("It is a draw!")

    # Player vs Computer
    if game_mode == "2":
        print("Which Computer Ai do you want to use")
        for i in range(len(ai_types)):
            print(f"{i+1}. {ai_type_string[i]}")
        ai_choice = ai_types[int(input())-1]
        turn_choice = input("Do you want to go first or second (f or s)? ")
        first_turn = "computer"
        second_turn = "player"
        if turn_choice == 'f':
            first_turn = "player"
            second_turn = "computer"
        winner = ''
        while winner == '':
            turn = second_turn
            if playing_board.whose_turn == playing_board.ex:
                turn = first_turn
            if turn == "computer":
                winner = computer_turn(ai_choice)
            else:
                winner = player_turn()
        if winner == playing_board.ex:
            print(f"{first_turn} is the victor")
        else:
            print(f"{second_turn} is the victor")

    # Computer vs Computer
    if game_mode == "3":
        print("Which Computer Ai do you want to use for the first computer")
        for i in range(len(ai_types)):
            print(f"{i + 1}. {ai_type_string[i]}")
        ai_choice1 = ai_types[int(input()) - 1]
        print("Which Computer Ai do you want to use for the second computer")
        ai_choice2 = ai_types[int(input()) - 1]
        winner = ""
        while winner == "":
            turn = ai_choice2
            if playing_board.whose_turn == playing_board.ex:
                turn = ai_choice1
            winner = computer_turn(turn)
        if winner == playing_board.ex:
            print(f"")