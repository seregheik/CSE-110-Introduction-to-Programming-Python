# with open('courses.txt') as courses_file:
#     for courses in courses_file:
#         courses = courses.strip()
#         parts= courses.split(',')
#         print(f'Course title {parts[0]}, Price {parts[1]}')
max_age = -1
min_age = 0
with open('people.txt') as people:
    for person in people:
        person = person.strip()
        person = person.split()
        name = person[0]
        age = int(person[1])
        if age > max_age:
            max_age = age
            min_age = max_age
        if age < min_age:
            min_name = name
            min_age = age
        print(f'{name} {age} ')
        
    print(max_age)
    print(min_age)
    print(min_name)