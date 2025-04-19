#password generation
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
s=int(input("do you need easy or hard password press 0 for easy and 1 for hard"))
if s==0:

    password=""

    for char in range(1,nr_letters+1):
        password+=random.choice(letters)
    for char in range(1,nr_symbols+1):
        password+=random.choice(symbols)
    for char in range(1,nr_numbers+1):
        password+=random.choice(numbers)
    print(password)   
else:
    password=[]
    for char in range(1,nr_letters+1):
        password.append(random.choice(letters))
    for char in range(1,nr_symbols+1):
        password.append(random.choice(symbols))
    for char in range(1,nr_numbers+1):
        password.append(random.choice(numbers))
        random.shuffle(password)
    passw=""
    for char in password:
        passw+=char
    print(passw) 

