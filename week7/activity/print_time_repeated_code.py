# from datetime import datetime

# first_name = 'Osasere'
# def print_time(message):
#     print(message)
#     print(datetime.now())
#     print()

# print('Hey')
# print_time('fuck you')
def initial_name(name):
    initial = name[0:1].upper()
    return initial

firstname = input('enter your firsname: ')
lastname = input('enter your last name: ')

firstname_initial = initial_name(firstname)
lastname_initial = initial_name(lastname)

print(firstname_initial)
print(lastname_initial)