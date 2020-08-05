import os
import ast


def press_any_key():
    return input('\nPress any key')


def clear():
    return os.system('cls')


def menu():
    clear()
    print('10 Awesome Pythonic One Lienrs\n')
    print('Menu:\n')
    print('1. Swap two variables')
    print('2. Multiple variable assignment')
    print('3. Sum over every second element of a list')
    print('\n0. Exit\n')
    choice = int(input('Choice: '))
    if choice == 0:
        press_any_key()
        exit()
    elif choice == 1:
        swap()
        press_any_key()
        clear()
        menu()
    elif choice == 2:
        multi()
        press_any_key()
        clear()
        menu()
    elif choice == 3:
        sum_second()
        press_any_key()
        clear()
        menu()


def swap():
    clear()
    print("""Let's start with a classic: swapping the values of variables
by simply swapping positions on assignment - the most
intuitive way in my opinion. No need to use a temporary
variable. It even works with more than two variables.\n""")
    try:
        a = int(input('Input a: '))
        b = int(input('Input b: '))
    except:
        print('Incorrect input, using default values:')
        a = 1
        b = 2
    print(f'\n# a = {a}; b = {b}')
    print('a, b = b, a')
    a, b = b, a
    print(f'# print(a,b) >> {a} {b}')


def multi():
    clear()
    print('''Swapping variables is actually a special case of Pythons
ability to assign multiple variables at once. Here you can
use it to assign list elements to the given variables,
which is also called unpacking. The * will do packing
the remaining values again, which results in a sublist for
c. It even works for every other position of * (e.g. the
beginning or middle part of the list).\n''')
    try:
        var_list = input('Input list [1,2,3,4,5]: ')
        var_list = ast.literal_eval(var_list)
        if not isinstance(var_list, list):
            print('Using default values [1,2,3,4,5]')
            var_list = []
            var_list = [1, 2, 3, 4, 5]
    except:
        if isinstance(var_list, str):
            print('Using default values [1,2,3,4,5]')
        else:
            print('Incorrect input, using default values [1,2,3,4,5]')
        var_list = []
        var_list = [1,2,3,4,5]
    a, b, *c = var_list
    print(f'\na, b, *c = {var_list}')
    print(f'# print(a,b,c) >> {a, b, c}')


def sum_second():
    clear()
    print('''No need for a special reduce function here, sum just 
adds the items of every given iterable. The extended 
slicing syntax [::] is used here to return every second 
element. You can read it as [start : stop : step], so [1::2] 
translates to start with the element of index 1 (second 
element), don't stop until the list ends (no argument given 
for second parameter) and always take 2 steps.''')
    try:
        var_list = input('\nInput list [1,2,3,4,5,6]: ')
        var_list = ast.literal_eval(var_list)
        if not isinstance(var_list, list):
            print('Using default values [1,2,3,4,5,6]')
            var_list = []
            var_list = [1, 2, 3, 4, 5, 6]
    except:
        if isinstance(var_list, str):
            print('Using default values [1,2,3,4,5,6]')
        else:
            print('Incorrect input, using default values [1,2,3,4,5,6]')
        var_list = []
        var_list = [1, 2, 3, 4, 5, 6]
    print(f'\n# a = {var_list}')
    s = sum(var_list[1::2])
    print('s = sum(a[1::2])')
    print(f'# print(s) >> {s}')


menu()
# static to active, let user input all variables, ex. sum_second: enter list of vars (default[1,2,3,4,5,6] >
# if no option or bad input use default, else use user inputs
