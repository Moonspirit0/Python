from random import choice 
from IPython.display import clear_output

#declare game variables 
words = ["tree", "basket", "chair", "paper", "python"]
word = choice(words) #randomly chooses a word from the list 
guessed, lives, game_over = [], 7, False #multi variable assignment

#create a list of underscores to the length of the word
guesses = ["_"] * len(word)

#create main game loop 
while not game_over: 
    #output game information
    hidden_word = "".join(guesses)
    print(f"Your guessed letters: {guessed}")
    print(f"Word to guess: {hidden_word}")
    print(f"Lives: {lives}")
          
    ans = input("Type quit or a letter: ")
    ans = ans.lower()
    
    clear_output() #clear all previous output
    
    if ans == "quit":
        print("Thanks for playing.") 
        game_over = True                           
    elif ans in word and ans not in guessed: #check if letter in word 
        print("You guessed the word correctly!") 
        
        #create a loop to change the underscore to proper letter
        for i in range(len(word)): 
            if word[i] == ans: #compares values at indexes
                guesses[i] = ans 
    elif ans in guessed: 
        print("You already guessed that. Try again.")
    else: 
        lives -= 1 
        print("Incorrect, you lost a life.") 
    if ans not in guessed: 
        guessed.append(ans)
    if lives <= 0:
        print("You lost all your lives, you lose!")
        game_over = True 
    elif word == "".join(guesses): 
        print("Congrats! You guessed correctly!") 
        game_over = True 
