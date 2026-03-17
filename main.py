import random

'''
1 for Snake
-1 for Water
0 for Gun
'''

#creating variable to count scores of your and computer
yourscore = 0
compscore = 0
draw = 0

#creating loop for continous play without restart  : y = yes and n = no
replay = "y"

while (replay == "y"):

    #to choose random numbers by computer
    computer = random.choice ([-1, 0, 1])
    #to input user's choice
    youstr = input("Enter your choice (s, w, g) : ")
    
    #uses dictonary to convert string to number and no. to string
    youdict = {"s": 1, "w": -1, "g": 0}
    reversedict = {1 : "Snake" , 0 : "Gun" , -1 : "Water"}

    you = youdict[youstr]  #to convert string to number for processing which is choosen by you

    #It Print your choice and computer choice every time during play
    print (f"You Choose : {reversedict[you]} \nComputer Choose : {reversedict[computer]}\n")


    #It show draw when both choice are same
    if (computer == you):
        draw += 1
        print ("Draw")

    #These conditional staements decides you win or lose!
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


    #This decides you play continuous or not (program termination)!
    print ("\n")
    replay = input ("Want to replay? (y/n) : ")

#During terminating of program it prints the score of Your & Computer and also print no. of draw
else :
    print (f"\nYour Score : {yourscore} \nComputer Score : {compscore} \nNo. of Draw Matches : {draw}")