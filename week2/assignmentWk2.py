import math

# for square
sqr_length = float(input('What is the length of a side of the square? '))
print(f'The area of the square is: {sqr_length**2}')

# for rectangle
rect_length = float(input('What is the length of rectangle? '))
rect_width = float(input('What is the width of the rectangle? '))
print(f'The area of the rectangle is: {rect_length*rect_width}')

# for circle
circ_radius = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {3.14 * (circ_radius**2)}')

# stretch 1
circ_radius_stretch = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {math.pi * (circ_radius_stretch**2)}')

# stretch 2
single_val = float(input('What is your value? '))
print(f'Area of square whith this lenght: {single_val*2}')
print(f'Area of circle with this radius: {math.pi * (single_val*2)}')
print(f'Volume of cube with that side: {single_val**3}')
print(f'Volume of sphere with that radius: { (4/3) * math.pi**(single_val**3) }')

# stretch 3
# for square

val_in_cm = float(input('What is the length of a side of the square in cm? '))
print(f'The area of the square is: {val_in_cm**2} cm\u00b2 and {(val_in_cm**2)/10000}cm\u00b3')

# for rectangle
rect_length_cm = float(input('What is the length of rectangle in cm? '))
rect_width_cm = float(input('What is the width of the rectangle in cm? '))
print(f'The area of the rectangle is: {rect_length_cm*rect_width_cm}cm\u00b2 and {(rect_length_cm*rect_width_cm)/10000}cm\u00b3 ')

# for circle
circ_radius_cm = float(input('What is the radius of the circle? '))
print(f'The area of the circle is: {3.14 * (circ_radius_cm**2)}cm\u00b2 and {(3.14 * (circ_radius_cm**2))/10000}cm\u00b3')