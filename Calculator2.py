print("Choose what you would like to do from the following menu:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")
operation = input("Type the corresponding operation you would like to perform: ")
operation = operation.lower()
if operation == "add":
    print("You chose to add.")
elif operation == "subtract":
    print("You chose to subtract.")
elif operation == "multiply":
    print("You chose to multiply.")
elif operation == "divide":
    print("You chose to divide.")

if operation == "subtract" or operation == "divide":
    print("Please keep in mind that the order of your numbers matter. This calculator does not accept negative values.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

try:
    num1, num2 = float(num1), float(num2)
    if operation == "add":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "subtract":
        result = num1 = num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "multiply":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "divide":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}") 
    else:
        print("Sorry, but you have entered the incorrect option from the menu.")
except:
    print("Error: Improper numbers used. Please try again.")
