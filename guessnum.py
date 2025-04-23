#guess the number and enjoy the time
import random
def number():
    
    num=random.randint(1,100)
    return num

def guess(cnum):
    guessnum=int(input("enter the num\n"))
    
    if cnum==guessnum:
        print("you won,found the correct num\n")
        return True
    elif  cnum>guessnum:
        print("your guess is lower than my guess\n")
    else:
        print("your guess is higher than my guess\n")
    return False


print("welcome to number guessing game !\n")
print("i am guessing a number between 1 to 100\n")
level=input("enter the level you want to try 'easy' or 'hard'\n")
cnum=number()
if level=='easy':
    print("you have 10 rounds to guess\n")
    for x in range(1,11):
        print(f"round {x},you have {10-x} guess left\n ")
        if(guess(cnum)):
            break
    else:    
        print(f"end of the game the number was {cnum}\n")   
elif level=='hard':
    print("you have 5 rounds to play\n")
    for x in range(1,6):
        print(f"round {x},you have {5-x} guess left\n ")
        if(guess(cnum)):
            break
    else:
        print(f"end of the game the num was {cnum}\n")  
else:
    print("invalid input")
