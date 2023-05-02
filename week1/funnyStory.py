# in this particular assignment i added a conditional statement 
# that gives two alternative endings to the story,
# if the user coincidentally types the animal and favourite pet as the same
# it gives an ending where they discover the animal is his pet
# or else it gives an ending where the owner comes to claim the animal

print (f'Please enter the following: \n')
adjective = input('adjective: ').lower()
animal = input('animal: ').lower()
verb = input('verb: ').lower()
exclamation = input('exclamation: ').capitalize()
verb2 = input('verb: ').lower()
verb3 = input('verb: ').lower()

# input for favourite pet
fav_pet = input('favorite pet: ').lower()

print (f'\n')
print (f'Your story is: \n')
print (f'The other day, I was really in trouble. It all started when I saw a very \n{adjective} {animal} {verb} down the hallway. "{exclamation}!" I yelled. But all \nI could think to do was to {verb2} over and over. Miraculously, \nthat caused it to stop, but not before it tried to {verb3} \nright in front of my family.')

# if and else statement to determine how the story ends

if fav_pet == animal :
    print(f'Turns out the {adjective} {animal} was my pet scooby')
else: 
    print(f'Only for the owner to come and claim the {animal}')