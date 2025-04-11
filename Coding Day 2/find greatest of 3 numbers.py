request="enter any three numbers x, y,,z:"
print(request)
x=float(input("enter number x:"))
y=float(input("enter number y:"))
z=float(input("enter number z:"))
if(x>=y) and (x>=z):
        print("x is greater")
elif(y>=x) and (y>=z):
        print("y is greater")
else:
        print("z is greater")
        
    