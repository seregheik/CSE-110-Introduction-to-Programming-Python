import math

def compute_area_square(length):
    area = length**2
    return area

def compute_area_rectangle(length,breadth):
    area = length*breadth
    return area

def compute_area_circle(radius):
    area = (math.pi)*(radius**2)
    return area
print('1. Square')
print('2. Rectangle')
print('3. Circle')
shape = input('Select shape: ').strip().capitalize()

if shape == '1' or shape == 'Square':
    length = float(input('Enter the length of the square: '))
    area_of_square = compute_area_square(length)
    print (area_of_square)
if shape == '2' or shape == 'Rectangle':
    length = float(input('Enter the length of the rectangle: '))
    breadth = float(input('Enter the breadth of the rectangle: '))
    area_of_rectangle = compute_area_rectangle(length,breadth)
    print(area_of_rectangle)
if shape == '3' or shape == 'Circle':
    radius = float(input('Enter radius of the circle: '))
    area_of_circle = compute_area_circle(radius)
    print(area_of_circle)