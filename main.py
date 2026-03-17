import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

computer = random.choice ([-1, 0, 1])
youstr = input("Enter your choice (s, w, g) : ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1 : "Snake" , 0 : "Gun" , -1 : "Water"}

you = youdict[youstr]

print (f"You Choose : {reversedict[you]} \nComputer Choose : {reversedict[computer]}")

if (computer == you):
    print ("Draw")
else:
    if (computer == -1 and you == 1):
        print ("You Win")

    elif (computer == -1 and you == 0):
        print ("You Lose")

    elif (computer == 1 and you == -1):
        print ("You Lose")

    elif (computer == 1 and you == 0):
        print ("You Win")

    elif (computer == 0 and you == 1):
        print ("You Lose")

    elif (computer == 0 and you == -1):
        print ("You Win")

    else :
        print ("Something Went Wrong!")