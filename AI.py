from Vhello import *
import sys

class AI_Vhello(object):
    """AI player for Vhello game engine"""

    def __init__(self, game, AI_player):
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
        score,move = self.min_max(self.game.board,0, -sys.maxsize-1 , sys.maxsize, self.AI_player)
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

    def positional_score(self, board):
        score = 0
        
        for col in range(0, 8):
            for row in range(0, 8):
                if board[row][col] == "B":
                    score = score + self.pos_value[row][col]
                elif board[row][col] == "W":
                    score = score - self.pos_value[row][col]

        return score


    def min_max(self, board, depth, alpja, beta, player):
        game_board = Vhello.pre_built(board, player)
        game_moves = game_board.get_possible_moves()

        if len(game_moves) == 0:
            return self.positional_score(board),None
        
        if self.max_depth !=0 and depth >= self.max_depth:#max_depth of 0 is to infinit depth
            return self.positional_score(board),None

        if player == game_board.B:#player win => max 
            v = -sys.maxsize -1
            move = board 

            for move in board:
                test_game = Vhello.pre_built(game_board.board , player)
                test_game.play(move[0], move[1])
                s, b = self.min_max(test_game.board, depth+1, alpha, beta,test_game.__get_opponent__(player))

                if s > v:
                    v = s
                    m = move
                alpha = max(alpha, v)
                if beta <= alpha:
                    break #beta prunning
                
            return v,m
        
        else:
            for move in board:
                test_game = Vhello.pre_built(game_board.board , player)
                test_game.play(move[0], move[1])
                s, b = self.min_max(test_game.board, depth+1, alpha, beta,test_game.__get_opponent__(player))

                if s < v:
                    v = s
                    m = move
                alpha = min(beta, v)
                if beta <= alpha:
                    break #beta prunning
                
            return v,m


class Greedy_AI(AI_Vhello):
    """Greedy in terms of flips for each turn. The more you can flip the better for that turn"""

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

            if self.__better_score__(best_move_score, test_move.score) == 1:
                best_move_score = test_move.score
                best_move = move
        return best_move

    def __better_score__(self, init_score, new_score):
        """TODO: remove this from here but for now depending if the player is White or Black the better score
                 would be negative or positive"""
        """  1 for new_score is better score
            -1 for new_score is not better score
             0 for Tie"""
        if self.AI_player == self.game.B:
            if new_score > init_score:
                return 1
            elif new_score < init_score:
                return -1
        else:
            if new_score < init_score:
                return 1
            elif new_score > init_score:
                return -1
        return 0


    