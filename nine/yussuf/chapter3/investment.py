import math

interest_rate = 0.07
invested_amount = float(input('Enter amount invested '))
number_of_year_to_calculated = int(input('Enter number of years '))

for i in range(number_of_year_to_calculated):
    calculate_interest = round(invested_amount * math.pow((1 + interest_rate),i),5)
    print(i,calculate_interest)