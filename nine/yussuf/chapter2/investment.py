import math



interest_rate = 0.07
invested_amount = float(input('Enter amount invested '))
number_of_year_to_calculated = int(input('Enter number of years '))
calculate_interest = round(invested_amount * math.pow((1 + interest_rate),number_of_year_to_calculated),5)
print('The total interest on',invested_amount,'is',calculate_interest,'after',number_of_year_to_calculated,'year(s)')
