import math
from math import pi
def max_count_char(input_str):
    max_count = 0
    max_char = ''

    for char in input_str:
        if char != max_char:
            if input_str.count(char) >= max_count:
                max_count = input_str.count(char)
                max_char = char
        else:
            continue

    return max_char