import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

#creating variable to count scores of your and computer
yourscore = 0
compscore = 0

#creating loop for continous play without restart  : y = yes and n = no

replay = "y"

while (replay == "y"):
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
            yourscore += 1
            print ("You Win")

        elif (computer == -1 and you == 0):
            compscore += 1
            print ("You Lose")

        elif (computer == 1 and you == -1):
            compscore += 1
            print ("You Lose")

        elif (computer == 1 and you == 0):
            yourscore += 1
            print ("You Win")

        elif (computer == 0 and you == 1):
            compscore += 1
            print ("You Lose")

        elif (computer == 0 and you == -1):
            yourscore += 1
            print ("You Win")

        else :
            print ("Something Went Wrong!")


    print ("\n")
    replay = input ("Want to replay? (y/n) : ")

else :
    print (f"\nYour Score : {yourscore} \nComputer Score : {compscore}")