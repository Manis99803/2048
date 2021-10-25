from config import GRID_SIZE, Direction
from tile import Tile
from utility import Utility

class Board:
    def __init__(self):
        self.__board = []
        for i in range(GRID_SIZE):
            self.__board.append([])
            for j in range(GRID_SIZE):
                self.__board[i].append(Tile(i, j))

        self.__board[1][1].value = 2
        self.__board[3][1].value = 2

    def get_tile(self, i, j):
        return self.__board[i][j]

    def check_game_won(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.__board[i][j].value == 2048:
                    return True
        return False
    
    def check_board_status(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.__board[i][j].value == "_":
                    return True
        return False

    def print_board(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                print(self.get_tile(i, j).value, end = " ")
            print()
        print()

class MergeBoardTiles:
    def __init__(self, board : Board):
        self.__board = board
        self.__utility = Utility()

    def merge_horizontal_tiles(self, direction):
        if direction == Direction.LEFT:
            self.__utility.reverse_board(self.__board)
        for i in range(GRID_SIZE - 1, -1, -1):
            for j in range(GRID_SIZE - 1, 0, -1):
                if self.__board.get_tile(i, j).value == self.__board.get_tile(i, j - 1).value \
                    and self.__board.get_tile(i, j).value != '_':
                    self.__board.get_tile(i, j).value += self.__board.get_tile(i, j).value
                    self.__board.get_tile(i, j - 1).value = "_"
        if direction == Direction.LEFT:
            self.__utility.reverse_board(self.__board)

    def merge_vertical_tiles(self, direction):
        # if direction == 
        for i in range(GRID_SIZE - 1, 0, -1):
            for j in range(GRID_SIZE - 1, -1, -1):
                if self.__board.get_tile(i,j).value  == self.__board.get_tile(i - 1, j).value \
                    and self.__board.get_tile(i, j).value != '_':
                    self.__board.get_tile(i,j).value += self.__board.get_tile(i, j).value
                    self.__board.get_tile(i - 1, j).value = "_"


