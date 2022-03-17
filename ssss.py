# def is_permutation(a: str, b: str) -> bool:
#     # Нужно проверить, являются ли строчки 'a' и 'b' перестановками
#     if sorted(a) == sorted(b):
#         return True
#     else:
#         return False
#
#
#
# print(is_permutation("abbba", "abab"))
# assert is_permutation("baba", "abab")  # True
# assert is_permutation("abbba", "abab")  # False

"""Пароль является надежным если:

его длина не менее 88 символов;
он содержит как минимум одну заглавную букву (верхний регистр);
он содержит как минимум одну строчную букву (нижний регистр);
он содержит хотя бы одну цифру."""

# def is_password_good(password):
#     pas_upper, pas_lower, pas_digit, pass_result = False, False, False, False
#     if len(password) >= 8:
#         for symbol in password:
#             if symbol.isalpha():
#                 if symbol == symbol.upper():
#                     pas_upper = True
#                 if symbol == symbol.lower():
#                     pas_lower = True
#             if symbol.isdigit():
#                 pas_digit = True
#             if pas_digit == True and pas_lower == True and pas_upper == True:
#                 pass_result = True
#                 break
#     return pass_result
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))


'''Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два 
слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и о
тличаются ровно в 1 символе и False в противном случае.'''

# # объявление функции
# def is_one_away(word1, word2):
#     count = 0
#     if len(word1) == len(word2):
#         for i in range(len(word1)):
#             if word1[i] != word2[i]:
#                 count += 1
#     if count == 1:
#         return True
#     else:
#         return False
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

# # объявление функции проверки не палиндром
# def is_palindrome(text):
#     text = ''.join(i for i in text if i.isalpha())
#     return text.lower() == text[::-1].lower()
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_palindrome(txt))

"""a:b:c, где a, b и c – натуральные числа

число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным."""
# объявление функции
# def is_valid_password(password):
#     palindrome, simple, even = False, False, False
#     password = password.split(':')
#     if len(password) == 3:
#         if password[0] == password[0][::-1]:
#             palindrome = True
#         d = 2
#         while d * d <= int(password[1]) and int(password[1]) % d != 0:
#             d += 1
#         if d * d > int(password[1]):
#             simple = True
#         if int(password[2]) % 2 == 0:
#             even = True
#     return palindrome and simple and even
#
# # считываем данные
# psw = input()
#
# # вызываем функцию
# print(is_valid_password(psw))

'''Напишите функцию is_correct_bracket(text), которая принимает в качестве 
аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение 
True если поступившая на вход строка является правильной скобочной последовательностью 
и False в противном случае.'''

# # объявление функции
# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replace('()', '')
#     return True if len(text) == 0 else False
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))
'''Напишите функцию convert_to_python_case(text), которая принимает в 
качестве аргумента строку в «верблюжьем регистре» и преобразует 
его в «змеиный регистр».'''
# объявление функции


# def convert_to_python_case(text):
#     result = ''
#
#     for i in text:
#         if i.isupper():
#             result += '_' + i.lower()
#         else:
#             result += i
#     return result[1::]
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))
'''https://stepik.org/lesson/334314/step/3?unit=317733'''
# объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x_sol = (x1 + x2)/2
#     y_sol = (y1 + y2)/2
#     return x_sol, y_sol
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# # объявление функции
# def compute_binom(n, k):
#     compute = factorial(n)/(factorial(k) * factorial(n - k))
#     return int(compute)
#
# def factorial(num):
#     result = 1
#     for i in range(2, num + 1):
#         result *= i
#     return result

# считываем данные
# n = int(input())
# k = int(input())

# вызываем функцию
# print(compute_binom(n, k))
'''Напишите функцию number_to_words(num), которая принимает в качестве 
аргумента натуральное число num и возвращает его словесное описание на русском языке.'''
# # объявление функции
# def number_to_words(num):
#     d = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь',
#     8: 'восемь', 9: 'девять', 10: 'десять', 11: 'одиннадцать', 12: 'двенадцать',
#     13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать',
#     17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать', 20: 'двадцать',
#     30: 'тридцать', 40: 'сорок', 50: 'пятьдесят', 60: 'шестьдесят', 70: 'семьдесят',
#     80: 'восемьдесят', 90: 'девяносто'}
#     if num > 20 and num not in (30, 40, 50, 60, 70, 80, 90):
#         first_num = num//10 * 10
#         second_num = num % 10
#         first_num = d[first_num]
#         second_num = d[second_num]
#         return f'{first_num} {second_num}'
#     else:
#         return f'{d[num]}'
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))

'''Напишите функцию get_month(language, number), которая принимает на вход два 
аргумента language – язык ru или en и number – номер месяца (от 1 до 12) 
и возвращает название месяца на русском или английском языке.'''

# # объявление функции
# def get_month(language, number):
#     ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август',
#               'сентябрь', 'октябрь', 'ноябрь','декабрь']
#
#     en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august',
#               'september', 'october', 'november', 'december']
#     if language == 'ru':
#         return ru[number - 1]
#     else:
#         return en[number - 1]
#
# # считываем данные
# lan = input()
# num = int(input())
#
# # вызываем функцию
# print(get_month(lan, num))

'''Магическая дата – это дата, когда день, умноженный на месяц, равен числу 
образованному последними двумя цифрами года.

Напишите функцию, is_magic(date) которая принимает в качестве аргумента 
строковое представление корректой даты и возвращает значение True если дата 
является магической и False в противном случае.'''

# # объявление функции
# def is_magic(date):
#     flag = False
#     d, m, g = map(int, date.split('.'))
#     if d * m == g % 100:
#         flag = True
#     return flag
#
# # считываем данные
# date = input()
#
# # вызываем функцию
# print(is_magic(date))

'''Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно 
панграммы используют для презентации шрифтов, чтобы можно было в одной фразе 
рассмотреть все глифы.

Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку 
текста на английском языке и возвращает значение True если текст является панграммой
 и False в противном случае.'''

# # объявление функции
# def is_pangram(text):
#     flag = True
#     for i in range(97, 123):
#         if chr(i) not in text.lower():
#             flag = False
#             break
#     return flag
#
# # считываем данные
# text = input()
#
# # вызываем функцию
# print(is_pangram(text))

# res = 0
# for i in range(int(input())):
#        res += int(input())
# print(res)


# x = [1, 2, 3]
# y = x
# y *= 2
# print(y)
# print(x)
# print(id(x) == id(y))

# objects = [1, 2, 1, 2, 3]
# result = set()
# for obj in objects:
#     result.add(id(obj))
# print(len(result))

# # создание класса Vehicle
# class Vehicle:
#     def print_details(self):
#         print("Это родительский метод из класса Vehicle")
#
#
# # создание класса, который наследует Vehicle
# class Car(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Car")
#
#
# # создание класса Cycle, который наследует Vehicle
# class Cycle(Vehicle):
#     def print_details(self):
#         print("Это дочерний метод из класса Cycle")
#
#
# car_a = Vehicle()
# car_a.print_details()
#
# car_b = Car()
# car_b.print_details()
#
# car_c = Cycle()
# car_c.print_details()


# from math import sqrt
#
#
# def easy(a, b):
#     summ = a + b
#     difference = a - b
#     composition = a * b
#     quotient = a / b
#     whole_part = a // b
#     remainder_of_division = a % b
#     square_root = sqrt(a ** 10 + b ** 10)
#     return f'{summ}\n{difference}\n{composition}\n{quotient}\n{whole_part}\n{remainder_of_division}\n{square_root}'
#
#
# print(easy(int(input()), int(input())))

#
# def imt(weight, height):
#     result = weight / (height * height)
#     if 18.5 <= result <= 25:
#         conclusion = 'Оптимальная масса'
#     elif result < 18.5:
#         conclusion = 'Недостаточная масса'
#     else:
#         conclusion = 'Избыточная масса'
#     return conclusion
#
#
# print(imt(int(input()), float(input())))


# def taxes(string):
#     symbols = len(string)
#     price = symbols * 60
#     result = f'{price//100} р. {price % 100} коп.'
#     return result
#
#
# print(taxes(input()))

# print(len([i for i in input().split()]))

# animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь",
# "Овца"] year = int(input()) % 12 print(animals[year])


# def reverse(num):
#     num = str(num)
#     if len(num) == 5:
#         num = num[::-1]
#     elif len(num) == 6:
#         num = num[0] + num[:0:-1]
#     i = 0
#     while num.startswith('0'):
#         num = num[i:]
#         i += 1
#     return num
#
#
# print(reverse(input()))


# def convention(num):
#     result = ''
#     for i in range(1, len(num) + 1):
#         result += num[-i]
#         if i % 3 == 0 and i != len(num):
#             result += ','
#     return result[::-1]
#
#
# print(convention(input()))


'''Задача Иосифа Флавия 🌶️🌶️
nn человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться, 
каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним.'''

# n, k = int(input()), int(input())
# result = 0
# for i in range(1, n + 1):
#     result = (result + k) % i
# print(result + 1)


#
# n = int(input())
# first, second, third, fourth = 0, 0, 0, 0
# for _ in range(n):
#
#     x, y = (int(i) for i in input().split())
#     if x > 0:
#         if y > 0:
#             first += 1
#         elif y < 0:
#             fourth += 1
#     elif x < 0:
#         if y > 0:
#             second += 1
#         elif y < 0:
#             third += 1
#
# print(f'Первая четверть: {first}\n\
# Вторая четверть: {second}\n\
# Третья четверть: {third}\n\
# Четвертая четверть: {fourth}')

# '''Больше предыдущего
# На вход программе подается строка текста из натуральных чисел. Из неё формируется список чисел.
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом. '''
#
#
# nums = [int(i) for i in input().split()]
#
# count = 0
# for i in range(1, len(nums)):
#     if nums[i] > nums[i - 1]:
#         count += 1
# print(count)

'''Назад, вперёд и наоборот
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. 
Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и т.д.). 
Если в списке нечетное количество элементов, то последний остается на своем месте.'''

# nums = [int(i) for i in input().split()]
# for i in range(0, len(nums) - 1, 2):
#     nums[i], nums[i + 1] = nums[i + 1], nums[i]
# print(*nums)


'''Сдвиг в развитии
На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется 
список чисел. Напишите программу циклического сдвига элементов списка направо, когда последний элемент 
становится первым, а остальные сдвигаются на одну позицию вперед, в сторону увеличения индексов.'''
# nums = [int(i) for i in input().split()]
# result = [nums[-1]]
# for i in range(len(nums) - 1):
#     result.append(nums[i])
# print(*result)

'''Различные элементы
На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. 
Из строки формируется список чисел. Напишите программу для подсчета количества разных элементов в списке.'''

# nums = [int(i) for i in input().split()]
# print(len(set(nums)))


'''Произведение чисел
Напишите программу для определения, является ли число произведением двух чисел из данного набора,
выводящую результат в виде ответа «ДА» или «НЕТ».'''

# from itertools import combinations
#
# nums = [int(input()) for i in range(int(input()))]
# check_num = int(input())
# flag = False
# for i in combinations(nums, 2):
#     num = i[0] * i[1]
#     if num == check_num:
#         flag = True
#         break
# print('ДА' if flag == True else 'НЕТ')


''' Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили 
сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать 
очередной модуль нового курса.'''

# rules = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#      'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
#      "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}
#
# tim_rus = f'{input()}-{input()}'
# print(rules[tim_rus])


'''Орел и решка
Дана строка текста, состоящая из букв русского алфавита "О" и "Р". Буква "О" – соответствует выпадению Орла, 
а буква "Р" – соответствует выпадению Решки. Напишите программу, которая подсчитывает наибольшее количество 
подряд выпавших Решек.'''

# s = sorted([i for i in input().split('О')])
# print(len(s[-1]))

'''Кремниевая долина 🌶️🌶️
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в 
качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней 
присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то 
холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы'''
# result = 0
# for _ in range(int(input())):
#     result += 1
#     string = input()
#     count = 0
#     for i in 'anton':
#         if i in string:
#             count += 1
#             string = string[string.find(i):]
#     if count == 5:
#         print(result, end=' ')

# '''Необходимо написать программу, реализующую алгоритм написания этой песни. Алгоритм выводит в конце
# предложения следующую в алфавитном порядке букву, если она встречается в строке текста, а очередную строку
# отображает уже без этой буквы.'''
# string = f'{input()} запретил букву '
#
# abc_list = [chr(i) for i in range(ord('а'), ord('я') + 1)]
# for i in abc_list:
#     if i in string:
#         print(string + i)
#         string = string.replace(i, '').replace('  ', ' ').lstrip()

'''Дополните приведенный код, используя цикл for и встроенную функцию max(), чтобы он выводил один общий 
максимальный элемент среди всех элементов вложенных списков list1.'''

# list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# maximum = -1
# for block in list1:
#     if max(block) >= maximum:
#         maximum = max(block)
# print(maximum)

'''Дополните приведенный код так, чтобы список list1 имел вид:

list1 = [[8, 7, 1], [102, 7, 9], [105, 106, 102], [103, 98, 99, 100], [3, 2, 1]]'''

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
#
# for el in list1:
#     el.reverse()
# print(list1)

'''Дополните приведенный код так, чтобы он выводил единственное число: сумму всех чисел 
списка list1 разделённую на общее количество всех чисел.'''

# list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
# total = 0
# counter = 0
# for block in list1:
#     for el in block:
#         total += el
#         counter += 1
# result = total/counter
# print(result)

'''Треугольник Паскаля 1 🌶️
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. 
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

0:      1
1:     1 1
2:    1 2 1
3:   1 3 3 1
4:  1 4 6 4 1
      .....
На вход программе подается число nn. Напишите программу, которая возвращает указанную строку треугольника 
Паскаля в виде списка (нумерация строк начинается с нуля).'''

# def pascal(rows):
#     result = []
#     for i in range(rows + 1):
#         temp_list = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 temp_list.append(1)
#             else:
#                 temp_list.append(result[i - 1][j - 1] + result[i - 1][j])
#         result.append(temp_list)
#     for el in range(rows ):
#         print(*result[el])
#
#
# pascal(int(input()))

'''Упаковка дубликатов 🌶️
На вход программе подается строка текста, содержащая символы. Напишите программу, которая упаковывает
 последовательности одинаковых символов заданной строки в подсписки.'''

# symbols = input().split()
# result = [[symbols[0]]]
# for i in range(1, len(symbols)):
#     if symbols[i] == symbols[i - 1]:
#         result[-1].append(symbols[i])
#     else:
#         result.append([symbols[i]])
# print(result)

'''Разбиение на чанки 🌶️
На вход программе подаются две строки, на одной символы, на другой число nn. Из первой строки формируется список.

Реализуйте функцию chunked(), которая принимает на вход список и число, задающее размер чанка (куска), а возвращает 
список из чанков указанной длины.'''

# def chunked(symbols, chunk):
#     res = []
#     for i in range(0, len(symbols), chunk):
#         res.append(symbols[:chunk])
#         del symbols[:chunk]
#     return res
#
#
# symbols = input().split()
# print(chunked(symbols, int(input())))

'''
Подсписки списка 🌶️🌶️
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например, 
[1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4] 
не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок
 любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу, 
которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
'''
# nums = input().split()
# result = [[]]
# for i in range(1, len(nums) + 1):
#     for j in range(len(nums) - i + 1):
#         result.append(nums[j:j + i])
# print(result)

'''Вывести матрицу 1
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество 
строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; 
подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.'''
#
# rows, cols = int(input()), int(input())
# result = [[None] * cols for _ in range(rows)]
# for row in range(rows):
#     for col in range(cols):
#         result[row][col] = input()
# for el in result:
#     print(*el, end='\n')

'''На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и 
столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы 
сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую 
строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый 
столбец, и так далее.'''

# rows, cols = int(input()), int(input())
# result = [[None] * cols for _ in range(rows)]
# for row in range(rows):
#     for col in range(cols):
#         result[row][col] = input()
#
# for el in result:
#     print(*el, end='\n')
# print()
# for col in range(cols):
#     for row in range(rows):
#         print(result[row][col], end=' ')
#     print()

'''След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, 
которая выводит след заданной квадратной матрицы.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = 0
# for i in range(n):
#     result += matrix[i][i]
# print(result)

'''Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, 
больших среднего арифметического элементов данной строки.'''
# n = int(input())
# matrix = []
# for _ in range(n):
#     matrix.append([int(i) for i in input().split()])
#
# for el in matrix:
#     count = 0
#     middle = sum(el)/n
#     for num in el:
#         if num > middle:
#             count += 1
#     print(count)

'''Максимальный в области 1
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = []
# for row in range(n):
#     for col in range(n):
#         if row >= col:
#             result.append(matrix[row][col])
# print(max(result))
#
'''Максимальный в области 2 🌶️
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
 '''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = []
# for row in range(n):
#     for col in range(n):
#         if col <= row <= n - 1 - col or col >= row >= n - 1 - col:
#             result.append(matrix[row][col])
# print(max(result))

'''Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, 
левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти; 
нижней четверти; левой четверти.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# left, top, bottom, right = [], [], [], []
# for row in range(n):
#     for col in range(n):
#         if col < row < n - 1 - col:
#             left.append(matrix[row][col])
#         if col > row > n - 1 - col:
#             right.append(matrix[row][col])
#         if row < col and row < n - 1 - col:
#             top.append(matrix[row][col])
#         if row > col and row > n - 1 - col:
#             bottom.append(matrix[row][col])
# print(f'Верхняя четверть: {sum(top)}\n'
#       f'Правая четверть: {sum(right)}\n'
#       f'Нижняя четверть: {sum(bottom)}\n'
#       f'Левая четверть: {sum(left)}')

'''Таблица умножения
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу 
 mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j.'''
# rows, cols = int(input()), int(input())
# mult = [[str(row * col).ljust(3) for col in range(cols)] for row in range(rows)]
# [print(*el) for el in mult]

'''Максимум в таблице
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице, 
затем nn строк по mm целых чисел в каждой, отделенных символом пробела.'''
# row, col = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(row)]
# maximum = max(max(matrix, key=max))
# for i in range(row):
#     for j in range(col):
#         if matrix[i][j] == maximum:
#             print(i, j)
#             break
#     else:
#         continue
#     break

'''Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице.'''
# rows, cols = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(rows)]
# i, j = [int(num) for num in input().split()]
# for row in range(rows):
#     matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
# [print(*el) for el in matrix]

'''Симметричная матрица
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.'''
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# transp_matrix = [[None] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         transp_matrix[j][i] = matrix[i][j]
# print('YES' if transp_matrix == matrix else 'NO')

'''Обмен диагоналей
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной 
и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно 
поменять местами элемент на главной диагонали и на побочной диагонали).'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
# [print(*el) for el in matrix]

'''Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы 
относительно горизонтальной оси симметрии.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix.reverse()
# [print(*el) for el in matrix]

'''Поворот матрицы
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке.'''
# n = int(input())
# matrix = [[i for i in input().split()] for _ in range(n)]
# t_matrix = [[None] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         t_matrix[j][i] = matrix[i][j]
#
# [print(*reversed(el)) for el in t_matrix]

'''Ходы коня
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и 
все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь, 
отметьте символами *, остальные клетки заполните точками.'''
# table = [[None] * 8 for _ in range(8)]
# y, x = (i for i in input())
# trans_y = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# trans_x = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
# for i in range(8):
#     for j in range(8):
#         if (i - trans_x[x]) ** 2 + (j - trans_y[y]) ** 2 == 5:
#             table[i][j] = '*'
#         elif i == trans_x[x] and j == trans_y[y]:
#             table[i][j] = 'N'
#         else:
#             table[i][j] = '.'
# [print(*el) for el in table]

'''Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел 
1, 2, 3, \ldots, n^21,2,3,…,n 
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу, 
которая проверяет, является ли заданная квадратная матрица магическим квадратом.'''
# n = int(input())
# square_nums_check = [int(num) for num in range(1, n ** 2 + 1)]
# sum_of_square, sum_of_main_diag, sum_of_side_diag, square_nums_real = [], 0, 0, []
# magic_square = [[int(i) for i in input().split()] for j in range(n)]
#
# for i in range(n):
#     sum_of_cols = 0
#     sum_of_main_diag += magic_square[i][i]
#     sum_of_side_diag += magic_square[i][n - i - 1]
#     sum_of_square.append(sum(magic_square[i]))
#     for j in range(n):
#         sum_of_cols += magic_square[j][i]
#     sum_of_square.append(sum_of_cols)
# sum_of_square.append(sum_of_main_diag)
# sum_of_square.append(sum_of_side_diag)
# for el in magic_square:
#     square_nums_real.extend(el)
# if square_nums_check == sorted(square_nums_real) and len(set(sum_of_square)) == 1:
#     print('YES')
# else:
#     print('NO')

'''Шахматная доска
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m, 
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную 
матрицу на экран, разделяя элементы пробелами.'''

# m, n = (int(i) for i in input().split())
# table = [[None] * n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if (i + j) % 2 != 0:
#             table[i][j] = '*'
#         else:
#             table[i][j] = '.'
# [print(*el) for el in table]


'''Побочная диагональ
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n и 
заполняет её по следующему правилу:

числа на побочной диагонали равны 11;
числа, стоящие выше этой диагонали, равны 00;
числа, стоящие ниже этой диагонали, равны 22.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.'''

# n = int(input())
# table = [[None] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i + j == n -1:
#             table[i][j] = 1
#         elif i + j >= n:
#             table[i][j] = 2
#         else:
#             table[i][j] = 0
# [print(*el) for el in table]

'''Заполнение
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу 
размером n×m и заполняет её числами от 1 до n⋅m в соответствии с образцом.'''

# n, m = (int(i) for i in input().split())
# matrix = []
# for i in range(n):
#     matrix.append([j + i for j in range(1, m * n + 1, n)])
# [print(*el) for el in matrix]
'''5 5
1  6   11  16  21
2  7   12  17  22
3  8   13  18  23
4  9   14  19  24
5  10  15  20  25'''
# ------------------------------------------------------------------------
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[i][n - i - 1] = 1, 1
# [print(*el) for el in matrix]
'''5
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
'''
# ------------------------------------------------------------------------
# n = int(input())
# matrix = [[1 if n - 1 - j >= i <= j or n - 1 - j <= i >= j else 0 for j in range(n)] for i in range(n)]
# [print(*el) for el in matrix]
'''5
1 1 1 1 1
0 1 1 1 0
0 0 1 0 0
0 1 1 1 0
1 1 1 1 1'''
# ------------------------------------------------------------------------
# n, m = (int(i) for i in input().split())
# row = [i for i in range(1, m + 1)]
# for i in range(n):
#     print(*row)
#     temp = row.pop(0)
#     row.append(temp)
'''5 5
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4'''
# ------------------------------------------------------------------------
'''Заполнение змейкой
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу 
размером n×m заполнив её "змейкой" в соответствии с образцом.'''
# def chunked(symbols, chunk):
#     res = []
#     for i in range(0, len(symbols), chunk):
#         res.append(symbols[:chunk])
#         del symbols[:chunk]
#     return res
#
#
# n, m = (int(i) for i in input().split())
# symbols = [i for i in range(1, n * m + 1)]
# count = 0
# for el in chunked(symbols, m):
#     count += 1
#     if count % 2 != 0:
#         print(*el)
#     else:
#         print(*reversed(el))

'''Заполнение диагоналями 🌶️'''
# n, m = (int(i) for i in input().split())
# matrix = [[0] * m for _ in range(n)]
# temp = 1
# for num in range(n*m):
#     for row in range(n):
#         for col in range(m):
#             if row + col == num:
#                 matrix[row][col] = temp
#                 temp += 1
# [print(*el) for el in matrix]
'''5 5
1  2  4  7  11
3  5  8  12 16
6  9  13 17 20
10 14 18 21 23
15 19 22 24 25
'''

'''Спиральная матрица или улитка    !ПРОВАЛ!   '''
# n, m = (int(i) for i in input().split())
# matrix = [[0] * m for _ in range(n)]
# matrix[0] = [i for i in range(1, m + 1)]
# index = n
# y, x = 0, n - 1
# while index < n * m:
#     for
#         index += 1
#         matrix[y][x] = index
#
#
# [print(*el) for el in matrix]


'''Сложение матриц
Напишите программу для вычисления суммы двух матриц.'''
# n, m = (int(i) for i in input().split())
# result = [[None for i in range(m)]for _ in range(n)]
# matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
# input()
# matrix2 = [[int(i) for i in input().split()] for _ in range(n)]
#
# for i in range(n):
#     for j in range(m):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]
#
# [print(*el) for el in result]

'''Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы.'''
# n1, m1 = (int(i) for i in input().split())
# mat1 = [[int(i) for i in input().split()] for _ in range(n1)]
# input()
# m2, k2 = (int(i) for i in input().split())
# mat2 = [[int(i) for i in input().split()] for _ in range(m2)]
# result = [[0 for _ in range(k2)] for _ in range(n1)]
# for i in range(k2):
#     for j in range(n1):
#         for x in range(m2):
#             result[i][j] += mat1[i][x] * mat2[x][j]
#
# [print(*el) for el in result]

'''Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в mm-ую степень.'''
# from copy import deepcopy
#
# n = int(input())
# m1 = [[int(i) for i in input().split()] for i in range(n)]
# m = int(input())
# m2 = deepcopy(m1)
# result = [[0 for _ in range(n)] for _ in range(n)]
# for _ in range(m - 1):
#     result = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for x in range(n):
#                 result[i][j] += m1[i][x] * m2[x][j]
#     m1 = deepcopy(result)
#
# [print(*el) for el in m1]

'''Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется 
список. Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных 
элементов принадлежат разным подспискам.'''
# nums = [i for i in input().split()]
# result = []
# n = int(input())
# for i in range(n):
#     result.append(nums[i::n])
# print(result)

'''Найти максимум ниже побочной диагонали квадратной матрицы'''
# size = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(size)]
# max_value = 0
# for i in range(size):
#     for j in range(size):
#         if i >= size - 1 - j and matrix[i][j] > max_value:
#             max_value = matrix[i][j]
# print(max_value)

'''Транспонирование матрицы
Напишите программу, которая транспонирует квадратную матрицу.'''
# size = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(size)]
# t_matrix = [[None] * size for _ in range(size)]
# for i in range(size):
#     for j in range(size):
#         t_matrix[i][j] = matrix[j][i]
#
# [print(*el) for el in t_matrix]

'''Снежинка
На вход программе подается нечетное натуральное число nn. Напишите программу, 
которая создает матрицу размером n \times nn×n заполнив её символами . . Затем заполните символами * среднюю строку
 и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран, 
 разделяя элементы пробелами.'''

# size = int(input())
# matrix = [['*' if i == j or i + j + 1 == size or i == size//2 or j == size//2 else '.' for j in range(size)]
#           for i in range(size)]
# [print(*el) for el in matrix]
'''5
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *'''

'''Симметричная матрица
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали.'''

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# transp_matrix = [[None] * n for _ in range(n)]
# matrix.reverse()
# for i in range(n):
#     for j in range(n):
#         transp_matrix[j][i] = matrix[i][j]
# print('YES' if transp_matrix == matrix else 'NO')

''' Латинский квадрат 🌶️
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый 
столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная 
квадратная матрица латинским квадратом.'''
# size = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(size)]
# transp_matrix = [[None] * size for _ in range(size)]
# check_nums = [int(i) for i in range(1, size + 1)]
# latinos = True
# for i in range(size):
#     if sorted(matrix[i]) != check_nums:
#         latinos = False
# for i in range(size):
#     for j in range(size):
#         transp_matrix[j][i] = matrix[i][j]
# for i in range(size):
#     if sorted(transp_matrix[i]) != check_nums:
#         latinos = False
# print('YES' if latinos == True else 'NO')

'''Ходы ферзя
На шахматной доске 8 \times 88×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет
 ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные 
 клетки заполните точками.'''
# table = [['.' for _ in range(8)] for _ in range(8)]
# dict_x = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
# dict_y = {'8': 0, '7': 1, '6': 2, '5': 3, '4': 4, '3': 5, '2': 6, '1': 7}
#
# x1, y1 = [i for i in input()]
# x1, y1 = dict_x[x1], dict_y[y1]
# for x2 in range(8):
#     for y2 in range(8):
#         if x1 == x2 and y2 == y1:
#             table[y2][x2] = 'Q'
#         elif abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
#             table[y2][x2] = '*'
# [print(*el) for el in table]

'''Диагонали параллельные главной
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу 
размером n \times nn×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 00;
на двух диагоналях, прилегающих к главной, число 11;
на следующих двух диагоналях число 22, и т.д.'''
# size = int(input())
# table = [[abs(i - j) for j in range(size)] for i in range(size)]
# [print(*el) for el in table]

'''Дополните приведенный код так, чтобы он вывел список, содержащий средние арифметические значения чисел каждого
вложенного кортежа в заданном кортеже кортежей numbers.'''
# numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
# result = []
# for el in numbers:
#     result.append(sum(list(el))/len(el))
# print(result)

'''Последовательность Трибоначчи
Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Трибоначчи.'''

# def freebonachi(n):
#     a, b, c = 1, 1, 1
#     for i in range(n):
#         yield a
#         a, b, c = b, c, a + b + c
#
#
# result = freebonachi(int(input()))
# [print(re, end=' ') for re in result]
'''Ученики 1010 класса онлайн-школы BEEGEEK получили задание прочесть на летних каникулах три книги:

"Что такое математика?";
"Математическая составляющая";
"100 гениальных идей по математике".
Оказалось, что nn учеников прочитали первую книгу, mm учеников — вторую, kk учеников — третью. Также известно, что xx 
учеников прочли первую или вторую, или обе эти книги, yy учеников — вторую или третью, или обе, zz учеников — первую 
и третью, или хотя бы одну из этих двух книг. Полностью выполнили задание только tt учеников. Всего в 1010 классе 
учится aa учеников. Напишите программу, которая выводит сколько учеников:

прочитали только одну книгу;
прочитали две книги;
не прочитали ни одной из рекомендованных книг.'''
# n, m, k, x, y, z, t, a = int(input()), int(input()), int(input()), int(input()), int(input()), \
#                          int(input()), int(input()), int(input())
# x5 = t
# x2 = m + n - x - t
# x4 = m + k - z - t
# x6 = n + k - y - t
# x1 = n - x2 - x4 - x5
# x3 = m - x2 - x5 - x6
# x7 = k - x4 - x5 - x6
# print(x1+x3+x7)
# print(x2+x4+x6)
# print(a-x1-x2-x3-x4-x5-x6-x7)

'''Уникальные символы 1
Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.'''
# n = int(input())
# words = list({i for i in input().lower()} for _ in range(n)) # set generator turned into nested list
# [print(len(el)) for el in words]


'''Уникальные символы 2
Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.'''
# result = set()
# for _ in range(int(input())):
#     result.update(input().lower())
# print(len(result))

'''Количество слов в тексте
Напишите программу для определения общего количества различных слов в строке текста.'''
# words = set([i.lower().strip('.,;:-?!') for i in input().split()])
# print(len(words))


'''Встречалось ли число раньше?
На вход программе подается строка текста, содержащая числа. Для каждого числа выведите слово 
YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось'''

# num_set = set()
# for num in input().split():
#     if int(num) not in num_set:
#         num_set.add(int(num))
#         print('NO')
#     else:
#         print('YES')

'''Количество совпадающих
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая определяет 
количество чисел, которые есть как в первой строке, так и во второй.'''
# set1, set2 = [{int(i) for i in input().split()} for _ in range(2)]
# print(*sorted(set1 & set2))

'''Числа первой строки
На вход программе подаются две строки текста, содержащие числа. Напишите программу, которая выводит все числа 
в порядке возрастания, которые есть в первой строке, но отсутствуют во второй.'''
# set1, set2 = [{int(i) for i in input().split()} for _ in range(2)]
# print(*sorted(set1 - set2))

'''Общие цифры
На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной 
строке. Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.'''
# n = int(input())
#
# nums = [{str(i) for i in input()} for _ in range(n)]
# for idx in range(1, n):
#     nums[0].intersection_update(nums[idx])
# print(*sorted(nums[0]))

'''Урок математики
Даны по 1010-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит 
множество оценок, имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.'''
# s1, s2, s3 = [{int(i) for i in input().split()} for _ in range(3)]
# union_set = s1 | s2 | s3
# intersection_set = s1 & s2 & s3
# result = union_set.difference(intersection_set)
# print(*sorted(result))

'''Урок математики
Даны по 1010-балльной шкале оценки по математике трех учеников. Напишите программу, которая выводит множество оценок, 
имеющихся у учеников, которые встречаются не более, чем у двух из указанных учеников.'''
# s1, s2, s3 = [{int(i) for i in input().split()} for _ in range(3)]
# result = s3 - (s1 | s2)
# print(*sorted(result, reverse=True))

'''Урок биологии
Даны по 1010-балльной шкале оценки по биологии трех учеников. Напишите программу, которая выводит множество оценок, 
не встречающихся ни у одного из трех учеников.'''
# s1, s2, s3 = [{int(i) for i in input().split()} for _ in range(3)]
# all_nums = set(range(11))
# result = all_nums - (s1 | s2 | s3)
# print(*sorted(result))

'''Используя генератор множеств, дополните приведенный код, так чтобы получить множество, 
содержащее уникальные слова (в нижнем регистре) строки sentence. Результат вывести на одной строке в 
алфавитном порядке, разделяя элементы одним символом пробела.'''

# sentence = '''My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and,
# save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory,
# over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely,
# you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered
# and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges.'''

# result_set = {word.lower().strip(':,.!?();') for word in sentence.split() if len(word.strip(':,.!?();')) < 4}
# print(*sorted(result_set))

'''Используя генератор множеств, дополните приведенный код, так чтобы он выбрал из списка files уникальные имена
файлов c расширением .png, независимо от регистра имен и расширений. Имена файлов вывести вместе с расширением,
все на одной строке, в нижнем регистре, в алфавитном порядке через пробел.'''
#
# files = ['python.png', 'qwerty.py', 'Python.PNg', 'apple.pnG', 'zebra.PNG',  'solution.Py', 'stepik.org',
#          'kotlin.ko', 'github.git', 'ZeBrA.PnG']
# result = {word.lower() for word in files if word.lower().endswith('.png')}
# print(*sorted(result))

'''Домашнее задание
Учитель проверяет домашнее задание в классе и получил следующие ответы: из nn школьников у mm домашнее задание съела 
собака, у kk отключили свет, а pp учеников постигли оба несчастья. Напишите программу, которая определяет сколько 
человек выполнило домашнее задание.'''

# n, m, k, p = [int(input()) for i in range(4)]
# result = n - ((m - p) + (k - p) + p)
# print(result)

'''Восход
На спутнике «Восход» установлен прибор для измерения солнечной активности. Каждую минуту он передаёт в обсерваторию по 
каналу связи положительное целое число — количество энергии солнечного излучения. Для правильного анализа результатов 
нет необходимости держать повторяющиеся данные. Напишите программу, которая выводит максимальное количество показаний 
спутника, при удалении которых результат будет правильно проанализирован.'''
#
# sunrise_data = [i for i in input().split()]
# sunrise_useful_data = set(sunrise_data)
# print(len(sunrise_data) - len(sunrise_useful_data))

'''Города
Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, однако к 
концу игры ввиду своего возраста забывают, какие города уже называли.

Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.'''

# cities = {input() for _ in range(int(input()))}
# next_city = input()
# print('OK' if next_city not in cities else 'REPEAT')

'''Книги на прочтение
Руслан получил в конце учебного года список литературы на лето. Теперь ему надо выяснить, какие книги из этого 
списка у него есть. У Руслана на компьютере в текстовом файле записаны все книги из его домашней библиотеки в 
случайном порядке.

Напишите программу, определяющую для каждой книги из списка на прочтение, есть она у Руслана или нет.'''

# in_library, need_to_read = int(input()), int(input())
# library = set(input() for _ in range(in_library))
# to_read = list(input() for _ in range(need_to_read))
# [print('YES' if to_read[i] in library else 'NO') for i in range(need_to_read)]

'''Странное увлечение
Как известно, математики странные люди. Не составляет исключения и Тимур — автор данного курса. Каждый день 
Тимур решает ровно две сложные математические задачи. Решая первую задачу, он записывает на первом листочке все 
числа, которые в ней встречаются. Далее он делает паузу и берется за вторую задачу. Затем записывает на втором 
листочке все числа, которые в ней встречаются. После этого он берет еще один листок и выписывает на него 
все совпадающие числа из первых двух листочков. Если такие числа есть, день удался, если общих чисел нет, 
Тимур считает день неудачным.

Напишите программу, которая находит общие числа двух листочков или сообщает, что день не удался 😏'''
# nums_of_bad_day = [{int(i) for i in input().split()} for _ in range(2)]
# intersection_of_nums = sorted(nums_of_bad_day[0] & nums_of_bad_day[1], reverse=True)
# print(*intersection_of_nums if len(intersection_of_nums) > 0 else ('BAD DAY', ))

'''Онлайн-школа BEEGEEK 1
При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества 
кандидата, но и его память.

Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать. Причем неважно, 
в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.

Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.'''

# nums_for_test = [{int(i) for i in input().split()} for _ in range(2)]
# print('YES' if nums_for_test[1] == nums_for_test[0] else 'NO')

'''Онлайн-школа BEEGEEK 2
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба эти предмета. 
У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только математику.'''

# m, n = int(input()), int(input())
# math = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
# print(len(math - inf))


'''Онлайн-школа BEEGEEK 3
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих предмета. 
У руководителя школы есть списки изучающих каждый предмет.

Напишите программу, позволяющую руководителю выяснить, сколько учеников изучает только один предмет.'''

# m, n = int(input()), int(input())
# math = {input() for _ in range(m)}
# inf = {input() for _ in range(n)}
# print(len(math ^ inf) if len(math ^ inf) > 0 else 'NO')

'''Онлайн-школа BEEGEEK 4
Руководитель онлайн-школы BEEGEEK и его помощник составили списки учеников их школы.

Напишите программу, которая выведет все фамилии учеников, которые вспомнили руководитель и его помощник.'''

# students = [{i for i in input().split()} for _ in range(2)]
# print(*sorted(students[0] | students[1]))

'''Онлайн-школа BEEGEEK 5 🌶️
Каждый ученик, обучающийся в онлайн-школе BEEGEEK изучает либо математику, либо информатику, либо оба этих 
предмета. У руководителя школы есть списки учеников, изучающих каждый предмет. Случайно списки всех учеников 
перемешались.

Напишите программу, которая позволит руководителю выяснить, сколько учеников изучает только один предмет.'''

# m, n = int(input()), int(input())
# math = set()
# inf = set()
# for i in range(n + m):
#     student = input()
#     if student in math:
#         math.remove(student)
#         inf.add(student)
#     else:
#         math.add(student)
#
# print(len(math) if len(math) > 0 else 'NO')

'''Онлайн-школа BEEGEEK 6 🌶️
Руководителю онлайн-школы BEEGEEK захотелось узнать, кто из его учеников присутствовал на всех уроках с начала 
учебного года. Для каждого урока есть листок со списком присутствовавших учеников.

Напишите программу, определяющую фамилии учеников, которые присутствовали на всех уроках.'''

# lessons = int(input())
# students_on_lesson = [{input() for _ in range(int(input()))} for _ in range(lessons)]
# for idx in range(1, lessons):
#     students_on_lesson[0].intersection_update(students_on_lesson[idx])
# print(*sorted(students_on_lesson[0]), sep='\n')

'''Ваша цель в этой ката состоит в том, чтобы реализовать разностную функцию, которая вычитает один список из 
другого и возвращает результат.

Он должен удалить все значения из списка, которые присутствуют в списке, сохраняя их порядок.ab

array_diff([1,2],[1]) == [2]
Если значение присутствует в , все его вхождения должны быть удалены из другого:b

array_diff([1,2,2,2,3],[2]) == [1,3]'''

# def array_dif(a, b):
#     result = list()
#     for el in a:
#         if el not in b:
#             result.append(el)
#     return result


# print(array_dif([1,2,2,2,3],[2]))

'''In this kata you have to write a simple Morse code decoder. While the Morse code is now mostly superseded by voice 
and digital data communication channels, it still has its use in some applications around the world.
The Morse code encodes every character as a sequence of "dots" and "dashes". For example, the letter A is coded as ·−, 
letter Q is coded as −−·−, and digit 1 is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital 
letters are used. When the message is written in Morse code, a single space is used to separate the character codes 
and 3 spaces are used to separate words. For example, the message HEY JUDE in Morse code 
is ···· · −·−−   ·−−− ··− −·· ·.

NOTE: Extra spaces before or after the code have no meaning and should be ignored.'''

'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), 
чей номер оканчивается на 88.'''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# result = list()
# for row in users:
#     if row['phone'].endswith('8'):
#         result.append(row['name'])
# print(*sorted(result))


'''Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых 
нет информации об электронной почте. '''
# users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
#          {'name': 'Helga', 'phone': '555-1618'},
#          {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
#          {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
#          {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
#          {'name': 'John', 'phone': '233-421-32', 'email': ''},
#          {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
#          {'name': 'Alina', 'phone': '+7948-799-2434'},
#          {'name': 'Robert', 'phone': '420-2011', 'email': ''},
#          {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
#          {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
#          {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
#          {'name': 'Roman', 'phone': '+7459-145-8059'},
#          {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
#          {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
#          {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]
# result = list()
# for el in users:
#     if 'email' not in el.keys() or len(el['email']) < 1:
#         result.append(el['name'])
# print(*sorted(result))

# '''Строковое представление
# Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова'''
# nums = {
#     0: "zero",
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }
# print(*[nums[int(i)] for i in input()])


'''Набор сообщений
На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. Поскольку 
с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. При однократном 
нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2, 3, 42,3,4 или 55 раз 
генерирует второй, третий, четвертый или пятый символ клавиши.'''

# decrypt = {
#     "1": [".", ",", "?", "!", ":"],
#     "2": ["A", "B", "C"],
#     "3": ["D", "E", "F"],
#     "4": ["G", "H", "I"],
#     "5": ["J", "K", "L"],
#     "6": ["M", "N", "O"],
#     "7": ["P", "Q", "R", "S"],
#     "8": ["T", "U", "V"],
#     "9": ["W", "X", "Y", "Z"],
#     "0": [" "]
# }
#
# sentence = input()
# result = list()
# for letter in sentence.upper():
#     for key, value in decrypt.items():
#         if letter in value:
#
#             result.append(key * (value.index(letter) + 1))
# print(*result, sep='')

'''Код Морзе
Код Морзе для представления цифр и букв использует тире и точки.

Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе.'''

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# decrypt = {key: value for key, value in zip(letters, morse)}
#
# encrypt = ''.join([i.upper() for i in input() if i not in '.,;:-?! +=-'])
# for letter in encrypt:
#     print(decrypt[letter], end=' ')

'''Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам, 
складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий 
словарь необходимо присвоить переменной result.'''
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# check = {'a': 400, 'b': 400, 'c': 312, 'd': 445, 'e': 98, 'f': 90, 'm': 230, 'p': 123, 'q': 34, 't': 853, 'w': 111,
# 'z': 999}
#
# result = {}
# keys = dict1.keys() | dict2.keys()
# for key in keys:
#     result[key] = dict2.get(key, 0) + dict1.get(key, 0)
#
# print(result, check, sep='\n')
'''Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько, 
должно быть выведено то, что меньше в лексикографическом порядке.'''

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange
# ' \ 'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry
# apricot ' \ 'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon
# ' \ 'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple
# ' \ 'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
# 'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
# 'barley ' temp = {word: s.count(word) for word in set(s.split())} result = [] max_value = max(temp.values()) for
# key, value in temp.items(): if temp[key] == max_value: result.append(key) print(min(result))
'''Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж в
ида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут 
перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список 
кличек собак (сохранив исходный порядок следования).'''

# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for el in pets:
#     result.setdefault(el[1:], []).append(el[0])

'''Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, 
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.'''

# results = list()
#
# words = [word.lower().strip(':,.!?();') for word in input().split()]
# dict_words = {el: words.count(el) for el in set(words)}
# min_value = min(dict_words.values())
# for key, value in dict_words.items():
#     if dict_words[key] == min_value:
#         results.append(key)
#
# print(min(results))
'''Исправление дубликатов 🌶️
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так, 
чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам 
постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался.'''

# words = [i for i in input().split()]
# dict_of_words = {}
# for word in words:
#     dict_of_words[word] = dict_of_words.get(word, -1) + 1
#     if dict_of_words[word] > 0:
#         print(f'{word}_{dict_of_words[word]}', end=' ')
#     else:
#         print(word, end=' ')

'''Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык. 
Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу 
создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из 
этого словаря.'''

# words_dict = {}
# for _ in range(int(input())):
#     row = input().split(': ')
#     words_dict[row[0].lower()] = row[1]
# for _ in range(int(input())):
#     result = words_dict.get(input().lower(), 'Не найдено')
#     print(result)

'''Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово 
(или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами.'''
# first, second = input(), input()
# f_dict = {i: first.count(i) for i in first}
# s_dict = {i: second.count(i) for i in second}
# print('YES' if f_dict == s_dict else 'NO')

'''Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами 
или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.'''

# first, second = input().lower(), input().lower()
# f_dict = {i: first.count(i) for i in first if i.isalpha()}
# s_dict = {i: second.count(i) for i in second if i.isalpha()}
# print('YES' if f_dict == s_dict else 'NO')

'''Словарь синонимов
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу, 
которая для одного данного слова определяет его синоним.'''

# words_dict = {}
# for _ in range(int(input())):
#     row = input().split()
#     words_dict[row[1]] = row[0]
#     words_dict[row[0]] = row[1]
# print(words_dict[input()])


# d = {i[0]: i[1] for i in [input().split() for _ in range(int(input()))]}
# word = input()
# for key, value in d.items():
#     if value == word:
#         print(key)
#     elif key == word:
#         print(value)


'''Страны и города
На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу, 
которая для каждого города выводит, в какой стране он находится.'''
# cities = dict()
# for _ in range(int(input())):
#     key, *values = input().split()
#     cities.update(cities.fromkeys(values, key))
# [print(cities[input()]) for _ in range(int(input()))]

'''Телефонная книга
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру 
находить все номера определённого друга.
'''
# phone_numbers = dict()
# for _ in range(int(input())):
#     number, name = input().lower().split()
#     phone_numbers.setdefault(name, []).append(number)
# for _ in range(int(input())):
#     print(*phone_numbers.get(input().lower(), ['абонент не найден']))

'''Секретное слово
Напишите программу для расшифровки секретного слова методом частотного анализа.'''

# encripted = input()
# dict_of_transcripted = dict()
# for _ in range(int(input())):
#     letter, count = input().split(': ')
#     dict_of_transcripted[letter] = count
# for letter in encripted:
#     for key, value in dict_of_transcripted.items():
#         if str(encripted.count(letter)) == dict_of_transcripted[key]:
#             print(key, end='')

'''Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка 
numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 11.
Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}'''

# numbers = [1, 6, 18]
# result = {i: [x for x in range(1, i + 1) if i % x == 0] for i in sorted(numbers)}
# print(result)

'''Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет 
строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}'''

# words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']
#
# result = {i: [ord(symbol) for symbol in i] for i in words}
# pprint(result)

# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
#
# result = []
# for key, values in emails.items():
#     result.extend(f'{value}@{key}' for value in values)
# print(*sorted(result), sep='\n')
#
'''Порядковый номер
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв, 
слова разделены одним пробелом или несколькими.

Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с 
учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д.'''
# sentence = input().split()
# sentence_count = dict()
# for word in sentence:
#     sentence_count[word] = sentence_count.get(word, 0) + 1
#     print(sentence_count[word], end=' ')

'''Scrabble game
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв. 
Чем реже буква встречается, тем больше она ценится:'''
# d = {
#     1: "AEILNORSTU",
#     2: "DG",
#     3: "BCMP",
#     4: "FHVWY",
#     5: "K",
#     8: "JX",
#     10: "QZ"
# }
# word = input()
# point = 0
# for letter in word:
#     for k, v in d.items():
#         if letter in d[k]:
#             point += k
# print(point)

'''Строка запроса
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного 
знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green 
Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса, 
сформированную из этих параметров.'''

# def build_query_string(params):
#     temp = []
#     for k, v in params.items():
#         temp.append(f'{k}={v}')
#     result = ['&'.join(sorted(temp))]
#     return str(*result)
#
#
# print(build_query_string({'name': 'timur', 'age': 28}))
# print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))

'''Слияние словарей 🌶️
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать 
словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей 
переданного списка.'''

# def merge(values):      # values - это список словарей
#     result = dict()
#     for value in values:
#         for k, v in value.items():
#             if k in result:
#                 result[k].add(v)
#             else:
#                 result[k] = {v}
#     return result
#
#
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))

'''Опасный вирус 😈
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль
прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).

Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна будет 
возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима.'''
# file_operations = dict()
# s = {'write': 'W', 'read': 'R','execute': 'X'}
# for _ in range(int(input())):
#     file, *operations = input().split()
#     for operation in operations:
#         file_operations.setdefault(operation, []).append(file)
# print(file_operations)
# for _ in range(int(input())):
#     command, file = input().split()
#     print('OK' if s[command] in file_operations and file in file_operations[s[command]] else 'Access denied')

'''Покупки в интернет-магазине 🌶️
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем 
интернет-магазина.'''
# result = dict()
# for _ in range(int(input())):
#     name, item, count = input().split()
#     result[name] = result.get(name, {})
#     result[name][item] = result.get(name, {}).get(item, 0) + int(count)
# for el in sorted(result):
#     print(f'{el}:', sep='\n')
#     for sub_el in sorted(result[el]):
#         print(f'{sub_el} {result[el][sub_el]}')
'''Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество
 попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке).'''
# import random
#
# sides = {1: 'Орел', 2: 'Решка'}
#
# for _ in range(int(input())):
#     side = random.randrange(1, 3)
#     print(sides[side])

'''Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 66 гранями. Программа 
принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика 
(каждое на отдельной строке).'''
# import random
# [print(random.randint(1, 6)) for _ in range(int(input()))]

'''Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину 
пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z 
(в нижнем и верхнем регистре).'''
# import random


# length = int(input())
# for _ in range(length):
#     value = random.randint(65, 90)
#     print(chr(value) if random.randrange(0, 2) == 0 else chr(value).lower(), end='')

'''Лотерейный билет содержит 77 чисел из диапазона от 11 до 4949 (включительно).

Напишите программу, которая с помощью модуля random генерирует 77 различных случайных чисел для лотерейного билета. 
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела.'''
# result_lot = set(random.randrange(1, 50) for _ in range(7))
# print(*sorted(result_lot))

'''IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес.'''
# import random
#
#
# def generate_ip():
#     result = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
#     return result
#
#
# print(generate_ip())

'''Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква 
английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный 
почтовый индекс Латверии.'''
# import random, string
#
#
# def generate_index():
#     letters, nums = string.ascii_uppercase, string.digits
#     return f'{random.choice(letters)}{random.choice(letters)}{random.choice(nums)}_' \
#            f'{random.choice(nums)}{random.choice(letters)}{random.choice(letters)}'
#
# print(generate_index())

'''Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы 
(двумерного списка).'''
# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for el in matrix:
#     random.shuffle(el)
# print(matrix)

'''Напишите программу, которая с помощью модуля random генерирует 100100 случайных номеров лотерейных билетов и выводит 
их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 77 цифр;
все 100100 лотерейных билетов должны быть различными.'''
# import random
#
# for _ in range(100):
#     print(random.randint(1000000, 9999999))

'''Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму.'''

# import random
#
#
# def random_shuffle(text):
#     list_of_text = list(text)
#     random.shuffle(list_of_text)
#     return ''.join(i for i in list_of_text)
#
#
# print(random_shuffle(input()))

'''Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1
 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго.'''
# import random
#
#
# def bingo_map():
#     nums = random.sample(range(1, 76), 25)
#     nums[25//2] = 0
#     return nums
#
#
# print(bingo_map())
# step = 0
# result = bingo_map()
# for _ in range(5):
#     print(*result[step:step + 5])
#     step += 5

'''Тайный друг 🌶️
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним 
решать задачи по программированию.'''
# import random
#
# n = int(input())
# students = [input() for _ in range(n)]
# helper_students = students.copy()
# k = False
# while not k:
#     for i in range(len(students)):
#         if students[i] == helper_students[i]:
#             k = False
#             random.shuffle(helper_students)
#         else:
#             k = True
# for i in range(n):
#     print(f'{students[i]} - {helper_students[i]}')

'''Генератор паролей 1
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и 
прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).'''

# import string, random
#
#
# count, length = int(input()), int(input())
#
#
# def generate_passwords(count, length):
#     allowed_symbols = list((set(string.digits) | set(string.ascii_letters)) - set('lI1oO0'))
#     result = list()
#     for _ in range(count):
#         result.append(''.join(random.sample(allowed_symbols, length)))
#     return result
#
#
# [print(el) for el in generate_passwords(count, length)]

'''Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и 
прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной 
букве в верхнем и нижнем регистре.'''
# import random, string
#
#
# def generate_password(length):
#     en_up = [el for el in string.ascii_uppercase if el not in 'OI']
#     en_low = [el for el in string.ascii_lowercase if el not in 'ol']
#     digits = [el for el in string.digits if el not in '01']
#     all_symbols = en_up + en_low + digits
#     result = random.choice(en_up) + random.choice(en_low) + random.choice(digits)
#     for _ in range(length - 3):
#         result += random.choice(all_symbols)
#
#     return ''.join(random.sample(result, length))
#
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
#
# n, m = int(input()), int(input())
# [print(el) for el in generate_passwords(n, m)]


'''Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы 
неравенств:'''

# import random
#
# n = 10 ** 6  # количество испытаний
# k = 0
# s0 = 16
# for _ in range(n):
#     x = random.uniform(-2, 2)
#     y = random.uniform(-2, 2)
#     if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
#         k += 1
# print((k / n) * s0)

'''Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа \piπ.'''
#
# import random
#
# n = 10 ** 6  # количество испытаний
# k = 0
# s0 = 4
# for _ in range(n):
#     x = random.uniform(-1, 1)
#     y = random.uniform(-1, 1)
#     if x ** 2 + y ** 2 <= 1:
#         k += 1
# print((k / n) * s0)


'''Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы 
он вывел сумму наибольшего и наименьшего Decimal числа.'''
# from _decimal import Decimal as D
# s = '0.77 4.03 9.06 3.80 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 6.67 ' \
#     '1.46 5.26 4.83 7.23 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 5.78 5.37 ' \
#     '0.03 9.60 8.86 2.73 5.83 6.50 '
# list_of_dec = [D(i) for i in s.split()]
# print(max(list_of_dec) + min(list_of_dec))

'''Decimal числа, разделенные символом пробела, хранятся в строковой переменной s. Дополните приведенный код, чтобы он 
вывел на первой строке сумму всех чисел, а на второй строке 55 самых больших чисел в порядке убывания, разделенных 
символом пробела.'''
#
# from decimal import Decimal as D
#
#
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 ' \
#     '7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 ' \
#     '3.86 5.56 1.43 8.36 6.29 5.13 '
# list_of_dec = [D(i) for i in s.split()]
# print(sum(list_of_dec))
# print(*sorted(list_of_dec, reverse=True)[:5])

'''Дополните приведенный код, чтобы он вывел сумму наибольшей и наименьшей цифры Decimal числа.'''

# from decimal import Decimal
#
# number = Decimal(input())
# tuple_of_digits = number.as_tuple().digits
# print(min(tuple_of_digits) + max(tuple_of_digits) if abs(number) > 1 else max(tuple_of_digits))

'''Математическое выражение
На вход программе подается Decimal число dd. Напишите программу, которая вычисляет значение выражения:'''
# from decimal import *
#
#
# number = Decimal(input())
# result = number.exp() + number.ln() + number.log10() + number.sqrt()
# print(result)

'''Десятичные числа хранятся в списке numbers в виде строк. Дополните приведенный код, чтобы он для каждого десятичного 
числа вывел его представление в виде обыкновенной дроби в формате:

десятичное число = обыкновенная дробь'''
# from fractions import Fraction as F
#
#
# numbers = ['6.34', '4.08', '3.04', '7.49', '4.45', '5.39', '7.82', '2.76', '0.71', '1.97', '2.54', '3.67', '0.14',
#            '4.29', '1.84', '4.07', '7.26', '9.37', '8.11', '4.30', '7.16', '2.46', '1.27', '0.29', '5.12', '4.02',
#            '6.95', '1.62', '2.26', '0.45', '6.91', '7.39', '0.52', '1.88', '8.38', '0.75', '0.32', '4.81', '3.31',
#            '4.63', '7.84', '2.25', '1.10', '3.35', '2.05', '7.87', '2.40', '1.20', '2.58', '2.46']
# for el in numbers:
#     print(f'{el} = {F(el)}')

'''Десятичные числа разделенные символом пробела хранятся в строковой переменной s. Дополните приведенный код, чтобы 
он вывел сумму наибольшего и наименьшего числа в виде обыкновенной дроби.'''
#
# from fractions import Fraction
#
# s = '0.78 4.3 9.6 3.88 7.08 5.88 0.23 4.65 2.79 0.90 4.23 2.15 3.24 8.57 0.10 8.57 1.49 5.64 3.63 8.36 1.56 ' \
#     '6.67 1.46 5.26 4.83 7.13 1.22 1.02 7.82 9.97 5.40 9.79 9.82 2.78 2.96 0.07 1.72 7.24 7.84 9.23 1.71 6.24 ' \
#     '5.78 5.37 0.03 9.60 8.86 2.73 5.83 6.50 0.123 0.00021'
#
# list_of_nums = [Fraction(el) for el in s.split()]
# print(max(list_of_nums) + min(list_of_nums))

'''Сократите дробь
Даны два натуральных числа mm и nn. Напишите программу, которая сокращает дробь и выводит ее.'''
# from fractions import Fraction
#
# print(Fraction(int(input()), int(input())))

'''Операции над дробями
Даны две дроби в формате a/b. Напишите программу, которая вычисляет и выводит их сумму, разность, произведение и 
частное.

Sample Input 1:

2/3
3/7
Sample Output 1:

2/3 + 3/7 = 23/21
2/3 - 3/7 = 5/21
2/3 * 3/7 = 2/7
2/3 / 3/7 = 14/9'''
# from fractions import Fraction as F
#
# num1, num2 = input(), input()
# for point in '+-*/':
#     print(f'{num1} {point} {num2} = {eval(f"F(num1) {point} F(num2)")}')
'''Сумма дробей 1
На вход программе подается натуральное число nn. Напишите программу, которая вычисляет и выводит рациональное 
число, равное значению выражения '''
# from fractions import Fraction as F
# from math import factorial
#
# n = int(input())
# result = sum([F(1, factorial(i)) for i in range(1, n + 1)])
# print(result)

'''Юный математик 🌶️
Дима учится в седьмом классе и сейчас они проходят обыкновенные дроби с натуральными числителем и знаменателем. Вчера 
на уроке математики Дима узнал, что дробь называется правильной, если ее числитель меньше знаменателя, и несократимой, 
если нет равной ей дроби с меньшими натуральными числителем и знаменателем.

Дима очень любит математику, поэтому дома он долго экспериментировал, придумывая и решая разные задачки с правильными 
несократимыми дробями. Одну из этих задач Дима предлагает решить вам с помощью компьютера.

На вход программе подается натуральное число nn. Напишите программу, которая находит наибольшую правильную несократимую 
дробь с суммой числителя и знаменателя равной nn.'''
# from fractions import Fraction
#
# n = int(input())
# lst = []
#
# for i in range(1, n-1):
#     for j in range(i+1, n):
#         k = Fraction(i, j)
#         if k.numerator + k.denominator == n:
#             lst.append(Fraction(i, j))
#
# print(max(lst))
'''Упорядоченные дроби
На вход программе подается натуральное число nn. Напишите программу, которая выводит в порядке возрастания все 
несократимые дроби, заключённые между 00 и 11, знаменатель которых не превосходит nn.'''
# from math import gcd
# from fractions import Fraction as F
# result = set()
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if gcd(i, j) == 1 and i < j:
#             result.add(F(i, j))
# print(*sorted(list(result)), sep='\n')


# z1, z2 = complex(input()), complex(input())
# for point in '+-*':
#     print(f'{z1} {point} {z2} = {eval(f"(z1) {point} (z2)")}')


'''Комплексные числа хранятся в списке numbers. Дополните приведенный код так, чтобы он вывел комплексное число с 
наибольшим модулем и сам модуль числа на отдельных строках.'''
# numbers = [3 + 4j, 3 + 1j, -7 + 3j, 4 + 8j, -8 + 10j, -3 + 2j, 3 - 2j, -9 + 9j, -1 - 1j, -1 - 10j, -20 + 15j, -21 + 1j,
#            1j, -3 + 8j, 4 - 6j, 8 + 2j, 2 + 3j]

# abs_of_numbers = [abs(num) for num in numbers]
# i = abs_of_numbers.index(max(abs_of_numbers))
# print(numbers[i], max(abs_of_numbers), sep='\n')


# n, z1, z2 = int(input()), complex(input()), complex(input())
# result = z1 ** n + z2 ** n + z1.conjugate() ** n + z2.conjugate() ** (n + 1)
# print(result)

'''Рисую гадость черепахой, мучаю животное'''
import turtle

#
#
# def square(len):
#     for _ in range(4):
#         turtle.forward(len)
#         turtle.left(90)
#
#
# for _ in range(8):
#     turtle.left(45)
#     square(200)

# def hexagon():
#     for _ in range(6):
#         turtle.forward(100)
#         turtle.left(60)
#
#
# for _ in range(12):
#     turtle.left(30)
#     hexagon()

'''Напишите функцию matrix(), которая создает, заполняет и возвращает матрицу заданного размера. При этом 
(в зависимости от переданных аргументов) она должна вести себя так:

matrix() — возвращает матрицу 1 \times 11× 1, в которой единственное число равно нулю;
matrix(n) — возвращает матрицу n \times nn× n, заполненную нулями;
matrix(n, m) — возвращает матрицу из nn строк и mm столбцов, заполненную нулями;
matrix(n, m, value) — возвращает матрицу из nn строк и mm столбцов, в которой каждый элемент равен числу value.
При создании функции пользуйтесь аргументами по умолчанию.

Примечание 1. Приведенный ниже код:

print(matrix())                   # матрица 1 × 1 из 0
print(matrix(3))                  # матрица 3 × 3 из 0
print(matrix(2, 5))               # матрица 2 × 5 из 0
print(matrix(3, 4, 9))            # матрица 3 × 4 из 9
должен выводить:

[[0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]]'''

# def matrix(row=1, col=None, el=0):
#     if col is None:
#         col = row
#     result = [[el for _ in range(col)] for _ in range(row)]
#     return result

'''Напишите функцию mean(), которая принимает произвольное количество аргументов и возвращает среднее арифметическое 
переданных в нее числовых (int или float) аргументов.'''
# def mean(*args):
#     result = [i for i in args if type(i) is int or type(i) is float]
#     return sum(result)/len(result) if len(result) > 0 else 0.0
#
#
# print(mean())
# print(mean(7))
# print(mean(1.5, True, ['stepik'], 'beegeek', 2.5, (1, 2)))
# print(mean(True, ['stepik'], 'beegeek', (1, 2)))
# print(mean(-1, 2, 3, 10, ('5')))
# print(mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

'''Напишите функцию greet(), которая принимает произвольное количество аргументов строк имен (как минимум одно) и 
возвращает приветствие в соответствии с образцом.'''


# def greet(name, *args):
#     source = name.split() + list(args)
#     result = f'Hello, {" and ".join(i for i in source)}'
#     return result + '!'
#
# print(greet('Timur'))
# print(greet('Timur', 'Roman'))
# print(greet('Timur', 'Roman', 'Ruslan'))

'''Напишите функцию print_products(), которая принимает произвольное количество аргументов и выводит список продуктов 
(любая непустая строка) по образцу: <номер продукта>) <название продукта> (нумерация продуктов начинается с единицы). 
Если среди переданных аргументов нет ни одного продукта, необходимо вывести текст Нет продуктов.'''
# def print_products(*args):
#     list_of_products = [el for el in args if type(el) is str and el != '']
#     dict_of_products = {i: list_of_products[i - 1] for i in range(1, len(list_of_products) + 1)}
#     if dict_of_products:
#         for key, value in dict_of_products.items():
#             print(f'{key}) {value}')
#     else:
#         print('Нет продуктов')
#
#
# print_products('Бананы', [1, 2], ('Stepik',), 'Яблоки', '', 'Макароны', 5, True)

'''Напишите функцию info_kwargs(), которая принимает произвольное количество именованных аргументов и печатает 
именованные аргументы в соответствии с образцом: <имя аргумента>: <значение аргумента>, при этом имена аргументов 
следуют в алфавитном порядке (по возрастанию).'''


# def info_kwargs(**kwargs):
#     for el, value in sorted(kwargs.items()):
#         print(f'{el}: {value}')
#
#
# info_kwargs(first_name='Timur', last_name='Guev', age=28, job='teacher')

'''Дан список numbers, содержащий кортежи чисел. Напишите программу, которая с помощью встроенных функций min() и max() 
выводит те кортежи (каждый на отдельной строке), которые имеют минимальное и максимальное среднее арифметическое 
значение элементов.'''
numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34),
           (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4),
           (90, 1, -45, -21)]




