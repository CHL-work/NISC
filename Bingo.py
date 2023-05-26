def check_winner(matched_card):
    n = len(matched_card)
    # check rows
    for i in range(n):
        if all(matched_card[i]):
            return True
    # check columns
    for i in range(n):
        if all(matched_card[j][i] for j in range(n)):
            return True
    # check diagonals
    if all(matched_card[i][i] for i in range(n)) or all(matched_card[i][n - i - 1] for i in range(n)):
        return True
    return False

def play(calledSquares, cardData):
    winners = []
    n = len(cardData[0]) # number of rows/columns in each card
    # create matched cards data with the same dimensions as cardData
    matched_cards = [[[row[col] == -1 for col in range(n)] for row in card] for card in cardData]

    for round in calledSquares:
        _, value = round
        for i, card in enumerate(cardData):
            # update the matched card according to the called square
            for j in range(n):
                for k in range(n):
                    if card[j][k] == value:
                        matched_cards[i][j][k] = True
            # check if this card is a winner
            if check_winner(matched_cards[i]):
                winners.append(i)
        if winners: # if we have winners, end the game
            break
    return winners

def main():
    calledSquares = [[1, 21], [1, 19], [1, 24], [1, 20], [1, 30]]
    cardData = [
        [
         [6, 21, 36, 55, 61], 
         [12, 19, 43, 56, 69], 
         [9, 24, -1, 46, 71], 
         [3, 20, 44, 52, 67], 
         [1, 30, 34, 57, 65]],
        [
         [4, 16, 40, 46, 72], 
         [10, 17, 41, 58, 62], 
         [2, 26, -1, 48, 66], 
         [7, 18, 37, 60, 63], 
         [14, 30, 35, 59, 73]]
    ]

    print(play(calledSquares, cardData)) # Output: [0]


if __name__ == "__main__":
    main()

