import random
from config import GRID_SIZE

class Utility:
    def __init__(self):
        pass
    
    def transpose_Board(self, board):
        for i in range(GRID_SIZE):
            for j in range(i + 1, GRID_SIZE):
                tile_value = int()
                tile_value = board.get_tile(j, i).value
                board.get_tile(j, i).value = board.get_tile(i, j).value
                board.get_tile(i, j).value = tile_value

    def reverse_board(self, board):
        for i in range(GRID_SIZE):
            j = 0
            k = GRID_SIZE - 1
            while j < k:
                tile_value = int()
                tile_value = board.get_tile(i, j).value
                board.get_tile(i, j).value = board.get_tile(i, k).value
                board.get_tile(i, k).value = tile_value
                j += 1
                k -= 1

    def add_tile(self, board):
        while True:
            x = random.randint(0, 3)
            y = random.randint(0, 3)

            if board.get_tile(x, y).value == "_":
                board.get_tile(x, y).value = 2
                break
