class Guess:
    #The player's guess.
    
   
    def __init__(self):
      
        self.__guess = ''

    def set_guess(self, guess):
        #This function/method sets the player's guess for storage

        self.__guess = guess

    def get_guess(self):
        #This function/method gets the current player's guess
        return self.__guess 