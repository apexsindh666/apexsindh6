logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)

"""
import random
from gamedata import data

def randomacct():
   return random.choice(data)


def format_data(account):
   name=account["name"]
   description=account["description"]
   country=account["country"]
   return  (f"{name},a {description},from {country}")
def checkans(user_guess,a_follower,b_follower):
   if a_follower>b_follower:
      return user_guess=="a"
   else:
      return user_guess=="b"
   

score=0
print(logo)
game_shouldcontinue=True
while game_shouldcontinue:
    acc_a=randomacct()
    acc_b=randomacct()
    if acc_a==acc_b:
        acc_b=random.choice(data)
    print(f"compare A: {format_data(acc_a)}")
    print(vs)
    print(f"against B: {format_data(acc_b)}")
    guess=input("who has more followers: 'A' or 'B'\n" ).lower()
    fca=acc_a["follower_count"]
    fcb=acc_b["follower_count"]
    is_correct=checkans(guess,fca,fcb)
    if is_correct:
        score+=1
        print(f"you are rigth score: {score}")
        acc_a=acc_b
    else:
        print(f"sorry thats wrong score: {score}")
        game_shouldcontinue=False


