
class Car:

    def __init__(self, present_coordinates, direction, name= "Car"):
        if(type(present_coordinates) != list or len(present_coordinates) != 2):
            raise ValueError("Invalid coordinates given!")
        elif direction not in ("N", "E", "S", "W"):
            raise ValueError("Invalid direction given!")
        else:
            self.present_coordinates = present_coordinates
            self.old_coordinates = [0,0]
            self.direction = direction
            self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_present_coordinates(self, present_coordinates): 
        if(type(present_coordinates) != list or len(present_coordinates) != 2):
            raise ValueError("Invalid coordinates given!")
        else:
            self.present_coordinates = present_coordinates

    def get_present_coordinates(self):
        return self.present_coordinates

    def set_old_coordinates(self, old_coordinates): 
        if(type(old_coordinates) != list or len(old_coordinates) != 2):
            raise ValueError("Invalid coordinates given!")
        else:
            self.old_coordinates = old_coordinates

    def get_old_coordinates(self):
        return self.old_coordinates
    
    def set_direction(self, direction):
        if direction not in ("N", "E", "S", "W"):
            raise ValueError("Invalid direction given!")
        else:
            self.direction = direction

    def get_direction(self):
        return self.direction

    def __str__(self):
        return f'{self.name} is at {self.present_coordinates} facing {self.direction}.'