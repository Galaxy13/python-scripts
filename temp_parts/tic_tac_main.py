from temp_parts.ext_lib import poc_ttt_provided as provided

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
from temp_parts.ext_lib import poc_ttt_gui

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000  # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player
EMPTY = provided.EMPTY
PLAYERX = provided.PLAYERX
PLAYERO = provided.PLAYERO
DRAW = provided.DRAW


# Add your functions here.
def mc_trial(board, player):
    while board.check_win() is None:
        random_square = (random.randrange(board.get_dim()), random.randrange(board.get_dim()))
        if random_square in board.get_empty_squares():
            board.move(random_square[0], random_square[1], player)
            player = provided.switch_player(player)
        else:
            continue
    return


def mc_update_scores(scores, board, player):
    if player == DRAW:
        return
    else:
        temp_board = board.clone()
        for index_row, row in enumerate(scores):
            for index_col, square in enumerate(row):
                if temp_board.square(index_row, index_col) == player:
                    scores[index_row][index_col] += (player - 1)
                elif temp_board.square(index_row, index_col) == EMPTY:
                    continue
                else:
                    scores[index_row][index_col] -= (provided.switch_player(player) - 1)


def get_best_move(board, scores):
    empty_list = board.get_empty_squares()
    if len(empty_list) > 1:
        max_score = 0
        max_score_index = ()
        for square in empty_list:
            if scores[square[0]][square[1]] > max_score:
                max_score_index = square
                max_score = scores[square[0]][square[1]]
        return max_score_index
    else:
        return empty_list[0]


def mc_move(board, player, trials):
        score_list = []
        for row_index in range(board.get_dim()):
            score_list.append([])
            for dummy_col in range(board.get_dim()):
                score_list[row_index].append(0)

        for dummy_int in range(trials):
            board_clone = board.clone()
            mc_trial(board_clone, player)
            game_win = board_clone.check_win()
            mc_update_scores(score_list, board_clone, game_win)

        best_move = get_best_move(board, score_list)
        print(best_move)
        return best_move[0], best_move[1]



# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)

# board = provided.TTTBoard(3)
# player = provided.PLAYERX
# print(board)
# board.move(1, 1, PLAYERX)
# player = provided.switch_player(player)
# mc_trial(board, player)
# print(board)
# board.move(0, 0, PLAYERO)
# # mc_trial(board, player)
# print(board)
#
# temp_list = []
# for i in range(3):
#     temp_list.append([])
#     for j in range(3):
#         temp_list[i].append(0)
#
# # player = board.check_win()
# player = board.check_win()
# for dummy_int in range(NTRIALS):
#     board_clone = board.clone()
#     mc_trial(board_clone, player)
#     player = board_clone.check_win()
#     mc_update_scores(temp_list, board_clone, player)
#
# print(temp_list)
#
# print(get_best_move(board, temp_list))

# print(board)
# print(mc_move(board, player, NTRIALS))