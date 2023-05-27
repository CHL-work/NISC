import pytest
import bingo

def test_check_winner_row_true():
    input_card = [
                  [False, False, False, False, False], 
                  [False, False, False, False, False], 
                  [True, True, True, True, True], 
                  [False, False, False, False, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_row_true failed!"


def test_check_winner_column_true():
    input_card = [
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_column_true failed!"

def test_check_winner_diagonal_true_1():
    input_card = [
                  [True, False, False, False, False], 
                  [False, True, False, False, False], 
                  [False, False, True, False, False], 
                  [False, False, False, True, False], 
                  [False, False, False, False, True]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_diagonal_true_1 failed!"

def test_check_winner_diagonal_true_2():
    input_card = [
                  [False, False, False, False, True], 
                  [False, False, False, True, False], 
                  [False, False, True, False, False], 
                  [False, True, False, False, False], 
                  [True, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_diagonal_true_2 failed!"

def test_check_winner_false():
    input_card = [
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card)==False, "test_check_winner_false failed!"

def test_check_winner_false_2():
    input_card = [
                  [False, False, False, False, False], 
                  [False, False, False, False, False], 
                  [False, False, False, False, False], 
                  [False, False, False, False, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card)==False, "test_check_winner_false_2 failed!"


def test_play_no_winners():
    called_squares = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, -1, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [15, 25, 35, 45, 55],
            [16, 26, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 48, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [], "test_play_no_winners failed!"

def test_play_winner_first_turn():
    called_squares = [[0, 10], [0, 14]]
    card_data = [
    	[
            [10, 20, 30, 40, 50],
            [-1, 21, 31, 41, 51],
            [-1, 22, 32, 42, 52],
            [-1, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [10, 20, -1, 40, -1],
            [11, 21, -1, 41, -1],
            [12, 22, -1, 42, -1],
            [13, 23, -1, 43, -1],
            [14, 24, -1, 44, -1]
        ],

    ]
    assert bingo.play(called_squares, card_data) == [1], "test_play_winner_first_turn failed!"

def test_play_one_winner_row():
    called_squares = [[0, 10], [1, 20], [2, 30], [3, 40], [4, 50]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, -1, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [15, 25, 35, 45, 55],
            [16, 26, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 48, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [0], "test_play_one_winner_row failed!"

def test_play_one_winner_column():
    called_squares = [[0, 10], [0, 11], [0, 12], [0, 13], [0, 14]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, -1, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [15, 25, 35, 45, 55],
            [16, 26, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 48, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [0], "test_play_one_winner_column failed!"

def test_play_free_space_winner():
    called_squares = [[2, 30], [2, 31], [2, 32], [2, 33]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, 32, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, 32, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, -1, 44, 54]
        ],
    ]
    assert bingo.play(called_squares, card_data) == [1], "test_play_free_space_winner failed!"

def test_play_diagonal_winner():
    called_squares = [[0, 10], [1, 21], [2, 32], [3, 43], [4, 54]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, 32, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22,  0, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
    ]
    assert bingo.play(called_squares, card_data) == [0], "test_play_diagonal_winner failed!"

def test_play_multiple_winners():
    called_squares = [[0, 10], [1, 21], [2, 32], [3, 43],[4, 54]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, 32, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [10, 25, 35, 45, 55],
            [16, 21, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 43, 58],
            [19, 29, 39, 49, 54]
        ],
        [
            [10, 25, 35, 45, 55],
            [16, 26, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 48, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [0, 1], "test_play_multiple_winners failed!"

def test_play_game_end():
    called_squares = [[0, 10], [1, 21], [2, 32], [3, 43], [4, 54], [4, 59]]
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, 32, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [10, 25, 35, 45, 55],
            [16, 21, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 38, 43, 58],
            [19, 29, 39, 49, 54]
        ],
        [
            [10, 25, 35, 45, 55], #This should not be a winning card 
            [16, 21, 36, 46, 56], #game should be ended before calling [4, 59]
            [17, 27, -1, 47, 57],
            [18, 28, 38, 43, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [0, 1], "test_play_game_end failed!"


def test_play_no_called_squares():
    called_squares = []
    card_data = [
        [
            [10, 20, 30, 40, 50],
            [11, 21, 31, 41, 51],
            [12, 22, -1, 42, 52],
            [13, 23, 33, 43, 53],
            [14, 24, 34, 44, 54]
        ],
        [
            [15, 25, 35, 45, 55],
            [16, 26, 36, 46, 56],
            [17, 27, -1, 47, 57],
            [18, 28, 37, 48, 58],
            [19, 29, 39, 49, 59]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [], "test_play_no_called_squares failed!"


