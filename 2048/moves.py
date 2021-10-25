from board import Board
from utility import Utility
from config import GRID_SIZE

class Moves:
    def __init__(self, board : Board):
        self.__board = board
        self.__utility = Utility()
    
    def move_right(self):
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.__board.get_tile(i, j).value != '_':
                    for k in range(GRID_SIZE - 1, j, -1):
                        if self.__board.get_tile(i, k).value == '_':
                            self.__board.get_tile(i, k).value = self.__board.get_tile(i, j).value
                            self.__board.get_tile(i, j).value = '_'
                            break

    def move_left(self):
        self.__utility.reverse_board(self.__board)
        self.move_right()
        self.__utility.reverse_board(self.__board)
        
    def move_up(self):
        self.__utility.transpose_Board(self.__board)
        self.move_left()
        self.__utility.transpose_Board(self.__board)

    def move_down(self):
        self.__utility.transpose_Board(self.__board)
        self.move_right()
        self.__utility.transpose_Board(self.__board)
