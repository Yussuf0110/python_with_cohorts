# name = 'yussuf'
# name_capitalize = name.capitalize()
# big_name = name.upper()
# lower_name = big_name.lower()
# print(name_capitalize)
# print(big_name)
# print(lower_name)
# sng = [2,3,4,5,6,7,8,1]
# print(len(sng))

list_of_names = ['Helen','Pauuuuul','Saka', 'Holyf', 'Smith']
print(len(list_of_names[3]))
print(max(list_of_names,key=len))
print(min(list_of_names,key=len))

for i in range(len(list_of_names)):
    if len(list_of_names[i]) == 5:
        print(list_of_names[i])
        
class_a = ['Helen','Paul','Joe','Ruger','Motunrayo']
class_b = ['David','Johnson','Esther','Mufobi','John']

max_a = max(class_a,key=len)
max_b = max(class_b,key=len)
min_a = min(class_a,key=len)
min_b = min(class_b,key=len)

if len(max_a) > len(max_b): print('Class A has the longest:',max_a)
elif len(max_b) > len(max_a): print('Class B has the longest:',max_b)
else: print ('Equal')

if len(min_a) < len(min_b): print('Class A has the smallest:',min_a)
elif len(min_b) < len(min_a): print('Class B has the smallest:',min_b)
else: print ('Equal')
