"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
try:
    import SimpleGUICS2Pygame.codeskulptor as codeskulptor
except:
    import codeskulptor

codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    if board.check_win() is not None:
        return [SCORES[board.check_win()]]

    empty_squares = board.get_empty_squares()
    best_score = -3
    if player == provided.PLAYERO:
        factor = -1
    else:
        factor = 1

    for move in empty_squares:
        temp_board = board.clone()
        temp_board.move(move[0], move[1], player)
        score = mm_move(temp_board, provided.switch_player(player))
        if score[0] * factor == 1:
            best_score = score[0] * factor
            best_move = (move[0], move[1])
            return best_score * factor, best_move
        elif score[0] * factor > best_score:
            best_score = score[0] * factor
            best_move = (move[0], move[1])
    return best_score * factor, best_move


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

provided.play_game(move_wrapper, 1, False)
poc_ttt_gui.run_gui(3, provided.PLAYERX, move_wrapper, 1, False)

board = provided.TTTBoard(3)
board.move(1, 1, provided.PLAYERX)
board.move(0, 0, provided.PLAYERO)
board.move(2, 2, provided.PLAYERX)
board.move(0, 2, provided.PLAYERO)

print(mm_move(board, provided.PLAYERX))
