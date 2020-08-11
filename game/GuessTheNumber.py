
import random

points = [0,0]

def fun():
    try :
        number  = random.randint(0, 20)
        given_number  = int(input("please enter a number from 0  to 20 "))
        if number == given_number :
            points[1] += 1
            print("\n\nCongratulations you have gussed the right number!!" , "\n Scores: Computer " , points[0] ," : Player" , points[1] ,"\n\n" )
            play_again()
        if number > given_number and given_number <= 20 :
            points[0] += 1
            print("\n\nI guess my number is bigger than yours!!!", " \n Scores: Computer " , points[0] ," : Player" , points[1] ,"\n\n" )
            play_again()
        if number < given_number and given_number <= 20 :
            points[0] += 1
            print("\n\nI guess my number is smaller than your number!!!", "\n Scores: Computer " , points[0] ," : Player" , points[1] ,"\n\n" )
            play_again()
        else :
            print("[+] Please enter a number between 0-20")
            fun()
    except :
        exit()

def play_again():
    try:
        ask = input("[+]Pres 'Enter' to play again.\n [+] Enter any other key to exit ")
        if ask == "":
            fun()
        else :
            exit()
    except :
        exit()
fun()