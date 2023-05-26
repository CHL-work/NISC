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

def test_check_winner_row_false():
    input_card = [
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [True, True, True, True, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card)==False, "test_check_winner_row_false failed!"

def test_check_winner_col_true():
    input_card = [
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_col_true failed!"

def test_check_winner_col_false():
    input_card = [
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, True, False, False, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card)==False, "test_check_winner_col_false failed!"

def test_check_winner_dia_true_1():
    input_card = [
                  [True, False, False, False, False], 
                  [False, True, False, False, False], 
                  [False, False, True, False, False], 
                  [False, False, False, True, False], 
                  [False, False, False, False, True]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_dia_true_1 failed!"

def test_check_winner_dia_true_2():
    input_card = [
                  [False, False, False, False, True], 
                  [False, False, False, True, False], 
                  [False, False, True, False, False], 
                  [False, True, False, False, False], 
                  [True, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card), "test_check_winner_dia_true_2 failed!"

def test_check_winner_dia_false():
    input_card = [
                  [True, False, False, False, True], 
                  [False, True, False, True, False], 
                  [False, False, True, False, False], 
                  [False, True, False, True, False], 
                  [False, False, False, False, False]
                 ]
    assert bingo.check_winner(input_card)==False, "test_check_winner_dia_false failed!"

def test_vertical_match():
    called_squares = [[1, 21], [1, 19], [1, 24], [1, 20], [1, 30]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 72],
            [10, 17, 41, 58, 62],
            [2, 26, -1, 48, 66],
            [7, 18, 37, 60, 63],
            [14, 30, 35, 59, 73]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [0], "test_vertical_match failed!"

def test_diagonal_match():
    called_squares = [[0, 4], [1, 17], [2, 1], [3, 60], [4, 73]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 72],
            [10, 17, 41, 58, 62],
            [2, 26, -1, 48, 66],
            [7, 18, 37, 60, 63],
            [14, 30, 35, 59, 73]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [1], "test_diagonal_match failed!"

def test_no_winners():
    called_squares = [[0, 6], [1, 16], [2, 36], [3, 46]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 72],
            [10, 17, 41, 58, 62],
            [2, 26, -1, 48, 66],
            [7, 18, 37, 60, 63],
            [14, 30, 35, 59, 73]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [], "test_no_winners failed!"

def test_row_match():
    called_squares = [[0, 4], [1, 16], [2, 40], [3, 46], [4, 72]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 72],
            [10, 17, 41, 58, 62],
            [2, 26, -1, 48, 66],
            [7, 18, 37, 60, 63],
            [14, 30, 35, 59, 73]
        ]
    ]
    assert bingo.play(called_squares, card_data) == [1], "test_row_match failed!"

def test_multiple_winners():
    called_squares = [[0, 6], [1, 19], [2, 52], [3, 65]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 6],
            [10, 17, 41, 19, 62],
            [2, 26, -1, 48, 66],
            [7, 52, 37, 60, 63],
            [65, 30, 35, 59, 73]
        ]
    ]
    print(bingo.play(called_squares, card_data) )
    assert bingo.play(called_squares, card_data) == [0, 1], "test_multiple_winners failed!"

def test_multiple_winners_2(): #test if the game end immediately if there is a winner
    called_squares = [[0, 6], [1, 19], [2, 52], [3, 65], [4, 66]]
    card_data = [
        [
            [6, 21, 36, 55, 61],
            [12, 19, 43, 56, 69],
            [9, 24, -1, 46, 71],
            [3, 20, 44, 52, 67],
            [1, 30, 34, 57, 65]
        ],
        [
            [4, 16, 40, 46, 6],
            [10, 17, 41, 19, 62],
            [2, 26, -1, 48, 66],
            [7, 52, 37, 60, 63],
            [65, 30, 35, 59, 73]
        ],
        [
            [4, 16, 40, 46, 6],
            [10, 17, 41, 19, 62],
            [2, 26, -1, 48, 66],
            [7, 52, 37, 60, 63],
            [66, 30, 35, 59, 73]
        ]
    ]
    print(bingo.play(called_squares, card_data) )
    assert bingo.play(called_squares, card_data) == [0, 1], "test_multiple_winners failed!"


