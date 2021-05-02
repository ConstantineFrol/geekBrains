import sys

# =============================== Task 1 ===============================
print('=' * 30, ' Task 1 ', '=' * 30)


# Run-app from terminal: python Homework_4.py 8 12.50 100

def validate_args(arguments):
    if len(arguments) != 4:
        print('Error, expecting 3 parameters:\n'
              'Hours, Hourly rate, Bonus')
        sys.exit()


def calc_wage(work_hours=int, per_hour=float, extra_bonus=float) -> float:
    wage = (int(work_hours) * float(per_hour)) + float(extra_bonus)
    print(f'Your wage is: {wage}')


if __name__ == '__main__':
    validate_args(sys.argv)
    try:
        hours = sys.argv[1]
        hourly_pay = sys.argv[2]
        bonus = sys.argv[3]
        calc_wage(hours, hourly_pay, bonus)
    except (IndexError, ValueError):
        print('Invalid input, please try again')

# =============================== Task 2 ===============================

print('=' * 30, ' Task 2 ', '=' * 30)

result = []
rand_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

for i in range(1, len(rand_list)):
    if rand_list[i] > rand_list[i - 1]:
        result.append(rand_list[i])

print(result)
# OR Lambda exp.  [_ - means no matter what var name]🤓
print([rand_list[_] for _ in range(1, len(rand_list)) if rand_list[_] > rand_list[_ - 1]])

# =============================== Task 3 ===============================

print('=' * 30, ' Task 3 ', '=' * 30)

print([el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0])

# =============================== Task 4 ===============================

print('=' * 30, ' Task 4 ', '=' * 30)
# rand_gen_list = [random.randint(1, 100) for el in range(1, 11)]
rand_gen_list = [2, 2, 2, 7, 23, 1, 44, 3, 2, 10, 7, 4, 11]
# Remove all duplicates
print([val for val in rand_gen_list if rand_gen_list.count(val)])
# Remove all appears at least once
print([element for element in rand_gen_list if rand_gen_list.count(element) == 1])

print(list(dict.fromkeys(rand_gen_list)))

# =============================== Task 5 ===============================
from functools import reduce

print('=' * 30, ' Task 5 ', '=' * 30)


def add_two_num(a, b):
    return a * b


my_list = ([el for el in range(100, 1001) if el % 2 == 0])

print(reduce(add_two_num, my_list))

# =============================== Task 6 ===============================
import sys

# To run this file run in terminal:  python Homework_4.py <any number>
print('=' * 30, ' Task 6 ', '=' * 30)

from itertools import cycle, count


def count_my_list_el(a):
    for el in count(a):
        if el >= a + limit:
            print('\n')
            break
        else:
            print(el, ', ', end='')


def circle_my_list(a):
    counter = 0
    for el in cycle(a):
        counter += 1
        print(el, ', ', end='')
        if count == limit:
            print(f' printed {counter} times')
            break


if __name__ == '__main__':
    limit = 10
    starting_no = int(sys.argv[1])
    my_list = [el for el in range(starting_no, starting_no + 6)]
    circle_my_list(my_list)
    count_my_list_el(starting_no)

# =============================== Task 7 ===============================

print('=' * 30, ' Task 7 ', '=' * 30)

factorial_list = []
number = 4


def print_factorial(num):
    result = 0
    if num == 1:
        result = 1
    else:
        temp_val = yield from print_factorial(num - 1)
        result = num * temp_val
    yield result
    return result


for i in print_factorial(number):
    factorial_list.append(i)

print(f'Factorial of {number}! is: ', end='')
print(*factorial_list[:-1], sep=' * ', end='')
print(f' = {factorial_list[-1]}')
