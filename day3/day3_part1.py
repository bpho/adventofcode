#!/usr/bin/env python3
"""
Each tuple on the fabric has a counter, if counter > 2 it's overlapped
Ex: 
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
x = 1, y = 3
at {(2, 4): 1, (3, 4): 2, (4, 4): 0, (5, 4): 2
   (2, 5): 0, (3, 5): 1, (4, 5): 1, (5, 5): 1} etc.. would have a count
For all with a count > 2, this indicates overlapping fabric so that would be a
square inch 
"""

fabric_board = {}

def add_to_fabric_board(file_lines):
    for lines in file_lines:
        sections = lines.split()
        starting_positions = sections[2].split(',')
        x = int(starting_positions[0]) + 1
        y = int(starting_positions[1].rstrip(':')) + 1
        dimensions = sections[3].split('x')
        width = int(dimensions[0])
        height = int(dimensions[1])
        print("Sections: {} with x: {}, y: {}, width: {}, height: {}".format(sections, x, y, width, height))
        create_tuples(x, y, width, height)

def create_tuples(start_x, start_y, width, height):
    x = start_x
    y = start_y
    for width_index in range(0, width):
        for height_index in range(0, height):
            if (x+width_index, y+height_index) not in fabric_board:
                fabric_board[(x+width_index, y+height_index)] = 1
            else: 
                fabric_board[(x+width_index, y+height_index)] += 1
    
    return None

def square_inches_overlapped(fabric_board):
    square_inches = 0
    for values in fabric_board.values():
        if values > 1:
            square_inches += 1

    return square_inches

if __name__ == '__main__':
    f = open("day3/input.txt")
    file_lines = f.readlines()
    f.close()

    add_to_fabric_board(file_lines)
    final_sq_inches = square_inches_overlapped(fabric_board)
    print(final_sq_inches)