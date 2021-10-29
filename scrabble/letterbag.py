import json


class LetterBag:
    """The bag of letters that are available in the game. The main one used during game play will lose letters as
    users pick from the bag. """

    def __init__(self):
        self.letter_data = {}
        self.letter_dist = {}
        self.letter_scores = {}

    # ------------------------------------------------------------------
    # Functions to Process the Letter Info   
    # ------------------------------------------------------------------

    def get_letters(self, file):
        """Gets the list of scrabble letters distributions and returns a dict"""

        # Create a dictionary to store the letters data
        with open(file, "r") as infile:
            self.letter_data = json.load(infile)

        return self.letter_data

    def get_tile_dist(self, data):
        """Get the letter distributions from the data"""

        # Create a dictionary to store the letters and their distributions 
        self.letter_dist = {}
        for i in data['letters']:
            self.letter_dist[i] = data['letters'][i]['tiles']

        return self.letter_dist

    def get_letter_scores(self, data):
        """Get the letter distributions from the data"""

        # Create a dictionary to store the letters and their distributions 
        self.letter_scores = {}
        for i in data['letters']:
            self.letter_scores[i] = data['letters'][i]['points']

        return self.letter_scores
