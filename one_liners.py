import os


def press_any_key():
    return input('\nPress any key')


def clear():
    return os.system('cls')


def menu():
    print('Menu:\n')
    print('1. Swap two variables')
    print('2. Multiple variable assignment')
    print('3. Sum over every second element of a list')
    print('0. Exit\n')
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
    print('Swapping the values of variables by simply swapping positions on assignment:\n')
    a = int(input('a = '))
    b = int(input('b = '))
    print('\n# Swapping:\n>> a, b = b, a')
    a, b = b, a
    print(f'\nResult:\na = {a}\nb = {b}')


def multi():
    clear()
    print('Swapping variables is actually a special case of Pythons ability to assign multiple variables at once:\n')
    print('a, b, *c = [1,2,3,4,5]')
    print('# print(a,b,c) >> 1 2 [3, 4, 5]')


def sum_second():
    clear()
    print("Sum just adds the items of every given iterable."
          "\nThe extended slicing syntax [::] is used here to return every second element."
          "\nYou can read it as [start : stop : step], so [1::2] translates to start with the element of index 1 (second element),"
          "\ndon't stop until the list ends (no argument given for second parameter) and always take 2 steps:\n")
    print('# a = [1,2,3,4,5,6]')
    print('s = sum(a[1::2])')
    print('# print(s) >> 12')


clear()
print('Welcome to 10 Awesome Pythonic One Lienrs\n')
menu()
