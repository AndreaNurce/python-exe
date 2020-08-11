import random
item = ["rock" , "paper" , "scissors"]
scores = [0,0]

def main():
    try:
     random_item = random.randint(0 ,2)
     chosen = item[random_item]
     word = input("Choose : \n 1.Rock ,\n 2.Paper ,\n 3.Scissors \n Select : ")
     word.lower()

     if word ==  chosen :
         print("\n \n   [+] Hmm , this is a draw !!! \n \n   ")
         print(" [+] Scores : Computer : ", scores[0], "You", scores[1] ,"\n \n   ")
         play_again()
     if word == "rock" and chosen == "paper" or word == "paper" and chosen == "scissors" or  word == "scissors" and chosen == "rock":
         print("\n \n   [+] You lose !!! \n \n ")
         scores[0] += 1
         print(" [+] Scores : Computer : " ,scores[0] , "You" , scores[1],'\n \n   ' )
         play_again()

     if word == "paper" and chosen == "rock" or word == "scissors" and chosen == "paper" or word == "rock" and chosen == "scissors":
         print("\n \n   [+] Congrats you won!!! \n \n    ")
         scores[1] += 1
         print("[+] Scores : Computer : ", scores[0], " You", scores[1], "")
         play_again()
     else :
         print("\n \n    [-] Please enter a valid option !\n \n ")
         main()

    except KeyboardInterrupt :
        exit()


def play_again():
    try :
        ask = input(" [+]Pres 'Enter' to play again. \n\n [+] Enter any other key to exit. \n  ")
        if ask == "":
            main()
        else :
            exit()
    except KeyboardInterrupt :
        exit()
main()