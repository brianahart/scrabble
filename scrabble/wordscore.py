def score_word(word):
    """Takes a word as an input and returns the Scrabble value"""

    word = word.lower()
    # Initialize the score as 0 
    score = 0

    # Dictionary of scores per letter
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
              "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
              "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
              "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
              "x": 8, "z": 10}

    # Loop over the characters in the word 
    for c in word:

        # If the character is in the dictionary, add the value to score 
        if c in scores.keys():
            score += scores[c]

    # Return the score 
    return score
