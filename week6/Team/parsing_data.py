with open('hr_system.txt') as systemdata:
    for data in systemdata:
        data = data.strip()
        data = data.split()
        name = data[0]
        id_number = int(data[1])
        job_title = data[2]
        salary = float(data[3])

        paycheck = salary/24
        
        if job_title == 'Engineer':
            paycheck = paycheck + 1000

        print(f'{name} (ID: {id_number}), {job_title} - ${paycheck:.2f}')
        