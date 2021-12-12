class Roster:
    #This Roster class contains a collection of players. The responsibility of Roster is to keep track of the players

    def __init__(self):

        self.current = 0
        self.players = []
        
    def add_player(self, player):
        #This function/method adds the given player to the roster
        if player not in self.players:
            self.players.append(player)

    def get_current(self):
        #This function/method gets the current player object.

        return self.players[self.current]
    
    def next_player(self):
        #This function/method advances the turn to the next player.
        self.current = (self.current + 1) % len(self.players)

    def get_roster(self):
        #This function/method gets the current roster.
        return self.players