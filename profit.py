cp = int(input("enter the cost price"))
sp = int(input("enter the selling price"))

if(sp>cp):
    print("You have profit ")
    pt = sp-cp
    print(pt)
else:
    print("You have no profit.")