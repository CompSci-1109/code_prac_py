Arithmetic Operators
print("initialised values a=700,b=344")
a=700
b=344
c=a+b
d=a-b
e=a*b
f=a/b
g=a%b 

print("the sum:")
print(c)
print("the difference:")
print(d)
print("the product:")
print(e)
print("the quotient:")
print(f)
print("the remainder:")
print(g)

Comparison Operators
print("thus begins relational operators")
print(a>b)  #700>344, hence true
print(b>a)  #344>700, hence false

print(b<a)  #344<700, hence true
print(a<b)  #700<300, hence false

print(a<=b) #700<=344, hence false
print(a>=b) #700>=344, hence true

print(a==b) #700=344, hence false

Logical Operators
print("Thus begins the code and its output for Logical operators")
print(True and False)
print(True or False)
print( not False)

Bitwise operators
bitand=a&b
bitor=a|b
bitnot= ~a
print("bitwise and of a and b:")
print(bitand)
print("bitwise of a or b" )
print(bitor)
print("bitwise not of a:")
print(bitnot)

x=float(8.90)
y=float(6.28)

sum=x+y
dif=x-y
multip=x*y
quotie=x/y
rem=x%y

print ("sumfloat:")
print(sum)
print ("subtrfloat:")
print(dif)
print ("multipfloat:")
print(multip)
print ("quotfloat:")
print(quotie)
print ("remfloat:")
print(rem)

abs(x=x*-1)
print(abs(x))
round(x)
round(x,1)


import math
ab=float(input("Enter any number:"))
sqrt= math.sqrt(ab)
print(sqrt)

print(math.ceil(ab))
print(math.floor(ab))
