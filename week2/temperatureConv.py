# Fahrenheit to celcius converter
fahr = float(input('What is the temperature in Fahrenheit? '))
conv_fahr = (fahr - 32) * (5/9)
print(f'The temperture in Celcius is {conv_fahr: .1f} degrees')