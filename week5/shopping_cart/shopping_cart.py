# Author: Osasere Ikponmwosa 

# for creativity I made use of error handling should the user enter an unexpected input

actions = ['Add item', 'View Cart', 'Remove item', 'Compute total', 'Quit']
shopping_cart = []
items_prices = []

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
    # this action computes the total price of items in the cart
        elif user_action == 3:
            sum = 0
            for index in range(len(items_prices)):
                to_be_summed = items_prices[index]
                sum = to_be_summed + sum
            print(f'The total price of the items in the shopping cart is ${sum:.2f}')
        
    # this action is for user to remove item from shopping list
        elif user_action == 2:
            remove_from_cart_string = input('What item would you like to remove? ')
    # this 'try' is to handle errors resulting from invalid user input
            try:
                remove_from_cart = int(remove_from_cart_string)
                shopping_cart.pop(remove_from_cart-1)
                print('Item removed')
    # the error value if user enters wrong input for removal of item
            except ValueError:
                print('!!!Please enter a valid input!!!')

    # this action is for user to view contents of shopping cart   
        elif user_action == 1:
            if not shopping_cart:
                print('The cart is empty. Please add an item')
            else:
                print('\nThe contents of the shopping cart are:')
                for j in range(len(shopping_cart)):
                    cart_items = shopping_cart[j]
                    price = items_prices[j]
                    print(f'{j+1}. {cart_items} - ${price:.2f}')
    # this action is for user to add items to cart
        elif user_action == 0:
            add_to_cart = input('What item would you like to add? ').capitalize()
            price_of_item = input(f"What is the price of '{add_to_cart}'? ")
            try:
                item_price = float(price_of_item)
    # I made use of double quotations here because of the single quotation in the centence
                print(f"'{add_to_cart}' has been added to the cart")
                shopping_cart.append(add_to_cart)
                items_prices.append(item_price)
            except ValueError:
                print('\n!!!Please enter a proper price!!!')
    except ValueError:
        print('\n!!! Please type in a proper value !!!')