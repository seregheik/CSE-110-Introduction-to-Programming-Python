country = input('What country do you live at? ').lower()
tax = 0
if country == 'canada':
    province = input('What province do you live in? ').lower()
    if province in ('alberta', \
                    'nunavut', 'yukon'):
        tax = 0.05
    elif province in ('ontario'):
        tax = 0.13
    else:
         tax = 0.15
else:
    tax = 0.0
print (tax)
