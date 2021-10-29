class Board:
    """The actual board that contains empty spaces and spaces occupied by letters"""

    def __init__(self, player1, player2, letter_bag, scrabble_dict):
        self.scrabble_board = [[' ' for i in range(15)] for j in range(15)]
        self.word_count = 0
        self.letter_bag = letter_bag
        self.scrabble_dict = scrabble_dict

        self.p1 = player1
        self.p2 = player2
        self.current_player = self.p1

        self.start_x = 7
        self.start_y = 7
        self.direction = 'horizontal'
        self.play_area_list = [' ' for i in range(7)]
        self.board_letters = []

    # ------------------------------------------------------------------
    # Functions to Check Words for Validity on the Board  
    # ------------------------------------------------------------------

    def check_word_in_board(self, word):
        """Checks if a word can be added to the dictionary"""
        # Checks if the first word intersects with the center space 
        # Checks if the user used any of their letters
        # Checks if there is an intersection with another word
        # Checks if the word goes out of bounds 

        valid = True
        error = ''

        if self.word_count == 0 and self.check_center(word) is False:
            error = 'The first word needs to go through the center!'
            valid = False

        elif self.word_count > 0 and self.check_user_letters() is False:
            error = 'You need to use at least one letter from your board!'
            valid = False

        elif self.word_count > 0 and self.check_boundary(word) is False:
            error = 'That word goes out of bounds!'
            valid = False
            return valid, error

        elif self.word_count > 0 and self.check_intersect(word)[0] is False:
            error = self.check_intersect(word)[1]
            valid = False

        elif self.word_count > 0 and self.check_nearby_letters(word) is False:
            error = 'All adjacent letters must spell a valid word!'
            valid = False

        return valid, error

    def check_boundary(self, word):
        """Check if the word is out of bounds"""

        valid = True

        # If the direction is vertical  
        if self.direction == 'vertical':
            if len(word) + self.start_y > 15:
                valid = False

        # If the direction is horizontal 
        elif self.direction == 'horizontal':
            if len(word) + self.start_x > 15:
                valid = False

        return valid

    def check_intersect(self, word):
        """Check if the word intersects with another """

        valid = True
        intersections = 0
        error = ''

        x = self.start_x
        y = self.start_y

        # For each letter in the word
        for c in word:

            # Get the value of the current square 
            square = self.scrabble_board[y][x]

            # If there's a wild card, set the square equal to the corresponding letter 
            if '*' in square:
                square = square[0]

            # If the square is the same as the new letter, set valid to true 
            if square == c:
                valid = True
                intersections += 1

                # Else if the square already has a letter, set valid to false
            elif square != ' ':
                valid = False
                intersections += 1
                error = 'That word intersects with another word on the board!'

            # If the direction is vertical  
            if self.direction == 'vertical':

                # Increment in the y direction
                y += 1

            # If the direction is horizontal 
            elif self.direction == 'horizontal':

                # Increment in the x direction 
                x += 1

        # If there is not at least one intersection, set valid to False (only for words after the first)
        if intersections < 1:
            valid = False
            error = 'That word is not anchored on any other word!'

        return valid, error

    def check_center(self, word):
        """Check if the first word intersects with the center space"""

        valid = False

        x = self.start_x
        y = self.start_y

        # For each letter in the word
        for i in range(len(word)):

            # Check if any letter passes through the center
            if x == 7 and y == 7:
                valid = True

            # If the direction is vertical  
            if self.direction == "vertical":

                # Increment in the y direction
                y += 1

            # If the direction is horizontal 
            elif self.direction == "horizontal":

                # Increment in the x direction 
                x += 1

        return valid

    def check_user_letters(self):
        """Check that the user used at least one of their own letters"""

        valid = True

        if len(self.current_player.letters) >= 7:
            valid = False

        return valid

    def check_nearby_letters(self, word):
        """Check if the new word is too close to other words (and they don't form a new word)"""

        valid = True

        # ------ Horizontal ------#

        if self.direction == 'horizontal':

            # ------ Check up and down directions ------#

            x = self.start_x
            print("Horizontal: up and down")

            # For each letter in the word
            for c in word:

                new_word = c[0]
                y = self.start_y - 1

                while y >= 0 and self.scrabble_board[y][x] != ' ':
                    new_word = self.scrabble_board[y][x][0] + new_word
                    y -= 1

                y = self.start_y + 1

                while y < 15 and self.scrabble_board[y][x] != ' ':
                    new_word = new_word + self.scrabble_board[y][x][0]
                    y += 1

                if len(new_word) > 1 and self.scrabble_dict.check_valid_word(new_word)[0] is False:
                    valid = False
                
                print(x, y, new_word)

                x += 1

            # ------ Check left and right directions ------#

            print("Horizontal: left and right")

            x = self.start_x - 1
            y = self.start_y
            
            new_word = word

            while x >= 0 and self.scrabble_board[y][x] != ' ':
                new_word = self.scrabble_board[y][x] + new_word
                x -= 1

            x = self.start_x + len(word) 

            while x < 15 and self.scrabble_board[y][x] != ' ':
                new_word = new_word + self.scrabble_board[y][x][0]
                x += 1

            if len(new_word) > 1 and self.scrabble_dict.check_valid_word(new_word)[0] is False:
                valid = False

            print(x, y, new_word)

        # ------ Vertical ------#

        elif self.direction == 'vertical':

            # ------ Check left and right directions ------#

            y = self.start_y
            print("Vertical: left and right")

            # For each letter in the word
            for c in word:

                new_word = c[0]
                x = self.start_x - 1
                
                while x >= 0 and self.scrabble_board[y][x] != ' ':
                    new_word = self.scrabble_board[y][x][0] + new_word
                    x -= 1

                x = self.start_x + 1

                while x < 15 and self.scrabble_board[y][x] != ' ':
                    new_word = new_word + self.scrabble_board[y][x][0]
                    x += 1

                if len(new_word) > 1 and self.scrabble_dict.check_valid_word(new_word)[0] is False:
                    valid = False

                print(x, y, new_word)

                y += 1

            # ------ Check up and down directions ------#

            print("Vertical: up and down")

            x = self.start_x
            y = self.start_y - 1
            
            new_word = word

            while y >= 0 and self.scrabble_board[y][x] != ' ':
                new_word = self.scrabble_board[y][x] + new_word
                y -= 1

            y = self.start_y + len(word) 

            while y < 15 and self.scrabble_board[y][x] != ' ':
                new_word = new_word + self.scrabble_board[y][x][0]
                y += 1

            if len(new_word) > 1 and self.scrabble_dict.check_valid_word(new_word)[0] is False:
                valid = False

            print(x, y, new_word)
                
        return valid

    # ------------------------------------------------------------------
    # Function to Add Words to the Board  
    # ------------------------------------------------------------------

    def add_word_to_board(self, submitted_word, word_with_wilds):
        """Ensures that the user is able to add the word they spelled to the board. If so, it is added to the
        Scrabble Board """

        x = self.start_x
        y = self.start_y

        # For each letter in the word 
        for c in submitted_word:

            # If the character is a wild card and it is the first wildcard
            if c == '*' and self.scrabble_board[y][x] == ' ':

                # Get the corresponding letter
                wild_letter = self.scrabble_dict.check_valid_word(submitted_word)[2]

                # Add the mapping to the board 
                self.scrabble_board[y][x] = f'{wild_letter}=*'

            # If the character is a wild card and it is not the first wildcard
            elif '=*' in self.scrabble_board[y][x]:
                pass

            # Not a wild card
            else:
                # Add the letter to the Scrabble Board
                self.scrabble_board[y][x] = c

            # If the direction is vertical  
            if self.direction == 'vertical':

                # Increment in the y direction
                y += 1

            # If the direction is horizontal 
            elif self.direction == 'horizontal':

                # Increment in the x direction 
                x += 1

        # Increment the word count of the board
        self.word_count += 1

        # Add the  word to the current player's score and pick new letters
        self.current_player.add_score(word_with_wilds)
        self.current_player.pick_letters(self.letter_bag)

        # Update the play area 
        self.play_area_list = [' ' for i in range(7)]
        self.set_play_area()

        # Switch the current player 
        self.switch_current_player()

    # ------------------------------------------------------------------
    # Function to Switch Current Player and Pass Turn
    # ------------------------------------------------------------------

    def switch_current_player(self):
        """Function that switches the current player"""

        if self.current_player == self.p1:
            self.current_player = self.p2
        else:
            self.current_player = self.p1

    # ------------------------------------------------------------------
    # Function to Set Start Point and Direction
    # ------------------------------------------------------------------

    def set_start_point(self, x, y):
        """Sets the x and y start points"""

        self.start_x = x
        self.start_y = y

    def change_direction(self):
        """Switch the direction from horizontal to vertical (and vice versa)"""

        if self.direction == 'horizontal':
            self.direction = 'vertical'
        else:
            self.direction = 'horizontal'

    # ------------------------------------------------------------------
    # Function to Reset Play Area
    # ------------------------------------------------------------------

    def reset_play_area(self):
        """Resets the play area"""

        for i in range(len(self.play_area_list)):

            letter = self.play_area_list[i]
            if letter != ' ' and i not in self.board_letters:
                self.current_player.letters.append(letter)

        # Reset the play area to all spaces 
        self.play_area_list = [' ' for i in range(7)]

        self.set_play_area()

    def set_play_area(self):
        """Fills the play area with the letters from scrabble board"""

        # Reset the letters from the board
        self.board_letters = []

        # Add letters on the board to the playing area letters
        if self.direction == 'horizontal':

            # While i is less than 7 and start_x + 1 is less than 16
            i = 0
            while i < 7 and self.start_x + i < 15:

                letter_on_board = self.scrabble_board[self.start_y][self.start_x + i]

                # If that space on the scrabble board is not empty 
                if letter_on_board != ' ':
                    # Add the letter to the play area list
                    self.play_area_list[i] = letter_on_board

                    # Add that index to the board letters list 
                    self.board_letters.append(i)

                i += 1

        elif self.direction == 'vertical':

            # While i is less than 7 and start_x + 1 is less than 16
            i = 0
            while i < 7 and self.start_y + i < 15:

                letter_on_board = self.scrabble_board[self.start_y + i][self.start_x]

                # If that space on the scrabble board is not empty
                if letter_on_board != ' ':
                    # Add the letter to the play area list
                    self.play_area_list[i] = letter_on_board

                    # Add that index to the board letters list 
                    self.board_letters.append(i)

                i += 1
