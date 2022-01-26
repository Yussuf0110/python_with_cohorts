def find_smallest_among5_integer(first_Number,second_Number,third_Number,fourth_Number,fifth_Number):
    smallest = first_Number
    if second_Number < smallest: smallest = second_Number
    if third_Number < smallest: smallest = third_Number
    if fourth_Number < smallest: smallest = fourth_Number
    if fifth_Number < smallest: smallest = fifth_Number
    return smallest

def find_largest_among5_integer(first_Number,second_Number,third_Number,fourth_Number,fifth_Number):
    largest = first_Number
    if second_Number > largest: largest = second_Number
    if third_Number > largest: largest = third_Number
    if fourth_Number > largest: largest = fourth_Number
    if fifth_Number > largest: largest = fifth_Number
    return largest

def find_smallest_among3_integer(first_Number,second_Number,third_Number):
    smallest = first_Number
    if second_Number < smallest: smallest = second_Number
    if third_Number < smallest: smallest = third_Number
    return smallest

def find_largest_among3_integer(first_Number,second_Number,third_Number):
    largest = first_Number
    if second_Number > largest: largest = second_Number
    if third_Number > largest: largest = third_Number
    return largest