import pytest
from src import board

class TestBoard:

    def test_valid_board(self):
        board_set = board.Board(3, 3)
        assert board_set.get_grid() == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def test_invalid_board(self):
        with pytest.raises(ValueError, match= "Invalid width/height given!") as excinfo:
            board.Board(0, 3)

    def test_get_width(self):
        board_set = board.Board(2, 4)
        assert board_set.get_width() == 2
    
    def test_get_height(self):
        board_set = board.Board(3, 5)
        assert board_set.get_height() == 5