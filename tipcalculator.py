#calculte tip on basis of your hotel bill
print("welcome to the tip calculator\n")
bill=float(input('enter the total bill\n'))
p=int(input("total no of people\n"))
tip=int(input("tip % u wish to give 10,12,15\n"))
bt=(bill*(1+tip/100))/p
fp=round(bt,2)
print(f"each person should pay{fp}")
