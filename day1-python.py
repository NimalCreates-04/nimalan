 #type casting
a=str(input("enter your name"))
print(type(a))
b=float(input("enter yor hight"))
print(type(b))
#arthmathic operator
a=int(input("enter a number "))
b=int(input("enter anther number"))
print('addtition',a+b)
print('subtraction',a-b)
print('multiplication',a*b)
print('floor division',a/b,)
print('integer division',a//b)
print('remainder',a%b)
print('power',a**b)
#assignment opertors
print("enter a number we can tell its square")
a=int(input("enter a number"))
a**=2
print(a)

print("enter a number we can tell its cube")
a=int(input("enter a number"))
a**=3
print(a)
#relational opertors
age1=20
age2=13
print(age1==age2)
print(age1!=age2)
print(age1>age2)
print(age1<age2)
print(age1>=age2)
print(age1<=age2)
#logicial oprators
age=18
hight=160
if(age>17)and(hight>159):

    print("you pssed the exam")
else:
    print("you failed the exam")
    
level=20
health=7
if(level>25) or (health>5):
    print("next level")
else:
    print("failed")

a=True
print(not(a))

a=15
if not(a>20):
    print("greater")
else:
    print("lesser")
#special operators
#identity operaor
a=["apple","orange","dragon fruit"]
b=["apple","orange","dragon fruit"]
print(a is not b)

a=b
print(a is b)
#bitwise operator
a=int(input("enter a number"))
b=int(input("enter a number"))
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<3)    
print(a>>3)

      

    
    

    

    




