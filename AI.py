from Vhello import *
import sys

class AI_Vhello(object):
    """AI player for Othello game engine"""
    def __init__(self, game ,AI_player) -> None:
        self.game = game
        self.AI_player = AI_player
    
    def get_next_move(self):
        raise NotImplementedError("Inheritator forgot to implement this")
    
class Random_AI(AI_Vhello):
    def __init__(self, game, AI_player) -> None:
        super(Random_AI, self).__init__(game, AI_player)

    def get_next_move(self):
        return super().get_next_move()