from src import board, car, solve, readinput

def main():

    # part 1 logic
    print("\nTesting Part 1 logic")
    part_one_info = readinput.read_file("test_data_p1.txt")

    board_setup_p1 = readinput.setup_board(part_one_info[0])
    car_list_p1 = readinput.setup_cars(part_one_info[1:])

    # output result
    print("\n")
    print(solve.run_car_simulation(board_setup_p1, car_list_p1))
#----------------------------------------------------------------#

    # part 2 logic
    print("\nTesting Part 2 logic")
    part_two_info = readinput.read_file("test_data_p2.txt")

    board_setup_p2 = readinput.setup_board(part_two_info[0])
    car_list_p2 = readinput.setup_cars(part_two_info[1:])
    
    # output result
    print("\n")
    print(solve.multiple_car_collision(board_setup_p2, car_list_p2))




if __name__ == "__main__":
    main()      
