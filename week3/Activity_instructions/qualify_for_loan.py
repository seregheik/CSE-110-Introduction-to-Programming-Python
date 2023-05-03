loan_size = float(input('How large is the loan? '))
credit_history = float(input('How good is your credit history? '))
income = float(input('How high is your income? '))
down_payment = float(input('How large is your down payment? '))

# set eligibilty to false
is_eligible = False

if loan_size > 5:
    if credit_history >= 7 and income >= 7:
        is_eligible = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            is_eligible = True
else: 
    if income >= 7 or down_payment >= 7:
        is_eligible = True
    elif income >= 4 and down_payment >= 4:
        is_eligible = True

if is_eligible:
    print('You\'re eligible for loan')
else:
    print('You\'re not eligible')