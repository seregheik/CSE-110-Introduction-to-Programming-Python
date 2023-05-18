friends = []
friend = ''

while friend != 'End':
    friend = input('Type the name of a friend: ').capitalize()
    if friend == 'End':
        print()
        print('Your friends are:')
        for friend_list in friends:
            print(friend_list)
    else:
        friends.append(friend)