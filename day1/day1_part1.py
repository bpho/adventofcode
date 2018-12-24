#!/usr/bin/env python3

def calculate_resulting_frequency(input_file):
    freq = 0
    for lines in input_file:
        if lines[0] is '+':
            print("This is a positive value: {}".format(lines))
            freq += int(lines[1:])
        else:
            print("This is a negative value: {}".format(lines))
            freq -= int(lines[1:])
            
    return freq

if __name__ == '__main__':
    f = open("day1/input.txt")
    result_freq = calculate_resulting_frequency(f)
    print("Resulting frequency is: {}".format(result_freq))
    f.close()