import random
import time
x  = "    "
print("\n\n\n",x*10 ,'*******************\n',x*10,'*    This is      *  \n',x*10,'*   a password    *\n',x*10,'*   generator     *\n',x*10,'*******************\n',x*10,'*Direct by Andr3a *\n',x*10,'*******************\n\n\n\n')

def inputed():
    nr = 0
    try:
     nr = int(input("[+] Specify how long do you want your password to be :  "))
    except ValueError:
        print('[-]Please enter a vaild number ')
        inputed()
    except KeyboardInterrupt :
        answer = input("\nDo you want to exit   Y/N")
        answer.lower()
        if answer == "y" or answer == "yes":
            print("\n\n[-] Exiting ... !!!\n\n")
            time.sleep(3)
            exit()
        if answer == "n" or answer == "no":
            inputed()
        else:
            print("[-] Exiting ... !!!")
            time.sleep(3)
            exit()
    return nr
nr = inputed()
def fun(num):
    text = "QWERTYUIOPASDFGHJKLZXCVBNM{};':<>,.?/1234567890-=!@#$%^&*()_+qwertyuiop[]asdfghjklzxcvbnm"
    text_list = list(text)
    string = ""
    if num < 8 :
        num = 8

    for i in range(num):
        ran_num = random.randint(0, 88)
        string += text_list[ran_num]
    print("\n Your passord is  : " ,string)
    try :
        input("\n\n Pres enter to continue")
    except KeyboardInterrupt:
        print("\n\n[-] Exiting ... !!!\n\n")
        time.sleep(3)
        exit()

fun(nr)
