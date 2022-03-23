"""Напишите программу, которая с помощью модуля random моделирует броски монеты. Программа принимает на вход количество
 попыток и выводит результаты бросков: Орел или Решка (каждое на отдельной строке)."""
# import random
#
# sides = {1: 'Орел', 2: 'Решка'}
#
# for _ in range(int(input())):
#     side = random.randrange(1, 3)
#     print(sides[side])

"""Напишите программу, которая с помощью модуля random моделирует броски игрального кубика c 66 гранями. Программа
принимает на вход количество попыток и выводит результаты бросков — выпавшее число, которое написано на грани кубика
(каждое на отдельной строке)."""
# import random
# [print(random.randint(1, 6)) for _ in range(int(input()))]

"""Напишите программу, которая с помощью модуля random генерирует случайный пароль. Программа принимает на вход длину
пароля и выводит случайный пароль, содержащий только символы английского алфавита a..z, A..Z
(в нижнем и верхнем регистре)."""
# import random


# length = int(input())
# for _ in range(length):
#     value = random.randint(65, 90)
#     print(chr(value) if random.randrange(0, 2) == 0 else chr(value).lower(), end='')

"""Лотерейный билет содержит 77 чисел из диапазона от 11 до 4949 (включительно).

Напишите программу, которая с помощью модуля random генерирует 77 различных случайных чисел для лотерейного билета.
Программа должна вывести числа в порядке возрастания на одной строке через один символ пробела."""
# result_lot = set(random.randrange(1, 50) for _ in range(7))
# print(*sorted(result_lot))

"""IP адрес состоит из четырех чисел из диапазона от 00 до 255255 (включительно) разделенных точкой.

Напишите функцию generate_ip(), которая с помощью модуля random  генерирует и возвращает случайный корректный IP адрес."""
# import random
#
#
# def generate_ip():
#     result = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
#     return result
#
#
# print(generate_ip())

"""Почтовый индекс в Латверии имеет вид: LetterLetterNumber_NumberLetterLetter, где Letter – заглавная буква
английского алфавита, Number – число от 00 до 9999 (включительно).

Напишите функцию generate_index(), которая с помощью модуля random генерирует и возвращает случайный корректный
почтовый индекс Латверии."""
# import random, string
#
#
# def generate_index():
#     letters, nums = string.ascii_uppercase, string.digits
#     return f'{random.choice(letters)}{random.choice(letters)}{random.choice(nums)}_' \
#            f'{random.choice(nums)}{random.choice(letters)}{random.choice(letters)}'
#
# print(generate_index())

"""Напишите программу, которая с помощью модуля random перемешивает случайным образом содержимое матрицы
(двумерного списка)."""
# import random
# matrix = [[1, 2, 3, 4],
#           [5, 6, 7, 8],
#           [9, 10, 11, 12],
#           [13, 14, 15, 16]]
# for el in matrix:
#     random.shuffle(el)
# print(matrix)

"""Напишите программу, которая с помощью модуля random генерирует 100100 случайных номеров лотерейных билетов и выводит
их каждый на отдельной строке. Обратите внимание, вы должны придерживаться следующих условий:

номер не может начинаться с нулей;
номер лотерейного билета должен состоять из 77 цифр;
все 100100 лотерейных билетов должны быть различными."""
# import random
#
# for _ in range(100):
#     print(random.randint(1000000, 9999999))

"""Анаграмма – это слово образованное путём перестановки букв, составляющих другое слово.

Например, слова пила и липа или пост и стоп – анаграммы.

Напишите программу, которая считывает одно слово и выводит с помощью модуля random его случайную анаграмму."""

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

"""Для игры в бинго требуется карточка размером 5×5, содержащая различные (уникальные) целые числа от 1
 до 75 (включительно), при этом центральная клетка является пустой (она заполняется числом 0).

Напишите программу, которая с помощью модуля random генерирует и выводит случайную карточку для игры в бинго."""
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

"""Тайный друг 🌶️
Напишите программу, которая случайным образом назначает каждому ученику его тайного друга, который будет вместе с ним
решать задачи по программированию."""
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

"""Генератор паролей 1
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и
прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра)."""

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

"""Генератор паролей 2 🌶️
Напишите программу, которая с помощью модуля random генерирует nn паролей длиной mm символов, состоящих из строчных и
прописных английских букв и цифр, кроме тех, которые легко перепутать между собой:

«l» (L маленькое);
«I» (i большое);
«1» (цифра);
«o» и «O» (большая и маленькая буквы);
«0» (цифра).
Дополнительное условие: в каждом пароле обязательно должна присутствовать хотя бы одна цифра и как минимум по одной
букве в верхнем и нижнем регистре."""
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


"""Напишите программу, которая при помощи метода Монте-Карло вычисляет площадь фигуры, задаваемой с помощью системы
неравенств:"""

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

"""Напишите программу, которая при помощи метода Монте-Карло определяет приближённое значение числа \piπ."""
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
