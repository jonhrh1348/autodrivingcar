import pytest
from src import board, solve, car, readinput
from src.log_config import configure_logger

logger = configure_logger(__name__)

class TestSolve:

    board_test = board.Board(10, 10)

    def test_add_or_update_car(self):
        car_test = car.Car([1, 2], "N", "A")
        grid = solve.add_or_update_car(self.board_test, car_test) 
        assert grid[7][1] == "A"

    def test_move_car(self):
        car_test = car.Car([0, 0], "N", "A")
        with pytest.raises(ValueError, match= "Invalid move given!") as excinfo:
            solve.move_car(self.board_test, car_test, "U") 

    def test_valid_car_move(self):
        assert solve.valid_car_move(self.board_test, 0, 0, "S") == [0, 0]
        assert solve.valid_car_move(self.board_test, 0, 1, "W") == [0, 1]
        assert solve.valid_car_move(self.board_test, 9, 9, "E") == [9, 9]
        assert solve.valid_car_move(self.board_test, 0, 9, "N") == [0, 9]

# to rework test cases
    def test_run_car_simulation(self):
        car_test = car.Car([1, 2], "N", "A")
        car_list = [[car_test, "FFRFFFRRLF"]]
        assert solve.run_car_simulation(self.board_test, car_list) == "4 3 S" 

    def test_multiple_car_collision_1(self):
        car_test = car.Car([1, 2], "N", "A")
        car_test_2 = car.Car([7, 8], "W", "B")
        car_list = [[car_test, "FFRFFFFRRL"], [car_test_2, "FFLFFFFFFF"]]
        line_one = f"A B \n5 4 \n7"

        assert solve.multiple_car_collision(self.board_test, car_list) == line_one

    def test_multiple_car_collision_2(self):
        car_test = car.Car([0, 0], "N", "A")
        car_test_2 = car.Car([9, 8], "W", "B")
        car_list = [[car_test, "FFRFFFFRRL"], [car_test_2, "FFRLLLFLRR"]]

        assert solve.multiple_car_collision(self.board_test, car_list) == "no collision"