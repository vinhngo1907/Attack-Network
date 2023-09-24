class Player(object):
    """Abstract Method to define rules for Players are Humman or Computer inherent"""
    def __init__(self, game, player):
        self.game = game
        self.player = player

        def play(self):
            raise NotImplementedError("Inheritator forgot to implement this")
        
#class Humman inherent from abstract class player
class Humman(Player):
    def __init__(self, game, player):
        super().__init__(game, player)
    
    #overrite function play
    def play(self):
        print("Player "+self.player+" turn to play!")
        possible_moves = self.game.get_possible_moves()
        print("Possible moves: " + str(possible_moves))
        