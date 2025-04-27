#loop application
 #students mark calculator
record=[]

students=int(input("enter the number of students\n"))
for i in range(students):
    name=input(f"enter the student {i+1} name\n")
    sub=int(input('enter the number of subjects\n'))
    total=0
    for j in range(sub):
        sn=input(f'enter subject {j+1} name\n')
        marks=float(input(f'enter the {sn} marks\n'))
        record.append({"name":name,"subname":sn,"marks":marks})
        
        total+=marks
    avg=total/sub
    print(f"the student {name} has scored total of {total} with average marks of {avg}")

# #bill calculator
stock=[]

grand_total=0
n=int(input('enter the number of items needed to buy\n'))
for i in range(n):
    name=input('enter the item\n')
    no=int(input(f'how many of {name} is needed\n'))
    price=int(input(f'enter the cost of {name}\n'))
    total=price*no
    stock.append([name,no,price,total])
    grand_total+=total

for item in stock:
    print(f"Item: {item[0]},\n Quantity: {item[1]},\n Price per item: {item[2]},\n total of item: {item[3]}")

print(f"\nGrand Total: {grand_total}")
           

# #godown stock checker
godown=[]
item=0
num=int(input("enter the number of items\n"))
for i in range(num):
    s=(input(f'enter the {i+1} element\n'))
    ele=int(input(f'enter the num of items left in {s}\n'))
    godown.append([s,ele])
for item in godown:
    name=item[0]
    quantity=item[1]
    if quantity<5:
        print(f"{name} is less than 5 and needed to bought to the stock")

#patter making
n=int(input('enter the number of rows\n'))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print("")

for i in range(n,0 ,-1): 
    for j in range(i):      
        print("*", end=" ")
    print("")                
