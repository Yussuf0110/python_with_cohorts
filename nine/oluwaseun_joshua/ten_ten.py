player_one=input("Enter the correct foot either leftfoot or rightfoot: ")
player_two=input("Enter the correct foot either leftfoot or rightfoot: ")

player_one_score=0
player_two_score=0

if(player_one=="rightfoot" and player_two=="leftfoot"):
    print("player one won")
    player_one_score +=1

elif(player_two=="rightfoot" and player_one == "leftfoot"):
    print("player two win")
    player_two_score +=1

elif(player_one==player_two):
    print("it a draw")


print("The score of player_one is  ",player_one_score)
print("The score of player_two is  ",player_two_score)