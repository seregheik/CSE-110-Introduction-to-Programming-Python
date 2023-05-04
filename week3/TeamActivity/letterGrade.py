grade_perc = float(input('What is your grade percent? '))

is_passed = False
sign = ''
sign_det = grade_perc % 10
if grade_perc <= 90 or grade_perc < 60:
    if sign_det >= 7:
     sign = '+'
elif sign_det < 3:
    sign = '-'

if grade_perc >= 90 and grade_perc <= 100:
    grade = 'A'
elif grade_perc >= 80 and grade_perc < 90:
    grade = 'B'
elif grade_perc >= 70 and grade_perc < 80:
    grade = 'C'
elif grade_perc >= 60 and grade_perc <70:
    grade = 'D'
elif grade_perc < 60:
    grade = 'F'
else:
    grade = 'not valid, please input a valid score'

if grade_perc >= 60 and grade_perc <= 100:
    is_passed = True

print(f'Your grade is {grade}{sign}')
if is_passed:
    print('Congratulations on passing your examinations.')
elif not is_passed and grade_perc < 60:
    print('Try harder next time')