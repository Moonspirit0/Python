""" 
word = "Baseball"
if "b" in word:
    print(f"{word} contains the character b")

word = "Baseball"
if "x" not in word:
    print(f"{word} does not contain the character x")

check = input("Type in a word: ")
if "es" in check:
    print(f"Your word, {check}, contain the letters es!")

ing = input("Enter a word: ")
if "ing" in ing[-3:]:
    print(f"Your word, {ing} ends with ing!")
    
word1 = input("Type in a word: ")
word2 = input("Enter another word: ")
word1 = word1.upper()
word2 = word2.upper()
if word1 == word2:
    print("They are both the same words!")
"""

number = input("Enter a number: ")
sqnumber = int(number) ** 2
print(f"{number} squared is: {sqnumber}!")
