# i added a discount calculator for all purchases above $500
# anytime the purchase exceeds $500 a message is displayed that the person is eligible for 18% discount
# and the total is recalculated and change displayed

price_of_child_meal = float(input('What is the price of the child\'s meal? $'))
price_of_adult_meal = float(input('What is the price of an adult\'s meal? $'))
no_child = int(input('How may children are there? '))
no_adult = int(input('How many adults are there? '))
tax_rate = float(input('What is the sales tax rate? '))

subtotal = (no_child*price_of_child_meal)+(no_adult*price_of_adult_meal)
sales_tax = (subtotal)* (tax_rate/100)
total= subtotal+sales_tax

print(f'\nSubtotal: ${subtotal:.2f}')
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Total: ${total}')

payment_amt = float(input('What is the payment amount? $'))
change = payment_amt-total

# Discount calculator

if total <= 500:
    print(f'Change: ${change:.2f}')
    print('Thank you for purchasing with us')
else :
    print(f'\nFor purchasing items worth over $500 you\'re eligible for 18% discount. \nYour total has been adjusted as follows:')
    adj_total = total - (0.18*total)
    adj_change = payment_amt - adj_total
    print(f'\nNew Total: ${adj_total:.2f} \nChange: ${adj_change:.2f}')
    print('Thank you for purchasing with us')