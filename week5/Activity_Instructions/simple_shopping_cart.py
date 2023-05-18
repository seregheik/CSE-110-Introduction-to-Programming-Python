cart = []
new_cart = []
items = ''
print('Please enter the items of the shopping list (type: quit to finish): ')
while items != 'Quit':
    items = input('Item: ').capitalize()
    if items != 'Quit':
        cart.append(items)
print()
print('The shopping list is: ')
for i in range(len(cart)):
    item = cart[i]
    print(item)
print()
print('The shopping list with indexes is: ')
for i in range(len(cart)):
    item = cart[i]
    print(f'{i}. {item}')
print()

change_item_index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ').capitalize()

# though i did come out with same result by creating a new array, this isnt the best way

# print('The shopping list with indexes is: ')
# for i in range(len(cart)):
#     if i < change_item_index or i > change_item_index:
#         item = cart[i]
#         new_cart.append(item)
#     else:
#         item = cart[change_item_index]
#         new_cart.append(new_item)
# for i in range(len(new_cart)):
#     new_item = new_cart[i]
#     print(f'{i}. {new_item}')

cart[change_item_index] = new_item
print()
print('The new shopping list with indexes is: ')
for i in range(len(cart)):
    item = cart[i]
    print(f'{i}. {item}')