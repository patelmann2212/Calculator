def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cannot divide by zero."


while True:
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    ex = int(input("Select to operate:\n1:Sum\n2:Substration\n3:Multiplication\n4:Division\n"))

    if ex == 1:
        print(add(a, b))
    elif ex == 2:
        print(subtract(a,b))
    elif ex == 3:
        print(multiply(a,b))
    elif ex == 4:
        print(divide(a,b))
    else:
        print("Enter valid selection!!")
        
    con = input("Are you want to continue? (yes/no)\n").lower()

    if con == 'no':
        print("Calculator exited")
        break

        
