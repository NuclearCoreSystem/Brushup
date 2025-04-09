# Just a calculator:
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

# Now comes the input:

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
operation = input("Choose Operation (+,-,*,/): ")

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
elif operation == '*':
    print(multiply(num1, num2))
elif operation == '/':
    print(divide(num1, num2))
else:
    print("Not Happening.")