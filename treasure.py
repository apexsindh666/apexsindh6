#dive into the game and find the treasure
print("welcome to treasure island")
print("your mission is to find the treasure")
c1=input("your are at the cross road do you wanna go left or right.").lower()
if c1=="right":
    print("game over you fell into a hole")
if c1=="left":
    c2=input("continue forward you have come to an lake type 'wait' to wait for boat or type 'swim' to swim in lake").lower()
    if c2=="wait":
        print("you reached the island safely")
        c3=input("you found 3 doors of red,yellow and green enter the door you want to move further").lower()
        if c3=="yellow":
            print("you found the treasure you won")
        elif c3=="red":
            print("you opened door of fire,you lost")
        else:
            print("you fell in to water of acid,you lost")
    else:
        print("you got eaten by pirhanas")
else:
    print("ivalid input")
