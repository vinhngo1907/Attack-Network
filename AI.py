from Vhello import *
import sys

class AI_Vhello(object):
    """AI player for Othello game engine"""
    def __init__(self, game ,AI_player):
        self.game = game
        self.AI_player = AI_player
    
    def get_next_move(self):
        raise NotImplementedError("Inheritator forgot to implement this")
    
class Random_AI(AI_Vhello):
    def __init__(self, game, AI_player):
        super(Random_AI, self).__init__(game, AI_player)

    def get_next_move(self):
        game_board = Vhello.pre_built(self.game.board, self.AI_player)
        game_moves = game_board.get_possible_moves()
        # return tupple (col,row)
        return game_moves[0]

class Minmax_AI(AI_Vhello):
    """Minmax using heuristic"""

    def __init__(self, game, AI_player, max_depth = 5):
        super(Minmax_AI, self).__init__(game, AI_player)
        self.max_depth = max_depth

    def get_next_move(self):
        score,move = self.min_max(self.game.board, 0, -sys.maxsize-1 , sys.maxsize, self.AI_player)
        return move
    
    pos_value =[
        [100, -1, 5, 2, 2, 5, -1, 100],
        [-1, -20, 1, 1, 1, 1, -20, -1],
        [ 5,   1, 1, 1, 1, 1,  1,  1 ],
        [ 2,   1, 1, 0, 0, 1,  1,  2 ],
        [ 2,   1, 1, 0, 0, 1,  1,  2 ],
        [ 5,   1, 1, 1, 1, 1,  1,  1 ],
        [-1, -20, 1, 1, 1, 1, -20, -1],
        [100, -1, 5, 2, 2, 5, -1, 100]
    ]

class Greedy_AI(AI_Vhello):
    def __init__(self, game, AI_player):
        """TODO: Not great to get the game as this shouldn't be changing anything"""
        super(Greedy_AI, self).__init__(game, AI_player)
    
    def get_next_move(self):
        possible_moves = self.game.get_possible_moves()
        best_move_score = self.game.score #Set to current initial score, Assumption that moves will always be better
        best_move = () #empty tuple to store best move
        print("possible moves: ", possible_moves)

        for move in possible_moves:
            col = move[0]
            row = move[1]
            
            test_move = Vhello.pre_built(self.game.board, self.AI_player)
            test_move.play(col, row)

        return super().get_next_move()
        