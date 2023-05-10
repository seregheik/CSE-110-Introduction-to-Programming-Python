# Osasere's adventure game
# I added extra levels and alternate endings 

print('\n\nWelcome to Ree\'s multi-choice game')
print('\nAlways choose your action by typing the word in capitals \
corresponding to your choice in the prompt.')
is_start = False
proceed = False
start = input('\nType START to start game ').upper()

if start == 'START':
    is_start = True
else:
    print('Thank you for your time, Hope to see you next time')

if is_start :
    print('\n\nYou wake up in a dark room you, while trying to stand up, you feel a MATCH and a FLASHLIGHT')
    pick = input('\nWhich one do you pick? ').upper()
    if pick == 'MATCH':
        action = 'and strike it'
        proceed = True
    elif pick == 'FLASHLIGHT':
        action = 'and turn it on'
        proceed = True
    if proceed:
        print(F'\n\nYou pick up the {pick.lower()} {action.lower()} and for an instant you could\
           \nsee the room around you illumnate and then you see three doors.')
        door = input('\nWill you go through the FIRST or SECOND or THIRD door? ').upper()
        proceed = False
        if door in ('FIRST', 'SECOND', 'THIRD'):
            proceed = True
            if door == 'FIRST':
                sight = 'Genie'
                first_action = f'{sight.lower()} approaches you'
                second_action = f'{sight.lower()} stops and ask, "What is your name?"'
            elif door == 'SECOND':
                sight = 'Lion'
                first_action = f'{sight.lower()} stares at you and looks towards the left'
                second_action = f'{sight.lower()} and stares back at you and said'
            elif door == 'THIRD':
                sight = 'Walking tree'
                first_action = f'{sight.lower()} dashes towards you'
                second_action = f'{sight.lower()} raises a branch in an attempt to strike you'

            print(f'\n\nYou turn the {door.lower()} door open and see a {sight}. The {first_action}. \nAlmost immediately the {second_action}')
            if door == 'FIRST':
                name = input('\nPlease input your name: ')
                print(f'\n\n"Welcome {name}, my name is Ahba, you are currently in my floor, to proceed i\'m gonna ask\
                      \nyou three questions. If you get all three correctly I will send you back to the real world but if you get any wrong,\
                      \nyou will be eaten by me. Your first question will be \
                      \nHow many tickles does it take to make an Octopus laugh? ')
                answer1 = input('TENTICKLES or EIGHT or ONE? ').upper()
                if answer1 == 'EIGHT':
                    print('\n\nCorrect. Now for your second question \
                          \n"What do you call a snowman with a sunburn?"')
                    answer2 = input('WATERLOGED or MELTING or PARCHED ').upper()
                    if answer2 == 'MELTING':
                         print('Correct. Now for your third question \
                          \n"What do you call a bear with no teeth?\
                          \n GROWLER or GUMMY or SMOOTH"')
                         answer3 = input('Input your answer ').upper()
                         if answer3 == 'GUMMY':
                             print('"Correct. You passed my test" says the genie. All of a sudden, theres a bright light and you\
                                   \nwake up in your room.\
                                   \n\
                                   \nCongratulations on completing this game')
                         else:
                             print('"Wrong answer" says the genie.\
                          \nYou are immediately attacked, you scream for help but no one is around to help. You are eaten.')
                    else:
                        print('"Wrong answer" says the genie.\
                          \nYou are immediately attacked, you scream for help but no one is around to help. You are eaten.')
                else:
                    print('"Wrong answer" says the genie.\n\
                          You are immediately attacked, you scream for help but no one is around to help. You are eaten.')                   
            elif door == 'SECOND':
                print(f'"I am known as Leonus, the Guardian of the floor of Wisdom,I possess knowledge \
                      \nthat spans across ages, and I have been bestowed with the ability to \
                      \ncommunicate with those who show courage and a pure heart.\
                      \nYour first test will be The compassionate resolve:\
                      \nYou encounter a group of individuals who are in desperate need of help. They are facing a \
                      \ncrisis and require immediate assistance. Despite potential risks and diificulties"\
                      \n')
                answer1 = input('do you IGNORE, HELP or PREACH for them? ').upper()
                if answer1 == 'HELP':
                    print('Despite potential risks and challenges, you decide to lend a helping hand, using \
                          \nyour wisdom to assess the situation and courageously take action to alleviate their suffering.\
                          \n\
                          \nFor Your second test:\
                          \nIn a dense forest you hear someone scream, the sunlight struggled to pierce through the thick canopy of trees. As you\
                          \nventured deeper into the unknown to find out what happened, the air grew heavy with a sense of mystery and uncertainty. \
                          \nSuddenly, a low growl echoed through the silence, followed by rustling bushes and snapping twigs. \
                          \nYour heart raced as you realized you were not alone. You finally see who screamed in a pool of blood\
                          \nand unable to walk. In the distance, a pair of gleaming eyes stared\
                          \nback at you, belonging to a wild and formidable creature. ')
                    answer2 = ('Do you rush to HELP, FIGHT the the wild creature or RETREAT? ').upper()
                    if answer2 == 'RETREAT':
                        print('With wisdom guiding your judgment, you decide to take a step back temporarily, strategizing and\
                              \ngathering additional information to ensure a more calculated and effective approach.\
                              \n\
                              \nFor your third test:\
                              \nIn a busy marketplace, a street vendor diligently displayed his handmade crafts, his sole means of \
                              \nsurvival. A corrupt official approached, demanding an exorbitant bribe to allow the vendor to continue operating.')
                        answer3 = input('Do you IGNORE, CONFRONT or make REIMBURSEMENT to the vendor?')
                        if answer3 == 'CONFRONT':
                            print('With unwavering courage and wisdom, you confront the issue head-on, fearlessly challenging those responsible\
                                  \nand seeking to rectify the situation. Your actions display both the strength to face adversity and the \
                                  \ndiscernment to choose the right course of action.\
                                  \n"You have passed the final test"says Leonus. All of a sudden there is a bright light and you wake up in your bedroom\
                                  \n\
                                  \nCongrats on finishing this game')
                        else:('oops you failed the last test.Try again next time')
                    else:
                        print(f'You charge headon to {answer2.lower()} and is killed by the wild animal. You failed this test')
                else:
                    print('You have failed this test')
            elif door == 'THIRD':
                print('\nYou try to run but theres nowhere to run to. You\'re killed by the tree. ')
    else: 
        print('You failed to pick any appropriate action and died!')
else:
    print ('You\'ve entered an invalid number') 