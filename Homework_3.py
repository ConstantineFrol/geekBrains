# # =============================== Task 1 ===============================
print('=' * 30, ' Task 1 ', '=' * 30)


def divide_digit(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'You can\'t divide by zero'


def ask_number(text):
    while True:
        try:
            number = int(input(text))
            break
        except ValueError:
            print('Wrong input, Please try again: ')
    return number


print(divide_digit(ask_number('Please input first number: '), ask_number('Please input second number: ')))

# =============================== Task 2 ===============================
print('=' * 30, ' Task 2 ', '=' * 30)


def ask_word(text):
    while True:
        string = input(text)
        if string.isalpha():
            return string
        else:
            print('Invalid input, please try again: ')


def check_input_len(word, length):
    result = str(word)
    if result.isdigit():
        while len(str(result)) < length:
            result = ask_number('Your input is too short, try another one: ')
        return result
    else:
        while len(result) < length:
            result = ask_word('Your input is too short, try another one: ')
        return result


def display_info(f_name, l_name, yob, town='none', email='none', phone_number=0) -> object:
    return f'user-info:\t{f_name}\t|\t{l_name}\t|\t{yob}\t|\t{town}\t|\t{email}\t|\t{phone_number}'


print(display_info(
    check_input_len(ask_word('first name: '), 3),
    check_input_len(ask_word('last name: '), 3),
    check_input_len(ask_number('date of birth: '), 4),
    ask_word('town: '),
    ask_word('email: '),
    ask_number('phone number: ')))

# =============================== Task 3 ===============================
print('=' * 30, ' Task 3 ', '=' * 30)


def sum_biggest_digits(*args):
    sorted_digits = tuple(sorted(args, reverse=True))
    return sorted_digits[0] + sorted_digits[1]


print(sum_biggest_digits(ask_number('Input first number: '), ask_number('Input second number: '),
                         ask_number('Input third number: ')))

# =============================== Task 4 ===============================
print('=' * 30, ' Task 4 ', '=' * 30)


def digit_into_power(digit, power):
    temp_digit = digit
    print(f'using **: {digit ** power}')
    times = range(power - 1)
    for moment in times:
        temp_digit *= digit
    print(f'using loop: {temp_digit}')


digit_into_power(ask_number('Input a number: '), ask_number('Input power : '))

# =============================== Task 5 ===============================
print('=' * 30, ' Task 5 ', '=' * 30)


def get_sum():
    user_data = []
    fulfil = True
    while True:
        result = 0
        user_data.append(input('For quit press \'q\', or input a number(s): '))
        separator = ' '
        temp_list = (separator.join(user_data))
        for item in temp_list:
            if item == 'q':
                temp_list = temp_list[:-1]
                fulfil = False
                break
        for i in temp_list:
            if i == ' ':
                continue
            else:
                result += int(i)
        print(f'result: {result}')
        if not fulfil:
            break


get_sum()

# =============================== Task 6 ===============================
print('=' * 30, ' Task 6 ', '=' * 30)
some_string = 'if you would like to join me'
print(f'Original string: {some_string}')


def get_string(text=str) -> str:
    return text.title()


print(get_string(some_string))
