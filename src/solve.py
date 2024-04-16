from src import board, car, log_config, readinput
from src.log_config import configure_logger
import copy

logger = configure_logger(__name__)

def add_or_update_car(board, car):
    #x refers to coordinate on x-axis, y is for y-axis

    x = car.get_present_coordinates()[0]
    y = car.get_present_coordinates()[1]
    old_x = car.get_old_coordinates()[0]
    old_y = car.get_old_coordinates()[1]

    # car should be in coordintes(x,y) which corresponds to board[-y-1][x]. This is because the first index refers to the y-coordinate, 
    # then the 2nd index refers to the x-coordinate which is contained inside the 1st list.
    board.grid[-old_y-1][old_x] = 0

    if board.grid[-y-1][x] != 0:
        return (board.grid[-y-1][x], car.get_name(), [x, y])   # store the tuple with 2 collidng car names, 3rd entry is the coordinates
    else:
        board.grid[-y-1][x] = car.get_name()
    
    return board.get_grid() # return the board state if there are no collisions after a move

def move_car(board, car, move):
    x, y = car.get_present_coordinates()[0], car.get_present_coordinates()[1]
    direction = car.get_direction()

    if move == "L" or move == "R":  # rotate car left/right
        old_direction = direction
        direction = turn_car(direction, move)
        car.set_direction(direction)

        logger.info(f' Car: {car.get_name()}, Present Coordinates:{car.get_present_coordinates()}, Present Direction: {car.get_direction()}, Old Direction: {old_direction}')

    elif move == "F":  # move car forward
        old_coordinates = car.get_present_coordinates()
        car.set_old_coordinates(old_coordinates)

        present_coordinates = valid_car_move(board, x, y, direction)
        car.set_present_coordinates(present_coordinates)

        update_board = add_or_update_car(board, car)

        logger.info(f' Car: {car.get_name()}, Present Coordinates:{car.get_present_coordinates()}, Old Coordinates:{car.get_old_coordinates()}, Present Direction: {car.get_direction()}')

        if type(update_board) == tuple:
            return update_board

    else:
        raise ValueError("Invalid move given!")

def valid_car_move(board, x, y, direction):
    match direction:
        case "E":
            if x + 1 > board.width - 1:  # prevent car from going out of bounds when at the edge of the board
                pass
            else:
                x += 1
        case "N":
            if y + 1 > board.height - 1:
                pass
            else:
                y += 1
        case "W":
            if x - 1 < 0:
                pass
            else:
                x -= 1
        case "S":
            if y - 1 < 0:
                pass
            else:
                y -= 1
    
    return [x, y]

def turn_car(direction, move):
    list_of_directions = ("N", "E", "S", "W")

    position = list_of_directions.index(direction)
    
    #car turns left/right, will follow the list to traverse left/right for new facing direction
    if move == "L":
        position -= 1
        if position < 0:
            position = 3

    elif move == "R":
        position += 1
        if position > 3:
            position = 0

    direction = list_of_directions[position]
    return direction      

# used for single car in part 1
def run_car_simulation(board, car_list):
    car = car_list[0][0]
    add_or_update_car(board, car)
    moves = car_list[0][1]

    for char in moves:
        current_move = move_car(board, car, char)

    answer = f"{car.get_present_coordinates()[0]} {car.get_present_coordinates()[1]} {car.get_direction()}"  
    logger.info(answer)
    return answer
    

# used for multiple cars in part 2
def multiple_car_collision(board, car_list):
    # collision logic, if have, print (cars, coordinates, step) else print no collision (to rework due to wrong output)

    for i in range(0, len(car_list)):
        for j in range(i+1, len(car_list)):

            # Get the car objects and their moves, create a deep copy of the object instead for collision checks, to prevent list mutation during each i, j loop
            first_car, first_car_moves = copy.deepcopy(car_list[i])
            second_car, second_car_moves = copy.deepcopy(car_list[j])

            add_or_update_car(board, first_car)
            add_or_update_car(board, second_car)
            min_moves = min(len(first_car_moves), len(second_car_moves))

            for k in range(0, min_moves):
                first_car_move = first_car_moves[k]
                second_car_move = second_car_moves[k]

                # first car will move, do not check as we simulate second car moving at the same time, check for collision only when second car moves into same coordinates
                move_car(board, first_car, first_car_move)
                collison_check = move_car(board, second_car, second_car_move)
                
                # 1st 2 entries of tuple are the colliding car names, 3rd entry is the coordinates of collision, 
                # last entry is the step where collision happened
                if type(collison_check) == tuple:
                    line_one = f"{collison_check[0]} {collison_check[1]} \n{collison_check[2][0]} {collison_check[2][1]} \n{k+1}"
                    logger.info(line_one)
                    return line_one

            board = readinput.setup_board([board.get_width(), board.get_height()]) # reset the board for the next pair of cars
            
    return "no collision"
