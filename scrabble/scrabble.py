from boardgui import *
from board import *
from letterbag import *
from scrabbledict import *
from player import *



class GameEngine:
    """Runs the game"""

    def __init__(self):
        # Generate the Scrabble dictionary
        self.s_dict = ScrabbleDict()
        self.s_dict.generate_data("sowpods.txt")

        # Generate the letter data, the letter bag, and the letter scores 
        self.l_bag = LetterBag()
        self.letter_data = self.l_bag.get_letters("letters.json")
        self.letter_bag = self.l_bag.get_tile_dist(self.letter_data)
        self.letter_scores = self.l_bag.get_letter_scores(self.letter_data)

        # Generate players 1 and 2
        self.p1 = Player()
        self.p1.name = "Player 1"
        self.p2 = Player()
        self.p2.name = "Player 2"

        # Players both pick letters to start 
        self.p1.pick_letters(self.letter_bag)
        self.p2.pick_letters(self.letter_bag)

        # Create the Scrabble Board 
        self.board = Board(self.p1, self.p2, self.letter_bag, self.s_dict)

        # Set current player to p1 
        self.board.current_player = self.p1

        # Create the GUI & initialize the game
        self.gui = BoardGUI(self.board,
                            self.l_bag.get_tile_dist(self.letter_data),
                            self.letter_scores)

game = GameEngine()
game.gui.window.mainloop()
