import pytest
from src import readinput, board, car, solve
from src.log_config import configure_logger

logger = configure_logger(__name__)

class TestReadInput:

    # test the 2 spaces condition
    def test_read_file_1(self):
        assert readinput.read_file("test_data_p1.txt") == [['10', '10'], ['1', '2', 'N', 'Car', 'FFRFFFRRLF']]

    # test the empty line condition
    def test_read_file_2(self):
        assert readinput.read_file("test_data_p2.txt") == [['10', '10'], ['1', '2', 'N', 'A', 'FFRFFFFRRL'], ['0', '4', 'S', 'C', 'RFFFFRRL'],
         ['7', '8', 'W', 'B', 'FFLFFFFFFF'], ['6', '6', 'E', 'D', 'FFLFFFRFL']]

        # test the empty line condition
    def test_read_file_3(self):
        with pytest.raises(ValueError, match= "The line should be either empty or contain 3 values. Please check the input file.") as excinfo:
            readinput.read_file("test_invalid_input.txt")

    def test_setup_board(self):
        final_board = readinput.setup_board(['3','3'])
        assert final_board.get_grid() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert final_board.width == 3
        assert final_board.height == 3

    def test_setup_car(self):   
        car_list = readinput.setup_cars([["1", "2", "N", "A", "FFRFFFRRLF"]])
        assert car_list[0][0].get_name() == "A" 
        assert car_list[0][0].get_present_coordinates() == [1, 2]
        assert car_list[0][0].get_direction() == "N"
        assert car_list[0][1] == "FFRFFFRRLF"

