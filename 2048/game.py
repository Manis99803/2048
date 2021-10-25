from board import Board, MergeBoardTiles
from utility import Utility
from config import Direction
from moves import Moves

class GameManager:
    def __init__(self):
        self.__board = Board()
        self.__moves = Moves(self.__board)
        self.__merge_board_tile = MergeBoardTiles(self.__board)
        self.__direction = [Direction.LEFT, Direction.RIGHT, Direction.TOP, Direction.BOTTOM]
        self.__utility = Utility()

    def start_game(self):
        print("Starting the Game")
        
        self.__board.print_board()
        while (not self.__board.check_board_status()) or (not self.__board.check_game_won()):
            for d in Direction:
                print(f'{d.name} : {d.value}')
            index = int(input("Enter direction in which you want to move the: "))

            direction = self.__direction[index]

            if direction == Direction.RIGHT:
                self.__moves.move_right()
                self.__merge_board_tile.merge_horizontal_tiles(direction)
                self.__moves.move_right()

            elif direction == Direction.LEFT:
                self.__moves.move_left()
                self.__merge_board_tile.merge_horizontal_tiles(direction)
                self.__moves.move_left()

            elif direction == Direction.TOP:
                self.__moves.move_up()
                self.__merge_board_tile.merge_vertical_tiles(direction)
                self.__moves.move_up()

            else:
                self.__moves.move_down()
                self.__merge_board_tile.merge_vertical_tiles(direction)
                self.__moves.move_down()

            self.__utility.add_tile(self.__board)
            self.__board.print_board()

game_manager = GameManager()
game_manager.start_game()
