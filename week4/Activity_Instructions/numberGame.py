import random
start = True
num = random.randint(1,2)
trials = 0
user_guess = int(input('What is the magic number guess? '))
while start:
    while user_guess != num:
        if user_guess > num:
            print('lower')
            user_guess = int(input('What is the magic number guess? '))
            trials = trials + 1
        elif user_guess < num:
            print('higher')
            user_guess = int(input('What is the magic number guess? '))
            trials = trials + 1
    print(f'You guessed it! You had a total of {trials} trials.')
    play_again = input('Do you want to play again? YES or NO ').lower()
    if play_again == 'no':
        start = False
        print('thank you for playing')
    elif play_again == 'yes':
        start = True
        user_guess = int(input('What is the magic number guess? '))
    else: 
        print('goodbye')
        start = False