# Bingo

This repository contains Python code to simulate a game of Bingo as per the rules provided in the problem statement. 

## How to Run

The code is written in Python 3 and can be run directly using any Python 3 interpreter, either from the command line or an IDE. 

Run the main file:

```
python bingo.py
```

Run the unit tests::

```
python -m pytest -s test_bingo.py
```

## How it Works

The main logic of the Bingo game is encapsulated in the `play()` function. It takes in two parameters, `calledSquares` and `cardData`, which respectively represent the squares called out in each round of the game, and the data for all Bingo cards in play.

The function creates a matched card for each card in play, initially marking a square as True if it is a free space (-1), and False otherwise. For each called square, it updates the matched card data, marking the square as True if the value is present in the respective card.

After each update, it checks if the updated card is a winner using the `check_winner()` function. This function checks for a winning condition, which is met if all values in a row, column, or either diagonal are True.

If any winners are found, the game ends immediately and the function returns a list of the indices of the winning cards.

The `test_bingo_simulation.py` file contains unit tests for the `play()` and `check_winner()` functions to ensure they work correctly.

