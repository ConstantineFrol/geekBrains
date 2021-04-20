# ================================================== Task 1 ==================================================
empty_list = []
my_list = [3452, 'hello', -35, 645, 4356, 'd', 'dfg', True, None, False, empty_list]


def check_type(some_list):
    for item in some_list:
        print(f'{item} is type of: {type(item)}')


check_type(my_list)

# ================================================== Task 2 ==================================================
# Get input without any validation
my_list2 = []
while len(my_list2) < 6:
    user_data = input('Please input any data: ')
    my_list2.append(user_data)


def swap_items(user_list):
    index = 0
    while index < len(user_list) - 1:
        user_list[index], user_list[index + 1] = user_list[index + 1], user_list[index]
        index += 2
    return user_list


# Compare results
print(f'{my_list2}')
print(swap_items(my_list2, ))


# ================================================== Task 3 ==================================================
# using dict
def check_month_dict(user_month):
    for season in seasons_1:
        for month in seasons_1[season]:
            if user_month == month:
                print(f'Your month belong to {season}, [used dict version]')
                return True
    return False


# using list
def check_month_list(user_month):
    for month in seasons_2:
        if user_month == month:
            if seasons_2.index(month) <= 2:
                print(f'Your month belong to Winter, [used list version]')
                return True
            elif 3 <= seasons_2.index(month) <= 5:
                print(f'Your month belong to Spring, [used list version]')
                return True
            elif 6 <= seasons_2.index(month) <= 8:
                print(f'Your month belong to Summer, [used list version]')
                return True
            elif 9 <= seasons_2.index(month) <= 12:
                print(f'Your month belong to Autumn, [used list version]')
                return True
    return False


seasons_1 = {'Winter': ['December', 'January', 'February'],
             'Spring': ['March', 'April', 'May'],
             'Summer': ['June', 'July', 'August'],
             'Autumn': ['September', 'October', 'November']}

seasons_2 = ['December', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
             'October', 'November']

while True:
    user_input = input('Please input a month: ')
    if user_input.isalpha():
        month = user_input[0].upper() + user_input[1:]
        result1 = check_month_dict(month)
        result2 = check_month_list(month)
        if result1 and result2:
            break
        else:
            print('no such month, try again')
            continue
    else:
        print('Incorrect input, try again')

# ================================================== Task 4 ==================================================
# get input with no validation
user_sentence = input('Please input any sentence: ')

my_list3 = user_sentence.split()
print(f'your list: {my_list3}')
for word in my_list3:
    if len(word) > 10:
        print(f'{my_list3.index(word) + 1}: {word[:10]}')
    else:
        print(f'{my_list3.index(word) + 1}: {word}')

# ================================================== Task 5 ==================================================
my_list4 = [7, 5, 3, 3, 2]

while len(my_list4) < 10:
    try:
        number = int(input('Please input a number: '))
        my_list4.append(number)
        print(sorted(my_list4, reverse=True))
    except ValueError:
        print('Wrong input, Please try again.')

# ================================================== Task 6 ==================================================
items = (1, {'item_name': 'pc', 'price': '20000', 'qty': '5', 'qty_type': 'pcs'}), (
    2, {'item_name': 'printer', 'price': '6000', 'qty': '2', 'qty_type': 'pcs'}), (
            3, {'item_name': 'scanner', 'price': '2000', 'qty': '7', 'qty_type': 'pcs'})

new_dict = {k: [v[1][k] for v in items] for k in items[0][1].keys()}
for item in new_dict:
    print(item, new_dict[item])
