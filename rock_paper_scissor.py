rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
choice=int(input("what do you choose? type 0 for rock,1 for paper,2 for scossors"))

import random
rn=random.randint(0,2)
print(game[rn])
if choice>=0 and choice<=2:
    print(game[choice])
if choice==0 and rn==2:
    print("you won")
elif choice>=3 or choice<0:
    print("invalid num,you loose")

elif rn>choice:
    print("you loose")
elif rn<choice:
    print("you win")
elif choice==rn:
    print("its a draw")
elif rn==0 and choice==2:
    print("you loose")