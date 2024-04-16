class Board:
    
    def __init__(self, width: int, height: int):
        grid = []
        # Note: This is a simple implementation of a board with a 2D list.
        # Bottom left (height-1, 0) in the nested list corresponds to coordinates(0,0) in a 10x10 board
        # Top right (0, width-1) in the nested list corresponds to coordinates(9, 9) in a 10x10 board

        if width < 1 or height < 1:
            raise ValueError("Invalid width/height given!")

        for i in range(height):
            grid.append([])
            for j in range(width):
                grid[i].append(0)
        self.grid = grid
        self.width = width
        self.height = height

    def get_grid(self):
        return self.grid

    def get_width(self):
        return self.width

    def get_height(self):   
        return self.height
        
