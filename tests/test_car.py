import pytest
from src import car

class TestCar:

    car_created = car.Car([0, 0], "N", "car")
    
    def test_valid_car(self):
        assert self.car_created.get_present_coordinates() == [0, 0] 
        assert self.car_created.get_direction() == "N"
        assert self.car_created.get_name() == "car"

    def test_set_name(self):
        self.car_created.set_name("car1")
        assert self.car_created.get_name() == "car1"

    def test_set_present_coordinates(self): 
        self.car_created.set_present_coordinates([1, 1])
        assert self.car_created.get_present_coordinates() == [1, 1]
    
    def test_set_old_coordinates(self): 
        self.car_created.set_old_coordinates([1, 1])
        assert self.car_created.get_old_coordinates() == [1, 1]

    def test_set_direction(self):   
        self.car_created.set_direction("E")
        assert self.car_created.get_direction() == "E"

    def test_str_method(self):
        car_two = car.Car([0, 0], "N", "car")
        assert car_two.__str__() == "car is at [0, 0] facing N."

    def test_invalid_car(self):
        with pytest.raises(ValueError, match = "Invalid coordinates given!") as excinfo:
            car.Car("a", "N", "car")
        with pytest.raises(ValueError, match = "Invalid coordinates given!") as excinfo:
            car.Car([0], "N", "car")
        with pytest.raises(ValueError, match = "Invalid direction given!") as excinfo:
            car.Car([0,1], "K", "car")

    def test_invalid_set_present_coordinates(self): 
        with pytest.raises(ValueError, match = "Invalid coordinates given!") as excinfo:
            self.car_created.set_present_coordinates([2])
    
    def test_invalid_set_old_coordinates(self): 
        with pytest.raises(ValueError, match = "Invalid coordinates given!") as excinfo:
            self.car_created.set_old_coordinates([1, 1, 1])

    def test_invalid_set_direction(self):   
        with pytest.raises(ValueError, match = "Invalid direction given!") as excinfo:
            self.car_created.set_direction("PP")

