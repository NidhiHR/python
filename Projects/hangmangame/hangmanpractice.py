import random
import Hangman
import hangmanword
import os

word_guess=random.choice(hangmanword.word)
# print(word_guess)

print(Hangman.logo)

lives=6

dash_list=[]
for _ in word_guess:
    dash_list+="_"
print(dash_list)

end_of_game=False
while not end_of_game:
    guess=input("enter ur guess:")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    for i in range(len(word_guess)):
        if guess==word_guess[i]:
            dash_list[i]=word_guess[i]
    print(dash_list)
   
    if guess not in word_guess:
        lives-=1
        if lives==0:
            print("YOU LOOSE")
            print(f"THE CORRECT WORD IS {word_guess}")
            end_of_game=True

    if '_' not in dash_list:
        print("YOU WIN!!")
        end_of_game=True

    print(Hangman.stages[lives])


