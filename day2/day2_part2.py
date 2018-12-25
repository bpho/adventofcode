#!/usr/bin/env python3
"""
Challenges:
- Not the most efficient solution... O(kn^2)
- Possible solutions... using a set and determining differences (^) in characters
- Could also utilize python libraries that will check for similar strings
"""

def find_common_box_ids(file_lines):
    for index, lines in enumerate(file_lines):
        for match_lines in file_lines[index+1:]:
            print("Lines: {}, Match Lines: {}".format(lines, match_lines))
            index_returned = is_one_character_difference(lines, match_lines)
            if index_returned:
                return lines, match_lines, index_returned

def is_one_character_difference(first_id, second_id):
    different_char_count = 0
    index_where_different = 0
    for index in range(0, len(first_id)-1):
        if first_id[index] != second_id[index]:
            different_char_count += 1
            index_where_different = index

        if different_char_count > 1:
            return False
    
    return index_where_different

if __name__ == '__main__':
    f = open("day2/input.txt")
    file_lines = f.readlines()
    stripped_file_lines = [lines.rstrip() for lines in file_lines]
    f.close()

    first_str, second_str, index = find_common_box_ids(stripped_file_lines)
    common_id = first_str[:index] + first_str[index+1:]
    print("The two closest ids are: {} and {} at index {}".format(first_str, second_str, index))
    print("The common string is: {}".format(common_id))
