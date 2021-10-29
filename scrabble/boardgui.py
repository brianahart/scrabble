from tkinter import *



class BoardGUI:
    """ This class makes the board, letter racks, and score. The board is a 15 x 15 grid."""

    def __init__(self, board, letter_dist, letter_scores):

        # Creates the window via Tkinter
        self.window_size = 1500
        self.window = Tk()
        self.window.title('Scrabble')
        self.canvas = Canvas(self.window, width=self.window_size, height=self.window_size)
        self.canvas.pack()

        # Set the gui's board and letter_dist 
        self.board = board
        self.letter_dist = letter_dist

        # Initialize lists to hold the tkinter elements
        self.board_gui_list = []
        self.p1_letters_gui = []
        self.p2_letters_gui = []
        self.pa_gui_list = []
        self.remaining_letters_list = []

        # Initialize all board objects 
        self.initialize_remaining_letters(20, 60, self.letter_dist, self.board.letter_bag)
        self.initialize_letter_scores(20, 400, letter_scores)
        self.initialize_board(200, 60)
        self.initialize_score(1000, 60)
        self.initialize_racks(1000, 240)
        self.initialize_play_area(1000, 600)
        self.update_gui()

        # Create a button to handle user clicks 
        self.window.bind('<Button-1>', self.handle_click)

    # ------------------------------------------------------------------
    # Functions to Draw the Board, Racks, Score Area, Play Area, and Letter Scores
    # ------------------------------------------------------------------

    def initialize_board(self, x_offset, y_offset):
        """Creates an empty board on the GUI"""

        self.board_x_offset = x_offset
        self.board_y_offset = y_offset

        # Create the title 
        self.canvas.create_text(self.board_x_offset + 375,
                                self.board_y_offset - 20,
                                text='Scrabble!',
                                font=('Helvetica bold', 24))

        # Create a square background
        self.canvas.create_rectangle(self.board_x_offset,
                                     self.board_y_offset,
                                     self.board_x_offset + 750,
                                     self.board_y_offset + 750,
                                     fill='#C2B298')

        # Create vertical lines 
        for i in range(16):
            self.canvas.create_line(self.board_x_offset + (i * 50),
                                    self.board_y_offset,
                                    self.board_x_offset + (i * 50),
                                    self.board_y_offset + 750)

        # Create horizontal lines 
        for i in range(16):
            self.canvas.create_line(self.board_x_offset,
                                    self.board_y_offset + (i * 50),
                                    self.board_x_offset + 750,
                                    self.board_y_offset + (i * 50))

        # Mark the center of the board 
        self.canvas.create_oval(self.board_x_offset + 372,
                                self.board_y_offset + 372,
                                self.board_x_offset + 378,
                                self.board_y_offset + 378,
                                fill='#FF7F7F')

        # Mark the start point 
        self.start_point = self.canvas.create_rectangle((self.board.start_x * 50) + 2 + self.board_x_offset,
                                                        (self.board.start_y * 50) + 2 + self.board_y_offset,
                                                        ((self.board.start_x + 1) * 50) - 2 + self.board_x_offset,
                                                        ((self.board.start_y + 1) * 50) - 2 + self.board_y_offset,
                                                        outline='red',
                                                        width=2)

    def initialize_racks(self, x_offset, y_offset):
        """Creates empty player racks for players 1 & 2 on the GUI"""

        self.rack_x_offset = x_offset
        self.rack_y_offset = y_offset

        # Player 1: Label rack and create rectangles to hold letters 
        self.canvas.create_text(self.rack_x_offset,
                                self.rack_y_offset - 20,
                                text='Player 1:',
                                font=('Helvetica', 18),
                                anchor='w')

        for i in range(7):
            self.canvas.create_rectangle(self.rack_x_offset + (i * 50),
                                         self.rack_y_offset,
                                         self.rack_x_offset + ((i + 1) * 50),
                                         self.rack_y_offset + 50,
                                         fill='#EBC9A3')

        # Player 2: Label rack and create rectangles to hold letters
        self.canvas.create_text(self.rack_x_offset,
                                self.rack_y_offset + 80,
                                text='Player 2:',
                                font=('Helvetica', 18),
                                anchor='w')

        for i in range(7):
            self.canvas.create_rectangle(self.rack_x_offset + (i * 50),
                                         self.rack_y_offset + 100,
                                         self.rack_x_offset + ((i + 1) * 50),
                                         self.rack_y_offset + 150,
                                         fill='#EBC9A3')

    def initialize_score(self, x_offset, y_offset):
        """Creates aa empty score area on the GUI"""

        self.score_x_offset = x_offset
        self.score_y_offset = y_offset

        # Create four rectangles to hold the score
        self.canvas.create_rectangle(self.score_x_offset,
                                     self.score_y_offset,
                                     self.score_x_offset + 200,
                                     self.score_y_offset + 40,
                                     fill='lightblue')
        self.canvas.create_rectangle(self.score_x_offset,
                                     self.score_y_offset + 40,
                                     self.score_x_offset + 200,
                                     self.score_y_offset + 100)
        self.canvas.create_line(self.score_x_offset + 100,
                                self.score_y_offset,
                                self.score_x_offset + 100,
                                self.score_y_offset + 100)

        # Add labels for Players 1 & 2 
        self.canvas.create_text(self.score_x_offset + 50,
                                self.score_y_offset + 20,
                                text='Player 1',
                                font=('Helvetica bold', 18))
        self.canvas.create_text(self.score_x_offset + 150,
                                self.score_y_offset + 20,
                                text='Player 2',
                                font=('Helvetica bold', 18))

        # Initialize the scores
        self.p1_score = Label(text=self.board.p1.score,
                              font=('Helvetica', 18))
        self.p1_score.place(x=self.score_x_offset + 50,
                            y=self.score_y_offset + 70,
                            anchor='center')
        self.p2_score = Label(text=self.board.p2.score,
                              font=('Helvetica', 18))
        self.p2_score.place(x=self.score_x_offset + 150,
                            y=self.score_y_offset + 70,
                            anchor='center')

    def initialize_play_area(self, x_offset, y_offset):
        """Creates the play area on the GUI"""

        self.pa_x_offset = x_offset
        self.pa_y_offset = y_offset

        # ------ Label and Spaces ------ # 
        # Create a label for the current player
        self.current_player = Label(text=f'Current Player: {self.board.current_player.name}',
                                    font=('Helvetica bold', 18),
                                    anchor='center')
        self.current_player.place(x=self.pa_x_offset + 75,
                                  y=self.pa_y_offset - 100)

        # Create empty spaces for the letters 
        for i in range(7):
            self.canvas.create_line(self.pa_x_offset + (i * 50) + 2,
                                    self.pa_y_offset,
                                    self.pa_x_offset + (i * 50) + 46,
                                    self.pa_y_offset)

        # ------ Buttons ------ # 
        # Create a button to pass a turn
        self.pass_turn = Button(text='Pass',
                                command=self.pass_turn)
        self.pass_turn.place(x=self.pa_x_offset,
                             y=self.pa_y_offset + 20)

        # Create button to change word directions 
        self.change_dir = Button(text='Current Dir: →',
                                 command=self.change_word_dir)
        self.change_dir.place(x=self.pa_x_offset + 80,
                              y=self.pa_y_offset + 20)

        # Create a button to reset the letters 
        self.reset = Button(text='Reset',
                            command=self.reset_word)
        self.reset.place(x=self.pa_x_offset + 200,
                         y=self.pa_y_offset + 20)

        # Create a button to submit words 
        self.submit = Button(text='Submit!',
                             command=self.submit_word)
        self.submit.place(x=self.pa_x_offset + 270,
                          y=self.pa_y_offset + 20)

        # ------ Error Message ------ #  
        # Create an error label and initializes it as blank 
        self.error_msg = Label(text='',
                               font=('Helvetica bold', 14),
                               fg='red')

        self.error_msg.place(x=self.pa_x_offset + 0,
                             y=self.pa_y_offset + 60)

    def initialize_letter_scores(self, x_offset, y_offset, letter_scores):
        """Creates a box and displays the remaining letters"""

        # Create a rectangle and give the box a label 
        self.canvas.create_rectangle(x_offset,
                                     y_offset,
                                     x_offset + 120,
                                     y_offset + 320,
                                     fill='grey')
        self.canvas.create_text(x_offset + 60,
                                y_offset + 30,
                                text="LETTER\nSCORES",
                                font=('Helvetica bold', 14))

        loc = [0, 0]

        # For each letter in letter scores
        for letter in letter_scores.keys():

            # If the letter is 'N' go to the next column 
            if letter == 'O':
                loc = [54, 0]

            # Display the scores
            text = f"{letter} - {letter_scores[letter]}"
            self.canvas.create_text(x_offset + loc[0] + 32,
                                    y_offset + loc[1] + 64,
                                    text=text,
                                    font=('Helvetica', 14))
            loc[1] += 18

    def initialize_remaining_letters(self, x_offset, y_offset, letter_dist, letter_bag):
        """Creates a box and reads the remaining letters, then displays them"""

        # Create a rectangle and give the box a label 
        self.canvas.create_rectangle(x_offset,
                                     y_offset,
                                     x_offset + 120,
                                     y_offset + 320,
                                     fill='lightgrey')
        self.canvas.create_text(x_offset + 60,
                                y_offset + 30,
                                text="REMAINING\n  LETTERS",
                                font=('Helvetica bold', 14))

        # Loop over the letters in the letter distribution
        loc = [0, 0]
        i = 0
        for letter in letter_dist.keys():

            # If the letter is 'O' go to the next column 
            if letter == 'O':
                loc = [54, 0]

            # If the letter is in the letter bag, display the number of tiles remaining
            if letter in letter_bag:
                text = f"{letter} - {letter_bag[letter]}"

            # If the letter is not in the letter bag, display 0 
            else:
                text = f"{letter} - 0"

            # Create a label for the letter text
            rem_letter = Label(text=text,
                               font=('Helvetica', 14),
                               bg='lightgrey')

            rem_letter.place(x=x_offset + loc[0] + 14,
                             y=y_offset + loc[1] + 50)

            # Add the label to the remaining letters list
            self.remaining_letters_list.append(rem_letter)

            loc[1] += 18
            i += 1

    # ------------------------------------------------------------------
    # Function to Update All Board Areas  
    # ------------------------------------------------------------------

    def update_gui(self):
        """Update everything on the GUI"""

        self.update_racks(self.board.p1.letters, self.board.p2.letters)
        self.update_play_area(self.board.play_area_list)

    # ------------------------------------------------------------------
    # Functions to Update Board, Racks, Score, Play Area, and Remaining Tiles 
    # ------------------------------------------------------------------

    def update_board(self, scrabble_board):
        """Updates the board when a player plays a word"""

        # Reset the board 
        for i in self.board_gui_list:
            self.canvas.delete(i)
        self.board_gui_list.clear()

        # Loop over the columns
        for i in range(15):

            # Loop over the rows
            for j in range(15):

                # Get the letter from the Scrabble Board 
                letter = scrabble_board[j][i]

                # If there's a wildcard 
                if '*' in letter:
                    letter = '*'

                if letter != ' ':
                    # Print the letter in the space
                    l_gui = self.canvas.create_text(self.board_x_offset + (i * 50) + 25,
                                                    self.board_y_offset + (j * 50) + 25,
                                                    text=letter,
                                                    font=('Helvetica bold', 18))
                elif letter == ' ':
                    l_gui = self.canvas.create_text(self.board_x_offset + (i * 50) + 25,
                                                    self.board_y_offset + (j * 50) + 25,
                                                    text=' ',
                                                    font=('Helvetica bold', 18))

                self.board_gui_list.append(l_gui)

    def update_racks(self, p1_letters, p2_letters):
        """Updates the rack with the player's current letters"""

        # Delete the existing letters 
        for i in self.p1_letters_gui:
            self.canvas.delete(i)
        self.p1_letters_gui.clear()

        # For every letter in the player's list, add text for that letter
        for i in range(len(p1_letters)):
            l = self.canvas.create_text(self.rack_x_offset + (i * 50) + 25,
                                        self.rack_y_offset + 25,
                                        text=p1_letters[i],
                                        font=('Helvetica bold', 18))

            # Append the text to the player's list 
            self.p1_letters_gui.append(l)

        # Delete the existing letters
        for i in self.p2_letters_gui:
            self.canvas.delete(i)
        self.p2_letters_gui.clear()

        # For every letter in the player's list, add text for that letter
        for i in range(len(p2_letters)):
            l = self.canvas.create_text(self.rack_x_offset + (i * 50) + 25,
                                        self.rack_y_offset + 125,
                                        text=p2_letters[i],
                                        font=('Helvetica bold', 18))

            # Append the text to the player's list 
            self.p1_letters_gui.append(l)

    def update_scores(self, p1_score, p2_score):
        """Updates players scores"""

        self.p1_score['text'] = p1_score
        self.p2_score['text'] = p2_score

    def update_play_area(self, letters):
        """Add letters to the play area"""

        # Print the current player     
        self.current_player['text'] = f'Current Player: {self.board.current_player.name}'

        # Reset the current play area 
        for i in self.pa_gui_list:
            self.canvas.delete(i)
        self.pa_gui_list.clear()

        # Print the letters to the play area 
        for i in range(len(letters)):

            letter = letters[i]

            # If there's a wild card, get the first value 
            if '*' in letter:
                letter = letter[0]

            l = self.canvas.create_text(self.pa_x_offset + (i * 50) + 25,
                                        self.pa_y_offset - 25,
                                        text=letter,
                                        font=('Helvetica bold', 18))

            self.pa_gui_list.append(l)

    def update_remaining_letters(self, letter_dist, letter_bag):
        """Updates the remaining letters on the GUI"""

        # For each letter in the letter distribution 
        i = 0
        for letter in letter_dist.keys():

            # If the letter is in the letter bag, display the number of tiles remaining
            if letter in letter_bag:
                text = f"{letter} - {letter_bag[letter]}"

            # If the letter is not in the letter bag, display 0 
            else:
                text = f"{letter} - 0"

            self.remaining_letters_list[i]['text'] = text
            i += 1

    # ------------------------------------------------------------------
    # Functions to Print Messages  
    # ------------------------------------------------------------------

    def print_msg(self, error):
        """Prints messages to the playing area"""

        self.error_msg['text'] = error

    # ------------------------------------------------------------------
    # Functions to Handle Clicks  
    # ------------------------------------------------------------------

    def handle_click(self, event):
        """Handles click events"""

        # Player 1 Rack 
        if (self.rack_x_offset < event.x < self.rack_x_offset + 350 and
            self.rack_y_offset < event.y < self.rack_y_offset + 50
            and self.board.current_player == self.board.p1):

            for i in range(7):
                if self.rack_x_offset + (i * 50) < event.x < self.rack_x_offset + ((i + 1) * 50):
                    self.click_on_letter(i, self.board.p1)

        # Player 2 Rack 
        elif (self.rack_x_offset < event.x < self.rack_x_offset + 350 and
              self.rack_y_offset + 100 < event.y < self.rack_y_offset + 150
              and self.board.current_player == self.board.p2):

            for i in range(7):
                if self.rack_x_offset + (i * 50) < event.x < self.rack_x_offset + ((i + 1) * 50):
                    self.click_on_letter(i, self.board.p2)

        # Board 
        elif (self.board_x_offset < event.x < self.board_x_offset + 750
              and self.board_y_offset < event.y < self.board_y_offset + 750):
            for i in range(15):
                for j in range(15):
                    if ((i * 50) + self.board_x_offset < event.x < ((i + 1) * 50) + self.board_x_offset and
                            (j * 50) + self.board_y_offset < event.y < ((j + 1) * 50) + self.board_y_offset):
                        self.click_on_square(i, j)

    def click_on_letter(self, x, player):
        """Handles click event on the letters on the rack"""

        player.add_letter_to_word(self.board, x)
        self.board.set_play_area()
        self.update_gui()

    def click_on_square(self, x, y):
        """Handles clicks on the board"""

        # Set the start point on the board 
        self.board.set_start_point(x, y)

        # Highlight that square 
        self.canvas.coords(self.start_point,
                           (x * 50) + 2 + self.board_x_offset,
                           (y * 50) + 2 + self.board_y_offset,
                           ((x + 1) * 50) - 2 + self.board_x_offset,
                           ((y + 1) * 50) - 2 + self.board_y_offset)

        self.board.reset_play_area()
        self.update_gui()

    # ------------------------------------------------------------------
    # Functions to Handle Buttons 
    # ------------------------------------------------------------------

    def pass_turn(self):
        """Switch the current player"""

        self.board.reset_play_area()
        self.board.switch_current_player()
        self.update_gui()

    def change_word_dir(self):
        """Handles clicks on the change direction button"""

        self.board.change_direction()

        if self.board.direction == 'horizontal':
            self.change_dir['text'] = 'Current Dir: →'
        else:
            self.change_dir['text'] = 'Current Dir: ↓'

        self.board.reset_play_area()
        self.update_gui()

    def reset_word(self):
        """Resets the players letters and play area"""

        self.board.reset_play_area()
        self.update_gui()

    def submit_word(self):
        """When the user submits a word, check if it is valid. If it's valid, add it to the board"""

        submitted_word = ''
        word_with_wilds = ''

        # Add letters from the play area to the word to submit 
        for c in self.board.play_area_list:

            # If the index contains a wild card already set 
            if '=*' in c:

                submitted_word += c[0]
                word_with_wilds += '*'

            elif c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ*':
                submitted_word += c
                word_with_wilds += c

            elif c == ' ':
                break

        self.error_msg['text'] = ''

        # If it is a valid word in the scrabble dictionary 
        if self.board.scrabble_dict.check_valid_word(submitted_word)[0]:

            # If the word can be added to the board 
            if self.board.check_word_in_board(submitted_word)[0]:

                # Add the word to the board and update the gui 
                self.board.add_word_to_board(submitted_word, word_with_wilds)
                self.update_board(self.board.scrabble_board)
                self.update_scores(self.board.p1.score, self.board.p2.score)
                self.update_remaining_letters(self.letter_dist, self.board.letter_bag)
                self.is_gameover()
                self.update_gui()

            # If the word is not valid to be added to the board 
            else:
                self.print_msg(self.board.check_word_in_board(submitted_word)[1])
                self.reset_word()

        # If it is not a valid word, print the error 
        else:
            self.print_msg(self.board.scrabble_dict.check_valid_word(submitted_word)[1])
            self.reset_word()

    # ------------------------------------------------------------------
    # Function to End the Game 
    # ------------------------------------------------------------------

    def is_gameover(self):
        """Handle the end of game"""

        # If the letter bag is empty 
        if len(self.board.letter_bag) == 0:

            winner_txt = ''
            # Determine a winner 
            if self.board.p1.score > self.board.p2.score:
                winner_txt = f"{self.board.p1.name} wins!"
            elif self.board.p1.score < self.board.p2.score:
                winner_txt = f"{self.board.p2.name} wins!"
            else:
                winner_txt = "Tie!"

            self.canvas.create_rectangle(self.board_x_offset + 200,
                                         self.board_y_offset + 200,
                                         self.board_x_offset + 550,
                                         self.board_y_offset + 550,
                                         fill='white')

            self.canvas.create_text(self.board_x_offset + 375,
                                    self.board_y_offset + 345,
                                    anchor='center',
                                    text="GAME OVER",
                                    font=('Helvetica bold', 24),
                                    fill='blue')

            self.canvas.create_text(self.board_x_offset + 375,
                                    self.board_y_offset + 405,
                                    anchor='center',
                                    text=winner_txt,
                                    font=('Helvetica bold', 24),
                                    fill='blue')
