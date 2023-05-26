# NISC Technical Assessment

This repository contains Python code to the 2 changelles - Bingo and Count Occurrences.

## Bingo

Simulate a game of Bingo as per the rules provided in the problem statement. 

### How to Run

The code is written in Python 3 and can be run directly using any Python 3 interpreter, either from the command line or an IDE. 

Run the main file:

```
python bingo.py
```

Run the unit tests::

```
python -m pytest -s test_bingo.py
```

### How it Works

The main logic of the Bingo game is encapsulated in the `play()` function. It takes in two parameters, `calledSquares` and `cardData`, which respectively represent the squares called out in each round of the game, and the data for all Bingo cards in play.

The function creates a matched card for each card in play, initially marking a square as True if it is a free space (-1), and False otherwise. For each called square, it updates the matched card data, marking the square as True if the value is present in the respective card.

After each update, it checks if the updated card is a winner using the `check_winner()` function. This function checks for a winning condition, which is met if all values in a row, column, or either diagonal are True.

If any winners are found, the game ends immediately and the function returns a list of the indices of the winning cards.

The `test_bingo_simulation.py` file contains unit tests for the `play()` and `check_winner()` functions to ensure they work correctly.

Sure, here's a simple README.md for your project:

---

## Count Occurrences

This is a Python module that counts the occurrences of each character in a given string. It is designed to handle only ASCII characters (character codes 0 through 127).

### How it works

The main function, `count_occurrences(text)`, takes a string as input. It iterates over each character in the string. If the character is an ASCII character, the function increases its count in a dictionary.

After counting all characters, the function sorts the dictionary by the ASCII value of the characters and converts it to a list of tuples. Each tuple contains a character and its count.

### How to run

Run the main file:

```
python count.py
```

Run the unit tests::

```
python -m pytest -s test_count.py
```


