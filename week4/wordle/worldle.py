#Author: Osasere

# for creativity:
# instead of using a fixed word in a variable, I used the random.choice to 
# loop through an array for the game to have different words at start

import random

secret_words = ['mosiah',\
                'fish',\
                'nephi',\
                'moroni',\
                'jesus']

secret_word = random.choice(secret_words)


print('Welcome to the word guessing game! ')
trials = 0
user_guess = ''

print('Your hint is: ', end='')

for hint in secret_word:
    hint = '_ '
    print(hint,end='')

print()

while user_guess != secret_word:
    print()
    user_guess = input('What is your guess? ').lower()
    trials = trials + 1
    
    if len(user_guess) != len(secret_word):
        print(f'Sorry the secret word is a {len(secret_word)} letter word')
    if user_guess == secret_word:
         print(f'Congratulations! You guessed it!')
         print(f'It took you {trials} guesses.')
         break 
    if len(user_guess) == len(secret_word):
        print('The hint is: ', end='')
        for i, a in enumerate (secret_word):
            for j, b in enumerate(user_guess):
                while i == j:
                    if b == a:
                        b = f'{b.capitalize()} '
                    elif b in secret_word:
                         b = f'{b} '
                    else:
                        b = '_ '
                    print(b, end='')

                    break
             
                    