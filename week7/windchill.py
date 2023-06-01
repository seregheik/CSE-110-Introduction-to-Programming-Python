# author = osasere ik

# for creativity i added a checker for temperature and unit to make sure user enters
# valid credential
wind_speed = 0

def celcius_to_farenheit(celcius_temp):
    degree_farenheit = (celcius_temp*(9/5))+32
    return degree_farenheit

def wind_chill_calculator(air_temperature,wind_speed):
    air_temperature = float(air_temperature)
    wind_speed = float(wind_speed)
    wind_chill = 35.74 + (0.6215*air_temperature)\
        - (35.75*(wind_speed**0.16))\
        + (0.4275*air_temperature*(wind_speed**0.16))
    return wind_chill

keep_asking = False
while not keep_asking:
    temperature = input('What is the temperature? ')
    try:
        temperature = float(temperature)
        first_keep_asking = False
    except ValueError:
        first_keep_asking = True
    if not first_keep_asking:
        unit = input('Farenheit or Celcius (F/C)? ').capitalize()
        if (unit == 'C' or unit == 'Celcius'):
            temperature = celcius_to_farenheit(temperature)
            keep_asking = True
        elif (unit == 'F' or unit == 'Farenheit'):
            temperature = temperature
            keep_asking = True
        else:
            print('Please enter a valid input')
    else:
        print('Please enter a valid input')
while wind_speed < 60:
    wind_speed += 5
    wind_chill = wind_chill_calculator(air_temperature=temperature,wind_speed=wind_speed)
    print(f'At temperature {temperature}F, and wind speed {wind_speed}mph, the windchill is: {wind_chill:.2f}F')