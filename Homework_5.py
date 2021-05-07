import re

# =============================== Task 1 ===============================
from functools import reduce

print('=' * 30, ' Task 1 ', '=' * 30)

file_name1 = 'file_1.txt'
file_name2 = 'task_3.txt'
file_name3 = 'task_4.txt'
file_name4 = 'task_5.txt'
file_name5 = 'task_6.txt'


def write_into_file(file, text):
    with open(file, 'a') as file_1:
        file_1.write(text + '\n')
        # OR write using print method
        # print(f'Added using print(): {text}', file=file_1)


 user_typing = True
 print('input some text, to stop: input an empty string')
 while user_typing:
     tmp_data = ''
     tmp_data = input(': ')
     write_into_file(file_name1, tmp_data)
     if tmp_data == '':
         user_typing = False

# =============================== Task 2 ===============================
print('=' * 30, ' Task 2 ', '=' * 30)


def count_words_in_line(file):
    counter = 0
    print(f'The file: {file} contains:')
    file_data = open(file, 'r')
    for line in file_data:
        counter += 1
        words_in_line = len(line.split())
        print(f'line No: {counter}, number of words: {words_in_line}')
    file_data.close()


# count_words_in_line(file_name1)

# =============================== Task 3 ===============================
print('=' * 30, ' Task 3 ', '=' * 30)

# import random

names_list = ['Alex', 'John', 'Frank', 'Lucky', 'Bridget', 'Luise']


# This code create data in the file [name wage\n]
# for name in names_list:
#     write_into_file(file_name2, f'{name}  {random.randint(10000, 100000)}')


def find_avr_wage(file):
    tmp_list = []
    avg_wage = 0
    counter = 0
    with open(file, 'r') as read_f:
        file_data_1 = read_f.read().splitlines()
        print(f'Data from file:/n{file_data_1}')
        for el in file_data_1:
            for word in el.split(' '):
                if word.isdigit():
                    avg_wage += int(word)
                    counter += 1
                    if int(word) > 20000:
                        tmp_list.append(list(next(zip(*map(str.split, el.split(','))))))
    lucky_list = [item for sublist in tmp_list for item in sublist]
    print(f'Average Wage is: ${round((avg_wage / counter), 2)}')
    print(f'Those workers wage is higher than $20.000:')
    for employee in lucky_list:
        print(employee)


# find_avr_wage(file_name2)

# =============================== Task 4 ===============================
print('=' * 30, ' Task 4 ', '=' * 30)

# This code Create new File(task_3.txt) write into file data from a list(some_data)
# some_data = ['One - 1', 'Two - 2', 'Three - 3', 'Four - 4']
# for el in some_data:
#     write_into_file(file_name3, f'{el}')

template = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


def do_translation(file):
    with open(file, 'r') as f_data:
        tmp_list = []
        en_version = f_data.readlines()
        print(f'orig:{en_version}')
        for el in en_version:
            el = el.split(' ', 1)
            tmp_list.append(f'{template.get(el[0])} {el[1]}')
    with open(file, 'w') as into_file:
        into_file.writelines(tmp_list)


# do_translation(file_name3)

# =============================== Task 5 ===============================
print('=' * 30, ' Task 5 ', '=' * 30)


def get_digits_from_user():
    numbers = []
    user_typing = True
    while user_typing:
        sentence = input('Please input some numbers: ')
        for word in sentence.split():
            if word.isdigit():
                numbers.append(int(word))
        user_typing = False
    return numbers


def create_data_file(file_name):
    digits_list = get_digits_from_user()

    for el in digits_list:
        with open(file_name, 'a') as file_data:
            file_data.write(str(el) + ' ')


def get_sum(file_name):
    print(sum(float(num) for num in re.findall('[0-9]+', open(file_name, 'r').read())))


# create_data_file(file_name4)
# get_sum(file_name4)

# =============================== Task 6 ===============================
print('=' * 30, ' Task 6 ', '=' * 30)


def collect_file_data(file_name):
    tmp_list = []
    collage_data = {}
    with open(file_name, 'r') as rfile:
        data = rfile.readlines()
        for element in data:
            tmp_data = element.split(' ', 1)
            collage_data[tmp_data[0]] = (
                reduce(lambda x, y: x + int(y), (y for y in tmp_data[1].split() if y.isdigit()), 0))
        return collage_data


# print(collect_file_data(file_name5))

# =============================== Task 7 ===============================
print('=' * 30, ' Task 7 ', '=' * 30)

write_into_file()
