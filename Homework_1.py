import datetime
# ================================= Task 1 =======================================
# Get input from user as number
while True:
    try:
        number = int(input('Please input a number: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

print(f'Your number is: {number}')

# Get input from user as a string
while True:
    string = input('Please input a string: ')
    if string.isalpha():
        break

print(f'Your string is: {string}')

# ================================= Task 2 =======================================
# Convert user input in seconds into format hh.mm.ss
while True:
    try:
        time_in_seconds = int(input('Please input a number in seconds: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

conversion = datetime.timedelta(seconds=time_in_seconds)
converted_time = str(conversion)

print(f'Time is: {converted_time}')

# ================================= Task 3 =======================================
# Get sum of concat numbers
results = []
total = 0
final_value = 0
while True:
    try:
        user_input = int(input('Please input a number: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

for num in range(1, user_input + 1):
    total = int((str(user_input) * num))
    final_value += total
    results.append(total)

for i in range(len(results)):
    if i > 0 and i != len(results):
        print(' + ', end='')
    print(f'{int(results[i])}', end='')

print(f' = {final_value}')

# ================================= Task 4 =======================================
# Find the biggest value in the user input
while True:
    try:
        whole_number = int(input('Please input a number: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

max_number = max(str(whole_number))
print(f'The biggest value in: {whole_number} is:{max_number}')

# ================================= Task 5 =======================================
# Calc company profit in percentage depends on workers qty
profit = 0
while True:
    try:
        income = int(input('Please input company income: '))
        expense = int(input('Please input company expense: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

if income > expense:
    print('Oh my, your company is going up the hill')
    profit = income - expense
    while True:
        try:
            workers_qty = int(input('So how many employees in your company: '))
            break
        except ValueError:
            print('Wrong input, Please try again.')

    profit_per_employee = profit / workers_qty
    print(f'All right, so it\'s {profit_per_employee} per one employee\n'
          f'So, how about if I borrow from you tenner?')
elif income < expense:
    print('Well, you need to change the strategy, or you will lose everything')

# ================================= Task 6 =======================================
# Calculate the progress of the runner
days = 0
while True:
    try:
        distance = int(input('Please input runner distance for the first day: '))
        target = int(input('Please input runner target of the distance: '))
        break
    except ValueError:
        print('Wrong input, Please try again.')

print(f'Result:\n')
while True:
    days += 1
    if days >= 2:
        distance += distance * 10 / 100
    print(f'day {days}: {round(distance, 2)}')
    if distance > target:
        break

print(f'On day {days} the runner achieved a result at least {int(distance)}')
