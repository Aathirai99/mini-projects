'''
What it is: the computer picks a secret word, shown as underscores. 
You guess one letter at a time. 
Right guesses show in the word, wrong ones use up your lives. 
Guess the word before you run out of lives.
'''

import random
words = ['python', 'planet', 'garden', 'basket', 'window']

while True:
    print("Letss go")
    game_word = random.choice(words)
    #game_word = 'garden'
    life =6
    empty_input = ['_']*len(game_word)
    print(" ".join(empty_input))
    guessed_list = []
    

    while True: 

        
        
        inp = input("Guess a letter: ").lower()
        if len(inp) !=1 or  not inp.isalpha():
             print("Your entry is invalid. Enter a single letter")
             continue

        if inp not in guessed_list:
            guessed_list.append(inp)
        else: 
             print("letter already guessed, try a different letter")
             print("\n")
             continue


        


        turn = False
        for i in range(len(game_word)):

            if inp == game_word[i]:
                empty_input[i]= inp

                turn = True
            
        if turn == False:
            print("Wrong!")
            life-=1

        print('\n')
        print(" ".join(empty_input))
        print(f'Lives: {life}, Guessed: {" ".join(guessed_list)}')
        if '_' not in empty_input: 
                print("You have won!")
                break
            
        if life==0: 
            print("Game over. The word was", game_word)
            break


    inn = input("Play again, y/n? ")
    if inn.strip().lower() == 'y':
         continue
    else: 
         print("GOODBYE! ")
         break