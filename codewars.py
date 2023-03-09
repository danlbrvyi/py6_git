# def down(string):
#     return string.lower()
#
# def up(string):
#     return string.upper()
#
# list_strings = 'I lOvE ALL WoRLd'.split()
# print(list(map(down, list_strings)))
# print(list(map(up, list_strings)))



# print('1. Число является положительным, отрицательным или это число ноль?')
# number = int(input('Введите число: '))
# if number > 0:
#     print('Это положительное число')
# elif number < 0:
#     print('Это отрицательное число')
# else:
#     print('Это ноль')
#
# print('2. Проверка, содержит ли строка определенные слова?')
# string = 'Hello, world!'
# test_string = input('Введите слово: ')
# if test_string.lower() in string.lower() or test_string.upper() in string.upper():
#     print('Строка содержит слово ' + test_string)
# else:
#     print('Строка НЕ содержит слово ' + test_string)
#
# print('3. Проверка, имеют ли две строки одинаковую длину?')
# string1 = input('Введите первое слово: ')
# string2 = input('Введите второе слово: ')
# if len(string1) == len(string2):
#     print('Строки имеют одинаковую длину')
# else:
#     print('Строки имеют разную длину')
#
# print('4. Проверка, является ли число четным?')
# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Это число чётное')
# else:
#     print('Это число нечётное')
#
# print('5. Проверка, является ли число1 кратным число2 и число3?')
# number = int(input('Введите главное число: '))
# check_num1 = int(input('Введите первое проверяющее число: '))
# check_num2 = int(input('Введите второе проверяющее число: '))
# if number % check_num1 == 0 and number % check_num2 == 0:
#     print('Главное число кратное проверяющим числам')
# else:
#     print('Главное число НЕ кратное проверяющим числам')

# print('6. Проверка, является ли каждая цифра в числе четной:?')
# number = int(input('Введите число: '))
# all_digits_even = True
#
# for digit in str(number):
#     if int(digit) % 2 != 0:
#         all_digits_even = False
#         break
#
# if all_digits_even:
#     print('Каждая цифра в числе является четной')
# else:
#     print('Число содержит нечетные цифры')

number = int(input('Введите число: '))

def square(number):
    print(number ** 2)

def prostoe_number(number):
    if number < 2:
        return print('Число НЕ простое')
    elif number > 2:
        for i in range(2, 11):
            if number % i == 0:
                return print('Число НЕ простое')
            else:
                return print('Число простое')
    else:
        #для числа 2
        return print('Число простое')

square(number)
prostoe_number(number)


