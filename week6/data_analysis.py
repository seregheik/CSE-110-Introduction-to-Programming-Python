


max_life_expectancy = -1
overall_max_life_expectancy = -1
overall_min_life_expectancy = float('inf')
min_life_expectancy = float('inf')
summation = 0
reiteration = 0
year_array = []
country_array = []
expectancy_array = []
year_of_interest = int(input('Enter Year of interest: '))
drop = 0
a=0

with open('./life-expectancy.csv') as life_expectancy:
    next(life_expectancy) #skip the first line
    for life_expectancy in life_expectancy:
        life_expectancy = life_expectancy.strip()
        life_expectancy = life_expectancy.split(',')

        entity = life_expectancy[0]
        country_array.append(entity)
        code = life_expectancy[1]
        year = int(life_expectancy[2])
        year_array.append(year)
        expectancy = float(life_expectancy[3])
        expectancy_array.append(expectancy)

        if expectancy >= overall_max_life_expectancy:
            overall_max_life_expectancy = expectancy
            overall_max_entity = entity
            overall_max_year = year
        if expectancy <= overall_min_life_expectancy:
            overall_min_life_expectancy = expectancy
            overall_min_entity = entity
            overall_min_year = year
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
    print(f'\nThe overall max life expectancy is: {overall_max_life_expectancy} from {overall_max_entity} in {overall_max_year}')
    print(f'The overall min life expectancy is: {overall_min_life_expectancy} from {overall_min_entity} in {overall_min_year}')
    print(f'\nFor the year {year_of_interest}:')
    print(f'The average life expectancy accross all countries was {average_expectancy:.2f}')    
    print(f'The max life expectancy was in {max_entity} with {max_life_expectancy}')       
    print(f'The min life expectancy was in {min_entity} with {min_life_expectancy}') 
    
    for i in range(1, len(expectancy_array)):
        drop_difference = expectancy_array[i - 1] - expectancy_array[i]
        if drop_difference > drop:
            drop = drop_difference
            if country_array[i-1] == country_array[i]:
                print(country_array[i])
                print(year_array[i])
                print(drop)

    for i in range(1,len(country_array)):
        country_name = country_array[i]
        if country_array[i] == country_array_loop:
            a += 1
            
            print(f'{country_name}{a}')
        else:
            a = 0