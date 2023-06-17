age = input("Enter your age in numbers: ")
age = int(age) 

if age >= 0 and age <= 12:
    print("You are a kid")
elif age >= 12 and age <= 19:
    print("You are a teenager")
elif age >= 20 and age <= 30:
    print("You are a young adult")
elif age >= 31 and age <= 64:
    print("You are a adult")
elif age >= 65:
    print("You are a senior")
else:
    print("You have incorrectly entered your age") 
