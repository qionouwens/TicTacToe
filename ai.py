import random
import Board_class


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
    starting_board =


def random_start_conors_ai(board):
    pass


def random_start_middle_ai(board):
    pass


def block_and_finish_ai(board):
    pass


def min_max_ai(board):
    pass


ai_type_string = ["random ai", "random with finish", "random start conors", "random start middle",
                  "block and finish", "min max"]
ai_types = [random_ai, random_with_finish_ai, random_start_conors_ai, random_start_middle_ai, block_and_finish_ai,
            min_max_ai]

if __name__ == "__main__":
    playing_board = Board_class.Board()
    playing_board.turn(4)
    playing_board.turn(3)
    playing_board.turn(7)
    playing_board.print_board()
    for _ in range(15):
        print(random_ai(playing_board))

