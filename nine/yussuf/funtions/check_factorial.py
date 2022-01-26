def check_the_factorial(number):
    factorial = 1
    new_number = int(number)
    if new_number == 0: factorial = 1
    if new_number == 1: factorial = 1
    else:
        for i in range(new_number):
            factorial = factorial * new_number
            new_number-=1
    return factorial