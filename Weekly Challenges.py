"""

row = input("How many rows would you like?")
row = int(row)

for i in range(row):
    print(' ' * (row - i) + ' x' * i)

    
names = ['John', ' ', 'Amanda', 5]

for i in names:
    if type(i) == str and i.isalpha():
        print(i)
"""

temps = [32, 12, 44, 29]

for i in temps:
    print((9/5) * i + 32)
