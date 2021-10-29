import random

from wordscore import score_word


class Player:
    """A player in the game"""

    def __init__(self):
        self.name = ''
        self.letters = []
        self.letter_count = 0
        self.score = 0

    def add_score(self, word):
        """Adds the score of the word that the user entered"""

        self.score += score_word(word)

    def add_letter_to_word(self, board, place):
        """Adds a letter to the play area word and removes it from the rack"""

        if len(board.play_area_list) <= 7 and ' ' in board.play_area_list:
            letter = self.letters.pop(place)
            board.play_area_list[board.play_area_list.index(' ')] = letter

    def pick_letters(self, letter_bag):
        """Draws letters from the given bag. Return the bag without those letters"""

        # Create a dictionary from the given dict 
        letter_bag = letter_bag

        self.letter_count = len(self.letters)

        # Until the player has 7 letters
        while self.letter_count < 7:

            if len(letter_bag) == 0:
                break

            # Draw one letter and add it to the rack's list of letters 
            random_num = random.randrange(len(letter_bag))
            keys_list = list(letter_bag.keys())
            letter_drawn = keys_list[random_num]

            #letters_list = [i for i in letter_bag.keys()]
            #letter_drawn = random.choices(letters_list)
            letter_str = letter_drawn[0]
            self.letters.append(letter_str)

            # Remove one letter from the bag
            letter_bag[letter_str] = letter_bag[letter_str] - 1

            # If that was the last letter, remove that key from the dictionary 
            if letter_bag[letter_str] == 0:
                letter_bag.pop(letter_str)

            # Add one to the count of letters on the rack 
            self.letter_count += 1

        return letter_bag
