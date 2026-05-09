# TYPE CASTING
a = str(input("Enter your name: "))
print(type(a))

b = float(input("Enter your height: "))
print(type(b))


# ARITHMETIC OPERATORS
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Floor Division =", a // b)
print("Remainder =", a % b)
print("Power =", a ** b)


# ASSIGNMENT OPERATORS
print("Enter a number, we can tell its square")
a = int(input("Enter a number: "))
a **= 2
print("Square =", a)

print("Enter a number, we can tell its cube")
a = int(input("Enter a number: "))
a **= 3
print("Cube =", a)


# RELATIONAL OPERATORS
age1 = 20
age2 = 13

print(age1 == age2)
print(age1 != age2)
print(age1 > age2)
print(age1 < age2)
print(age1 >= age2)
print(age1 <= age2)


# LOGICAL OPERATORS
age = 18
height = 160

if (age > 17) and (height > 159):
    print("You passed the exam")
else:
    print("You failed the exam")


level = 20
health = 7

if (level > 25) or (health > 5):
    print("Next level")
else:
    print("Failed")


a = True
print(not a)


a = 15

if not(a > 20):
    print("Not greater than 20")
else:
    print("Greater than 20")


# SPECIAL OPERATORS
# IDENTITY OPERATORS
a = ["apple", "orange", "dragon fruit"]
b = ["apple", "orange", "dragon fruit"]

print(a is not b)

a = b
print(a is b)


# BITWISE OPERATORS
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 3)
print(a >> 3)
