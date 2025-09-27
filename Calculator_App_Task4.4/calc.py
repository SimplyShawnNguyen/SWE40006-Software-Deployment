def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

if __name__ == "__main__":
    print("Simple Calculator")
    print("Choose operation: add, sub, mul, div")
    choice = input("Enter choice: ")

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    if choice == "add":
        print("Result:", add(x, y))
    elif choice == "sub":
        print("Result:", subtract(x, y))
    elif choice == "mul":
        print("Result:", multiply(x, y))
    elif choice == "div":
        print("Result:", divide(x, y))
    else:
        print("Invalid choice")
