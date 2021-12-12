class Player:
    #This class will help us with anyone who is taking part in a game, the responsibility of Player is to keep track of their identity and last move

    def __init__(self, name):
 
        self._name = name

    def get_name(self):
        #This function/method returns the player's name.
        return self._name