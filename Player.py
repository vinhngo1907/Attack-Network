class Player(object):
    """Abstract Method to define rules for Players are Human or Computer inherent"""
    def __init__(self, game, player):
        self.game = game
        self.player = player

        def play(self):
            raise NotImplementedError("Inheritator forgot to implement this")

#class Human inherent from abstract class Player
class Human(Player):
    def __init__(self, game, player):
        #child inherent from parent 
        super(Human, self).__init__(game, player)
    
    #overrite function play
    def play(self):
        print("Player "+ self.player + " turn to play!")
        possible_moves = self.game.get_possible_moves()
        print("Possible moves: " + str(possible_moves))
        
        if len(possible_moves) == 0:
            print("No moves possible!")
            return 1

        col = int(input("Select column"))
        row = int(input("Select row"))

        print("Player: ", self.player, " Playing: col = "+ str(col) + " row = "+ str(row))
        self.game.play(col, row)
        return 0

class Computer(Player):

    def __init__(self, game, player, AI):
        super(Computer, self).__init__(game, player)
        self.AI = AI

    
    def play(self):
        possible_moves = self.game.get_possible_moves()
        if len(possible_moves) == 0:
            print("No moves possible!")
            return 1

        move = self.AI.get_next_move()
        col = move[0]
        row = move[1]

        print("Computer: "+ self.player," Playing: col = "+ str(col) + " row = "+ str(row) )
        self.game.play(col, row)
        return 0