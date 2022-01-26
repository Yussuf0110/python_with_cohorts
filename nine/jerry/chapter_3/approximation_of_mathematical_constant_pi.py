# 3.14 (Challenge: Approximating the Mathematical Constant )
# Write a script that computes the value of π from the following infinite series.
# Print a table that shows the value of
# π approximated by one term of this series, by two terms, by three terms, and so on.
# How many terms of this series do you have to use before you first get 3.14? 3.141? 3.1415? 3.14159?


pi = 0
numerator = 4
denominator = 1
for i in range(200001):
    if i % 2 == 1:
        pi += -(numerator / denominator)
    else:
        pi += (numerator / denominator)
    denominator += 2
    print(f"{numerator}/{denominator}", end=" : ")
    print(f'{pi}')

print('Final value of pi is', pi)
