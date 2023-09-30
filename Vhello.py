import numpy as np

class Vhello:
    W = 'W'
    B = 'B'
    row = 8
    col = 8
    BOARD_TOTAL_MOVES = row*col
    
    def __init__(self):
        self.__reset_board()

    @classmethod
    def pre_built(cls, board, turn):
        """When you have a setup you want to load"""
        """TODO: Later with board being changable will require a verifier"""

        new_game = cls()
        new_game.__reset_board__()
        new_game.board = [[board[col][row] for row in range(new_game.row)] for col in range(new_game.col)]
        new_game.turn = turn
        new_game.__recount_score__()
    
    def count_titles(self, title):
        count = 0
        for row in self.board:
            for val in row:
                if val == title:
                    count = count + 1
        return count
    
    def __recount_score__(self):
        self.board = [[' ' for row in range(self.row)] for col in range(self.col)]
        self.board[3][4] = self.B
        self.board[3][3] = self.W
        self.board[4][3] = self.B
        self.board[4][4] = self.W

        self.cur_moves = 4
        self.history = []
        self.turn = self.B

        self.scoreB = 2
        self.coreW = 2

    def __reset_board__(self):
        self.board = [[' ' for row in range(self.row)] for col in range(self.col)]
        self.board[3][4] = self.B
        self.board[3][3] = self.W
        self.board[4][3] = self.B
        self.board[4][4] = self.W

        self.cur_moves = 4
        self.history = []
        self.turn = self.B


        #init state have 2 black and 2 write
        self.scoreB = 2
        self.scoreW = 2

    def __printBoard__(self):
        s = "    0   1   2   3   4   5   6   7   \n"
        s= s + "------------------------------------\n"
        i=0
        for row in self.board:
            s = s + str(i) + " | "
            for loc in row:
                s = s + loc + " | "
            s = s + "\n"
            i = i + 1
        s = s + "------------------------------------\n"
        return s
    
    def __get_history__(self, display_board):
        hist = self.history
        self.__reset_board__()

        print("History of game: ")

        if display_board:
            print(self)
        
        while list:
            col, row = hist.pop()
            print(self.turn + " play at col: "+str(col)+ "row: "+str(row))
            self.play(col,row)
            if display_board:
                print(self)
    
    def __get_opponent__(self, player):
        return self.W if player == self.B else self.B
    
    def __switch_turn_(self):
        return self.B if self.turn == self.w else self.W
    
    def play(self, col, row):
        if self.is_playable(col, row) == False:
            return
        for dir_col in range(-1, 2):
            for dir_row in range(-1, 2):
                if dir_col != 0 or dir_row != 0:
                    if self.is_flipable(dir_col, dir_row, col, row, self.turn):
                        """
                            |*|*|*|
                            |*|W|*|
                            |*|*|*|
                            === * is check flip arround (col,row) when function play(col,row) run
                        """
                        self.flip(dir_col, dir_row, col, row, self.turn)
    
    def get_possible_moves(self):
        playable = []

        for col in range(0, self.col):
            for row in range(0, self.row):
                if self.board[row][col] == " " and self.is_playable(col,row):
                    playable.append((col, row))
        return playable

    def is_flipable(self, dir_col, dir_row, start_col, start_row, target):
        if target == self.W:
            jump = self.B
        else:
            jump = self.W

        row = start_row + dir_row
        col = start_col + dir_col

        #######################################################
        #check point in the board have different target example
        #       |W|B|
        #       |B|W|B| -> check if cannot flip return false check point next
        #       have no sample point current
        ########################################################        
        if self.out_of_bounds(col, row) or self.board[row][col] != jump:
            return False
        
        while True:
            if self.out_of_bounds(col, row) or self.board[row][col] == " ":
                return False
            
            if self.board[row][col] == target:
                return True

            col = col + dir_col
            row = row + dir_row
            
        #certainly
        return False
    
    def is_playable(self, row, col):
        if self.out_of_bounds(col, row):
            return False
        if self.board[row][col] == " ":
            return False
        for dir_col in range(-1, 2):
            for dir_row in range(-1, 2):
                if self.is_flipable(dir_col, dir_row, col, row, self.turn):
                    return True
        return False
        
    def game_finished(self):
        return True if self.cur_moves == self.BOARD_TOTAL_MOVES else False
    
    def out_of_bounds(self, col, row):
        return True if col < 0 or row < 0 or col > self.col or row > self.row else False
    
    def flip(self, dir_col, dir_row, start_col, start_row, title):
        row = start_row
        col = start_col

        #place point have tile in the position (col, row)
        self.__flip_vs_update__(col, row, title)

        #check out_of_bounds and next flip have tile diff with tile so flip this position
        while self.out_of_bounds(col, row) == False and self.board[row][col] != title:
            self.__flip_vs_update__(col, row, title)
            row = row + dir_row
            col = col + dir_col
    
    def __flip_vs_update__(self, row, col, title):
        #check this position have same title 
        if self.board[row][col] == title:
            return
        
        #
        if self.board[row][col] == self.B:
            #switch from B to W
            self.scoreW = self.scoreW + 1
            self.scoreB = self.scoreB - 1
        elif self.board[row][col] == self.W:
            #switch from W to B
            self.scoreW = self.scoreW - 1
            self.scoreB = self.scoreB + 1
        else:
            # board[row][col] == " " no tile in this point
            if title == self.B:
                self.scoreB = self.scoreB + 1 
            else:
                self.scoreW = self.scoreW - 1
            
        #change tile for this point
        self.board[row][col] = title