# number = int(input('Please type a positive number: '))

# while number<0:
#     print('Sorry, that is a negative number. Please try again.')
#     number = int(input('Please type a positive number: '))
# print(f'The number is: {number}')

# answer = input('May I have a piece of candy? ').lower()


answer = False

while not answer:
    answer_str = input('May I have a piece of candy? ').lower()
    if answer_str == 'yes':
        answer = True
print('Thank you')