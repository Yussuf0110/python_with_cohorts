from nine.yussuf.methods.find_largest_and_smallest import find_largest_among3_integer, find_largest_among5_integer, find_smallest_among5_integer

first_Input = int(input("Enter number "))
second_Input = int(input("Enter number "))
third_Input = int(input("Enter number "))
fourth_Input = int(input("Enter number "))
fifth_Input = int(input("Enter number "))

smallest = find_smallest_among5_integer(first_Input,second_Input,third_Input,fourth_Input,fifth_Input)
largest = find_largest_among5_integer(first_Input,second_Input,third_Input,fourth_Input,fifth_Input)
ex = find_largest_among3_integer(first_Input,second_Input,third_Input)

print("The largest is ",largest)
print("The smallest is ",smallest)
print(ex)