#its a simple calci which allows user to perform basic calculations
def calculator(a,b):
    s=input('enter the operation you need to do[+,-,*,/,%]\n')
    if s=='+':
        return a+b
    elif s=='-':
        return a-b
    elif s=='*':
        return a*b
    elif s=='/':
        return a/b
    else:
        print("invalid operator")
a=int(input('enter the value of first number\n'))
b=int(input('enter the value of second number\n'))
cal=calculator(a,b)
print(cal)
proceed=input("do you want to further proceed calculation ['yes' or 'no']\n")
if proceed=='yes':
    c=cal
    d=int(input('enter the next num\n'))
    final=calculator(c,d)
    print(f"final ans is {final}")
else:
    print(f"final ans is {cal}")
