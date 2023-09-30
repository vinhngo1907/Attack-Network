import numpy as np

class Vhello:
    W = 'W'
    B = 'B'
    row = 8
    col = 8
    BOARD_TOTAL_MOVES = row*col
    
    def __init__(self) -> None:
        self.__reset_board()
    
    @classmethod
    def pre_built(cls, board, turn):
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
    
    def get_possible_moves(self):
        playable = []

        for col in range(0, self.col):
            for row in range(0, self.row):
                if self.board[row][col] == " " and self.is_playable(col,row):
                    playable.append((col, row))
        return playable
    
    def __switch_turn_(self):
        return self.B if self.turn == self.w else self.W
    
    def out_of_bounds(self, col, row):
        return True if col < 0 or row < 0 or col > self.col or row > self.row else False

    def is_flipable(self, dir_col, dir_row, start_col, start_row, target):
        return
    
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
    

    def flip(self, dir_col, dir_row, start_col, start_row, title):
        row = start_row
        col = start_col

        #place point have tile in the position (col, row)
        self.__flip_vs_update__(col, row, title)

        #check out_of_bounds and next flip have tile diff with tile so flip this position
        while self.out_of_bounds(col, row) == False and self.board[row][col] != tile:
            self.__flip_vs_update__(col, row, title)
            row = row + dir_row
            col = col + dir_col
        
    def __flip_vs_update__(self, row, col, title):
        #check this position have same title 
        if self.board[row][col] == title:
            return