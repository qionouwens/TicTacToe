import random
from Board_class import Board


def get_available(board):
    available_list = []
    for index, available in enumerate(board.available):
        if available:
            available_list.append(index)
    return available_list


def random_ai(board):
    return random.choice(get_available(board))


def random_with_finish_ai(board):
    available = get_available(board)
    current_board = tuple(board.board)
    current_turn = board.whose_turn
    for cell in available:
        new_board = Board(list(current_board), current_turn)
        new_board.turn(cell)
        if new_board.is_winner() != "":
            return cell
    return random.choice(available)


def random_start_conors_ai(board):
    available = get_available(board)
    if len(available) > 7:
        available_conors = []
        for i in available:
            if i in [0, 2, 6 ,8]:
                available_conors.append(i)
        return random.choice(available_conors)
    return random.choice(available)


def random_start_middle_ai(board):
    available = get_available(board)
    if 4 in available:
        return 4
    return random.choice(available)


def block_and_finish_ai(board):
    available = get_available(board)
    current_board = tuple(board.board)
    current_turn = board.whose_turn
    if current_turn == board.ex:
        opponents_turn = board.o
    else:
        opponents_turn = board.ex
    for i in available:
        new_board = Board(list(current_board), current_turn)
        new_board.turn(i)
        if new_board.is_winner() != '':
            return i
    for i in available:
        new_board = Board(list(current_board), opponents_turn)
        new_board.turn(i)
        if new_board.is_winner() != '':
            return i
    return random.choice(available)


def min_max_ai(board):
    max_player = board.whose_turn


ai_type_string = ["random ai", "random with finish", "random start conors", "random start middle",
                  "block and finish", "min max"]
ai_types = [random_ai, random_with_finish_ai, random_start_conors_ai, random_start_middle_ai, block_and_finish_ai,
            min_max_ai]

if __name__ == "__main__":
    playing_board = Board()
    playing_board.turn(4)
    playing_board.turn(3)
    playing_board.turn(7)
    playing_board.turn(0)
    playing_board.print_board()
    for _ in range(15):
        print(random_ai(playing_board))
    print("-------------------------")
    for _ in range(15):
        print(random_with_finish_ai(playing_board))

