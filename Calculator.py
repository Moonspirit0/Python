print("Choose what you would like to do from the following menu:\n 1. Add\n 2. Subtract\n 3. Multiply\n 4. Divide")
operation = input("Type the corresponding number: ")
operation = operation.lower()
if operation == "1":
    print("You chose to add.")
elif operation == "2":
    print("You chose to subtract.")
elif operation == "3":
    print("You chose to multiply.")
elif operation == "4":
    print("You chose to divide.")

if operation == "2" or operation == "4":
    print("Please keep in mind that the order of your numbers matter.")
num1 = input("What is the first number? ")
num2 = input("What is the second number? ")

if operation == "2" or operation == "4" and num1 < num2:
   answer = input("Do you want to reverse the order of your numbers? Y/N:") 
   if answer == " y" or answer == " Y": 
       temp = int(num1)
       num1 = int(num2)
       num2 = int(temp)
       print("The numbers have been reversed.")
   elif answer == " n" or answer == " N":
        print("Okay.")

try:
    num1, num2 = float(num1), float(num2)
    if operation == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "4":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}") 
    else:
        print("Sorry, but you have entered the incorrect option from the menu.")
except:
    print("Error: Improper numbers used. Please try again.")
