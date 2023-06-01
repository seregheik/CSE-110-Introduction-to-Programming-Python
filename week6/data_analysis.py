max_life_expectancy = -1
overall_max_life_expectancy = -1
overall_min_life_expectancy = float('inf')
min_life_expectancy = float('inf')
summation = 0
reiteration = 0
print('Select one of the following to view data')
print('1. Year of interest')
print('2. Country')
user_input = input('Enter the number of your choice: ').capitalize().strip()
if user_input == '1' or user_input == 'Year' or user_input == 'Year of interest':
    year_of_interest = int(input('Enter Year of interest: '))
    user_input = 'Year'
elif user_input == '2' or user_input == 'Country':
    user_input = 'Country'
    country_of_interest = input('Enter country of interest: ')
    if len(country_of_interest) == 3:
        country_of_interest = country_of_interest.upper()
# country_of_interest = 'USA'
drop = 0

with open('./life-expectancy.csv') as life_expectancy:
    next(life_expectancy) #skip the first line
    for life_expectancy in life_expectancy:
        life_expectancy = life_expectancy.strip()
        life_expectancy = life_expectancy.split(',')

        entity = life_expectancy[0]
        code = life_expectancy[1]
        year = int(life_expectancy[2])
        expectancy = float(life_expectancy[3])
        if expectancy >= overall_max_life_expectancy:
            overall_max_life_expectancy = expectancy
            overall_max_entity = entity
            overall_max_year = year
        if expectancy <= overall_min_life_expectancy:
            overall_min_life_expectancy = expectancy
            overall_min_entity = entity
            overall_min_year = year
        if user_input == 'Country':
            if entity == country_of_interest or country_of_interest == code:
                country_of_interest = entity
                if expectancy >= max_life_expectancy:
                    max_life_expectancy = expectancy
                if expectancy < min_life_expectancy:
                    min_life_expectancy = expectancy
                    min_entity = entity
                summation += expectancy
                reiteration += 1
                average_expectancy = summation/reiteration
        elif user_input == 'Year':
            if year == year_of_interest:
                if expectancy >= max_life_expectancy:
                    max_life_expectancy = expectancy
                    max_entity = entity
                if expectancy < min_life_expectancy:
                    min_life_expectancy = expectancy
                    min_entity = entity
                summation += expectancy
                reiteration += 1
                average_expectancy = summation/reiteration
if user_input == 'Year':
    print(f'\nThe overall max life expectancy is: {overall_max_life_expectancy} from {overall_max_entity} in {overall_max_year}')
    print(f'The overall min life expectancy is: {overall_min_life_expectancy} from {overall_min_entity} in {overall_min_year}')
    print(f'\nFor the year {year_of_interest}:')
    print(f'The average life expectancy accross all countries was {average_expectancy:.2f}')    
    print(f'The max life expectancy was in {max_entity} with {max_life_expectancy}')       
    print(f'The min life expectancy was in {min_entity} with {min_life_expectancy}')
if user_input =='Country': 
    print(f'The maximum life expectancy for {country_of_interest} is {max_life_expectancy}')
    print(f'The minimum life expectancy for {country_of_interest} is {min_life_expectancy}')
    print(f'The average life expectancy for {country_of_interest} is {average_expectancy: .2f}')
