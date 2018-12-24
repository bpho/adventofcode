#!/usr/bin/env python3
"""
Challenges faced:
- When you keep a file opened and it loops through the entire file once, it doesn't
start at the beginning when you pass the file in again.. need to either manually 
'seek' from line 0 or close and re-open file
- Other solution is just to store the contents of the file in a list, reading it in memory
- After a file object is closed, either by a with statement or by calling f.close(), 
attempts to use the file object will automatically fail.
"""

global_set_of_frequencies = set()

def calculate_repeating_frequency(input_file, freq):
    start_freq = freq
    for lines in input_file:
        global_set_of_frequencies.add(start_freq)
        current_num = int(lines[1:])
        if lines[0] is '+':
            start_freq += current_num
        else:
            start_freq -= current_num
        
        if start_freq in global_set_of_frequencies:
            print("Found a repeating frequency: {}".format(start_freq))
            return True, start_freq
        
    return False, start_freq

if __name__ == '__main__':
    repeating_freq = False
    starting_freq = 0

    # Storing file contents in a list, can close file after
    with open("day1/input.txt") as file_object:
        file_lines = file_object.readlines()
    
    while repeating_freq is False:
        repeating_freq, starting_freq = calculate_repeating_frequency(file_lines, starting_freq)

    # Approach #2 to reading files and saving input in list
    # f = open("day1/input.txt")
    # file_lines = f.readlines()
    # f.close()
    # while repeating_freq is False:
    #     repeating_freq, starting_freq = calculate_repeating_frequency(file_lines, starting_freq)

    # Approach #3 reading files and pointing it back to beginning
    # f = open("day1/input.txt")
    # while repeating_freq is False:
    #     f.seek(0)
    #     repeating_freq, starting_freq = calculate_repeating_frequency(file_lines, starting_freq)
    # f.close()