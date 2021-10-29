import re


class ScrabbleDict:
    """The Scrabble Dictionary that generates data and contains a list of all valid words """

    def __init__(self):
        self.scrabble_dict = []

    def generate_data(self, file):
        """Generates a list of all the words in the scrabble dictionary and returns a list of data"""

        with open(file, "r") as infile:
            raw_input = infile.readlines()
            self.scrabble_dict = [datum.strip('\n') for datum in raw_input]

        return self.scrabble_dict

    def check_valid_word(self, word):
        """Check's a player's input to see if it is a valid word in the Scrabble Dictionary"""

        valid = False
        error = ''

        wild_index = word.find('*')
        wild_letter = ''

        # If the word has a wildcard in it 
        if '*' in word:

            # Define the regex word
            regex_word = '^' + word.replace('*', '[A-Z]') + '$'

            # Check every word for a match to our regex word 
            for w in self.scrabble_dict:
                match = re.match(regex_word, w)
                if match:
                    if wild_letter == '':
                        wild_letter = match[0][wild_index]
                    valid = True

        # If the word does not have a wildcard
        else:

            # If the word is in the Scrabble Dictionary, return true
            if word in self.scrabble_dict:
                valid = True

        # If the word is not in the Scrabble Dictionary, give an error  
        if valid is False:
            error = 'That is not a valid word in the Scrabble Dictionary!'

        return valid, error, wild_letter
