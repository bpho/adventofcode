#!/usr/bin/env python3
def create_character_breakdown(file_lines):
    character_dict = {}
    for characters in file_lines:
        if characters not in character_dict:
            character_dict[characters] = 1
        else:
            character_dict[characters] += 1
    
    return character_dict

def calculate_check_sum(file_lines):
    character_dict = {}
    valid_word_count_two = 0
    valid_word_count_three = 0
    for line in file_lines:
        character_dict = create_character_breakdown(line)
        
        if string_is_valid_with_n_occurences(character_dict, 2):
            valid_word_count_two += 1
        
        if string_is_valid_with_n_occurences(character_dict, 3):
            valid_word_count_three += 1

    return valid_word_count_two * valid_word_count_three

# Checks if n occurences exist 
def string_is_valid_with_n_occurences(char_dict, occurences):
    if occurences in char_dict.values():
        return True
    else:
        return False

if __name__ == '__main__':
    f = open("day2/input.txt")
    file_lines = f.readlines()
    f.close()

    check_sum = calculate_check_sum(file_lines)
    print(check_sum)