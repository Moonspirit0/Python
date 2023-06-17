"""
sport = ""
sports = ["Baseball", "Hockey", "Football", "Basketball"]
for sport in sports:
    print(sport)

names = ["Bob", "Jack", "Rob", "Bob", "Robert"]
while "Bob" in names:
    names.remove("Bob")
print(names)

words = []
done = True
while done:
    word = input("Enter a word: ")
    if word.lower() == "quit":
        done = False
    else:
        words.append(word)

for word in words:
    print(word)


"""

names = ["Lily", "Olivia", "Samantha", "Lily", "Felix", "Diana", "Olivia", "Olivia", "Diana"]
for name in names:
    while names.count(name)> 1:
        names.remove(name)
print(names)
