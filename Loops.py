"""
for num in range(100):
    if num%3 != 0:
        continue
    print(num)

#I searched up how to use divisibility stuff and it said to use num% and the number you wanted to use so I improvised it

word = input("Enter a word: ")
for letter in word:
    if letter in "aeiou":
        print(letter) 


while input("Type something: ").lower() != "quit":
    pass

"""

game_over = False
while game_over == False:
    for num in range(5):
        if num == 3:
            game_over = True
            break
        else:
            print(num)
            
