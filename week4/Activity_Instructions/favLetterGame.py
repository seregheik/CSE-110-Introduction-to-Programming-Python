fav_word = 'Commitment'
fav_letter = input('What is your favourite letter? ')

for fav_letter in fav_letter:
    for fav_word in fav_word:
        if fav_word == fav_letter:
            fav_word='_'
        print(fav_word, end='')