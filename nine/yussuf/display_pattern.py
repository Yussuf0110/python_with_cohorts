def display_patternA(userInput):
    for i in range(1,userInput,1):
        for j in range(i):
            print(j+1,end=" ")
        print()
        
def display_patternB(userInput):
    for i in range(userInput,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
            
print(display_patternA(6))
print(display_patternB(5))