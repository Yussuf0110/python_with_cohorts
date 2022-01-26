from nine.yussuf.funtions.find_largest_and_smallest import find_largest_among3_integer, find_smallest_among3_integer


first_input = int(input("Enter number: "))
second_input = int(input("Enter number: "))
third_input = int(input("Enter number: "))

sum = first_input + second_input + third_input
average = sum / 3
product = first_input * second_input * third_input

print("The sum is ",sum)
print("The average is ",average)
print("The product is ",product)
print("The smallest is ",find_smallest_among3_integer(first_input,second_input,third_input))
print("The largest is ",find_largest_among3_integer(first_input,second_input,third_input))