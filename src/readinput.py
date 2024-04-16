from src import board, car, log_config
from src.log_config import configure_logger

logger = configure_logger(__name__)

# may need to move
def read_file(file_name):

    logger.info(f" Reading file: {file_name}")
    file = open(file_name, "r")
    info_list = []

    # calculate number of lines
    with open(file_name, "r") as fp:
        length = sum(1 for line in fp)
        logger.info(f" Number of lines in the file: {length}")

    # first line is to read & define board size
    first_line = file.readline()
    size = first_line.split()

    for i in range(2, length):
        line = file.readline() 

        if(line == "\n"):
            result = list(filter(None, map(lambda line: line.strip(), file.readlines())))
            info_list = read_car_entries(result)
            break;

        elif(line.count(" ") == 2 ):
            car_data = line.split()
            car_data.append("Car")

            nextline = file.readline().strip()
            car_data.append(nextline)
            info_list.append(car_data)

            i += 1
        else:
            raise ValueError("The line should be either empty or contain 3 values. Please check the input file.")

    file.close()  

    width = size[0]
    height = size[1]
    info_list.insert(0, [width, height]) # insert board size in front of list
    
    logger.info(f" Board and Car Information: {info_list} ")
    return info_list

def read_car_entries(result):
    final_result = []

    if len(result) % 3 != 0:
        raise ValueError("There should be 3 lines for each car entry. Please check the input file.")

    for i in range(0, len(result)):
        if i % 3 == 1:
            car_data = result[i].split()
            car_data.append(result[i-1])  # add name of car
            car_data.append(result[i+1])  # add list of moves for the car

            final_result.append(car_data)
    return final_result
            
def setup_board(boardsize):
    width = boardsize[0]
    height = boardsize[1]

    board_set = board.Board(int(width), int(height))
    return board_set

def setup_cars(car_data):
    car_list = []

    for i in range(0, len(car_data)):
        car_info = car_data[i]
        car_created = car.Car([int(car_info[0]), int(car_info[1])], car_info[2], car_info[3]) # create the car with its present coordinates, direction and name
        logger.info(f" Car created: {car_created}")
        car_list.append([car_created, car_info[4]])

    return car_list