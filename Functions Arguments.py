numbers1 = [2, 4, 5, 10]
numbers2 = [1, 3, 6]
def square(nums):
    for num in nums:
        print(num**2)

def calcArea(r, pi = 3.14):
    area = pi * (r**2)
    print(f"Area: {area}")

def printName(first, last, middle = ""):
    if middle:
        print(f"{first}{middle}{last}")
    else:
        print(f"{first}{last}")

def addNums(num1, num2):
    print(num2)
    print(num1)

addNums(5, num2 = 2.5)
printName("John", "Smith")
printName("John", "Smith", "Paul")
calcArea(2)
calcArea(2, 3.14159)
square(numbers1)
square(numbers2)

