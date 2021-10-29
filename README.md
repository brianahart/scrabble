# Scrabble! 

## General Layout 

There are 6 areas to the game:
1. Remaining Letters - this box shows the counts of each letter remaining in the tile bag.
2. Letter Scores - this box shows the score associated with each letter. 
3. Main Board - the board is where the game takes place. Players will click on it to chose where to start their words and it will update once a valid word is submitted. 
4. Scores - this box shows each player's current score. 
5. Player Letter Racks - there is one rack for Player 1 and one rack for Player 2. The current player will only be able to select from letters in their rack. After a player successfully submits a valid word, the game will automatically choose new letters for them from the tile bag. 
6. Play Area - this area contains 7 empty spaces that the player will spell their word in. It will prepopulate with any letters that are already on the board. 

## Rules
Game starts on Player 1's turn. 

1. Current player clicks on a square on the game board to indicate where they would like to start their word. 
2. The player selects what direction they would like their word to go (horizontal or veritcal) 
3. The current player selects letters from their board to spell a word
4. The player clicks Submit! to add their word to the board    
	&nbsp;a. If the word is invalid, their letters will reset and it is still that player's turn 
5. Once the current player submits a valid word or passes their turn, it is the next player's turn 

## Buttons 
Pass - skips the current player's turn and goes to the other player's    
Current Dir - shows the current direction of the word to be player. Click on this button to change the direction you would like the word to be played.    
Reset - resets any letters that have been placed on the play area    
Submit! - submits a word to be checked for validation and added to the board    

## Wildcards 
Wildcards (blanks) are indicated by the letters marked "\*". They will autmatically default to the first letter in the alphabet that spells a valid word (i.e. if I play B\*T with the intention of playing BET, it will default to BAT since A comes before E). Once a wildcard is set, it cannot be overridden. It will appear on the board as an "\*" but when you see the letter in the play area, it will be the actual letter. You do not get points for wildcards. 

## Validation Checks 
1. Check Center - checks that the first word plays goes through the center
2. Check Player's Letters - checks that the player used at least one letter before submitting 
3. Check Boundary - checks that the word submitted does not go out of bounds 
4. Check Intersect - checks if the word intersects with any letters already on the board 
5. Check Anchor - checks if the word is anchored on another word 
6. Check Adjacent Letters - checks if the word submitted has any letters next to letters already on the board and, if so, whether those letters spell a word independently. 

## Limitations 
1. Players will only get points for the word in the play area that they submit. They will not get points for new words that they spell with adjacent letters already on the board. 
2. There is no option to pick new letters. If the player cannot go, they must pass their turn. 