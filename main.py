from calculator import add, subtract,multipy,divide
if __name__ == '__main__':
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    op = input("Enter the operation (+,*,/,-):  ")

    if op == "+":
        print(add(x,y))
    elif op == "-":
        print(subtract(x,y))
    elif op == "*":
        print(multipy(x,y))
    elif op == "/":
        print(divide(x,y))
    else:
        print("Invalid operation")
