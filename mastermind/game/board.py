import random
from game.roster import Roster
from game.player import Player

class Board:
    #The class "Board" contains the game elements, like a list of the player's assigned code, the gess and hint
    
    def __init__(self):
      
        self._player_items = []

    def prepare(self):
        #This function/method sets up the board with an entry for the current player.
        code = str(random.randint(1000, 9999))
        guess = "----"
        hint = "****"
        self._player_items.append([code, guess, hint])
        
    def _create_hint(self, code, guess):
        #This function/method generates a hint based on the given code and guess.
        hint = ""
        for index, letter in enumerate(guess):
            if code[index] == letter:
                hint += "x"
            elif letter in code:
                hint += "o"
            else:
                hint += "*"
        return hint

    def _set_player_items(self, player_index, guess, hint):
        #Sets the current player's guess and hint
         
        self._player_items[player_index][1] = guess
        self._player_items[player_index][2] = hint

    def _get_player_items(self, player_index):
        #this part of the code will give us the current player's code, guess, and hint

        return self._player_items[player_index]

    def display_board(self, roster):
        #Displays the current board in string format
        green = '\033[92m'
        blue = '\033[94m'
        end_color = '\033[0m'
        current_color = green

        board_string = '\n--------------------' 
        players = roster.get_roster()
        for player in players:
            index = players.index(player)
            #Now let's acces those index's
            guess = self._player_items[index][1]
            hint = self._player_items[index][2]

            if current_color == green:

                #We are switching to color blue if the first user's color is green
                current_color = blue
            else:
                current_color = green

            board_string += (f"\n{current_color}Player {player.get_name()}: {guess}, {hint}{end_color}")  
        board_string += '\n--------------------\n'
        return board_string
        



    