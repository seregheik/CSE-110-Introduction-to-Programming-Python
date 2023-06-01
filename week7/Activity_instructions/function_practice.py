def display_regular(message):
    regular = message
    return regular
def display_uppercase(message):
    uppercase = message.upper()
    return uppercase
def display_lower(message):
    lower = message.lower()
    return lower

user_message = input('Enter your message: ')



converted_regular = display_regular(user_message)
converted_upper = display_uppercase(user_message)
converted_lower = display_lower(user_message)


print(converted_regular)
print(converted_upper)
print(converted_lower)