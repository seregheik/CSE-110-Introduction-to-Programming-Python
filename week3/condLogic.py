price = float(input('how much did you pay? '))
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('Tax rate is: ' + str(tax))