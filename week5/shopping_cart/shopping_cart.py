actions = ['Add item', 'View Cart', 'Remove item', 'Compute total', 'Quit']
shopping_cart = []

print('Welcome to the shopping cart program!')
end = False
while not end:
    print('\nPlease select one of the following:')
    for i in range(len(actions)):
        action = actions[i]
        print(f'{i+1}. {action}')
    user_action_input = input('Please enter an action: ')

    # this is the try function to handle error should the user enter an invalid value
    try:
        user_action = int(user_action_input)
        user_action = user_action - 1
        if user_action > (len(action)) or user_action < 0:
            print('Please enter a valid action!!!')
        elif user_action == 4:
            print('Thank you. Goodbye.')
            end = True
            break
        elif user_action == 3:
            print('to be done')
        
    # this action is for user to remove item from shopping list
        elif user_action == 2:
            remove_from_cart_string = input('What item would you like to remove? ')

    # this 'try' is to handle errors resulting from invalid user input
            try:
                remove_from_cart = int(remove_from_cart_string)
                shopping_cart.pop(remove_from_cart)
                print('Item removed')
    # the error value if user enters wrong input for removal of item
            except ValueError:
                print('Please enter a valid input')

    # this action is for user to view contents of shopping cart   
        elif user_action == 1:
            if not shopping_cart:
                print('The cart is empty. Please add an item')
            else:
                print('\nThe contents of the shopping cart are:')
                for j in range(len(shopping_cart)):
                    cart_items = shopping_cart[j]
                    print(f'{j+1}. {cart_items}')


    # this action is for user to add items to cart
        elif user_action == 0:
            add_to_cart = input('What item would you like to add? ').capitalize()

    # I made use of double quotations here because of the single quotation in the centence
            print(f"'{add_to_cart}' has been added to the cart")
            shopping_cart.append(add_to_cart)
    except ValueError:
        print('\n!!! Please type in a proper value !!!')