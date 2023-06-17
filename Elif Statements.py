x, y = 5, 10
if x > y:
    print("x is greater")
elif x < y: 
    print("x is less")

if x > y:
    print("x is greater")
elif (x + 10) < y:
    print("x is less")
elif (x + 5) == y:
    print("equal") 

z = 5
if x > y:
    print("greater")
elif x <= y:
    if x ==z:
        print("x is equal to z")
    elif x != z:
        print("x is not equal to z")

number = input("Enter a number: ")
number = int(number) 
if number < 100:
    print("Your number is less than 100")
elif number > 100:
    print("Your number is greater than 100")

if x > y:
    print("greater")
elif x < y:
    print("lower")

name = "John"
if name == "Jacob":
    print("Hello Jacob!")
else:
    print(f"Hello {name}!")

name = input("Enter your name: ") 
if name[0] == "A":
    print("Name starts with an A")
elif name[0] == "B":
    print("Name starts with a B")
elif name[0] == "J":
    print("Name starts with a J")
else:
    print(f"Name starts with a {name[0]}")

name = "John"
if name == "Jack":
    print("Hello Jack")
else:
    print("Hello John")


time = input("Enter the time of day in military time without a colon: ")
time = int(time) 
if time < 1200:
    print("Good Morning")
elif time >= 1200 and time < 1700:
    print("Good Afternoon")
elif time >= 1700:
    print("Good Evening")
    
