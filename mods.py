"""Напишите программу, которая подключает модуль math и, используя значение числа \piπ из этого модуля, находит для
переданного ей на стандартный ввод радиуса круга периметр этого круга и выводит его на стандартный вывод."""

# import math
# r = float(input())
# print(2 * math.pi * r)
"""Напишите программу, которая запускается из консоли и печатает значения всех переданных аргументов на экран
 (имя скрипта выводить не нужно). Не изменяйте порядок аргументов при выводе.

Для доступа к аргументам командной строки программы подключите модуль sys и используйте переменную argv из этого модуля.

Пример работы программы:

> python3 my_solution.py arg1 arg2
arg1 arg2"""
import sys

# print(*sys.argv[1:])

"""Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать
число строк в нём.

Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать
пробельные символы по краям).

После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не
 принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.

В поле ответа введите одно число или отправьте файл, содержащий одно число."""

import requests

# with open('D:\Downloads\dataset_3378_2 (1).txt') as file:
#     url = file.read().strip()
# r = requests.get(url)
# print(r.text)
# summary = 0
# for line in r.text.splitlines():
#     summary += 1
# print(summary)

"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""
#
# download_link = 'https://stepic.org/media/attachments/course67/3.6.3/'
# filename = '699991.txt'
#
# while filename:
#     print(filename)
#     r = requests.get(download_link + filename)
#     if r.text.startswith('We'):
#         filename = None
#     else:
#         filename = r.text
# print(r.text)

"""За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой

Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков"""
# n = int(input())
# pre_res = dict()
# res = dict()
# list = []
# result = []
# for i in range(n):
#     list.append(input().split(';'))
#     pre_res.update({list[i][0]: '', list[i][2]: ''})
#     for key in pre_res:
#         if pre_res[key] == list.
#         pre_res[key] += list[i][1]
#     # pre_res
#     # for part in range(4):
#     #     res[list[i][part]] = list[i][part + 1]
# print(list)
# print(pre_res)

# import itertools
# n = int(input())
# x_list = [input().split(';') for x in range(n)]
# vs = [(x[0], x[2]) for x in x_list]
# clubs = set(itertools.chain.from_iterable(vs))
# res = {club:[0, 0, 0, 0, 0] for club in clubs}
# for kom1, gol1, kom2, gol2 in x_list:
#     res[kom1][0] += 1
#     res[kom2][0] += 1
#     if int(gol1) > int(gol2):
#         res[kom1][1] += 1
#         res[kom1][4] += 3
#         res[kom2][3] += 1
#     elif int(gol1) < int(gol2):
#         res[kom2][1] += 1
#         res[kom2][4] += 3
#         res[kom1][3] += 1
#     elif int(gol1) == int(gol2):
#         res[kom1][2] += 1
#         res[kom1][4] += 1
#         res[kom2][2] += 1
#         res[kom2][4] += 1
# for club in clubs:
#     print('{}:{}'.format(club, ' '.join(map(str, res[club]))))

"""Напишите программу, которая умеет шифровать и расшифровывать шифр подстановки. Программа принимает на вход две
строки одинаковой длины, на первой строке записаны символы исходного алфавита, на второй строке — символы конечного
алфавита, после чего идёт строка, которую нужно зашифровать переданным ключом, и ещё одна строка, которую нужно
расшифровать.

Пусть, например, на вход программе передано:
abcd
*d%#
abacabadaba
#*%*d*%

Это значит, что символ a исходного сообщения заменяется на символ * в шифре, b заменяется на d, c — на % и d — на #.
Нужно зашифровать строку abacabadaba и расшифровать строку #*%*d*% с помощью этого шифра. Получаем следующие строки,
 которые и передаём на вывод программы:
*d*%*d*#*d*
dacabac"""

# real = input()
# post_real = input()
# result_real = input()
# result_post_real = input()
# output_1 = ''
# output_2 = ''
# dictionary = {key: value for key, value in zip(real, post_real)}
# inverted_dictionary = dict(map(reversed, dictionary.items()))
#
# for symbol in result_real:
#     output_1 += dictionary[symbol]
# for symbol in result_post_real:
#     output_2 += inverted_dictionary[symbol]
# print(output_1, output_2, sep='\n')


"""Работа с файлами"""
# from collections import defaultdict
# d = dict()
# with open('D:\std\some_stepik_tests\dataset_3380_5 (1).txt') as file:
#     for line in file:
#         var = line.strip().split('\t')
#
#         d[var[0]] = var[2]
# print(sorted(d, key=d.__getitem__()))

# with open('/dataset_3380_5 (2).txt', 'r') as f, open('outxt', 'w') as g:
#     s = []
#     v = 0
#     for line in f:
#         s += line.split()
#         v += 1
#
#     t = [0] * 11
#     t2 = [0] * 11
#     k = 0
#     for i in range(2, v * 3, 3):
#         k = int(s[i - 2])
#         if 1 <= k <= 11:
#             t[k - 1] += int(s[i])
#             t2[k - 1] += 1
#
#     for i in range(0, 11):
#         value = [i + 1, ' ', t[i] / t2[i], '\n']
#         for x in value:
#             g.write(str(x))

"""Задача Иосифа Флавия 🌶️🌶️
nn человек, пронумерованных числами от 11 до nn, стоят в кругу. Они начинают считаться,
каждый kk-й по счету человек выбывает из круга, после чего счет продолжается со следующего за ним человека.
Напишите программу, определяющую номер человека, который останется в кругу последним."""

# n, k = int(input()), int(input())
# result = 0
# for i in range(1, n + 1):
#     result = (result + k) % i
# print(result + 1)

"""Определение по координатам в какой четверти находится объкт"""
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


"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число
дней, равное days."""

# from datetime import date, timedelta
#
#
# def next_date(year, month, day, new_day):
#     date_now = date(year, month, day)
#     delta = timedelta(days=new_day)
#     date_now += delta
#     return date_now.year, date_now.month, date_now.day
#
#
# year, month, day = map(int, input().split())
# nd = int(input())
# print(*next_date(year, month, day, nd))
"""Алиса владеет интересной информацией, которую хочет заполучить Боб.
Алиса умна, поэтому она хранит свою информацию в зашифрованном файле.
У Алисы плохая память, поэтому она хранит все свои пароли в открытом виде в текстовом файле.

Бобу удалось завладеть зашифрованным файлом с интересной информацией и файлом с паролями, но он не смог понять какой из
паролей ему нужен. Помогите ему решить эту проблему.

Алиса зашифровала свою информацию с помощью библиотеки simple-crypt.
Она представила информацию в виде строки, и затем записала в бинарный файл результат работы метода
simplecrypt.encrypt."""
# from simplecrypt import decrypt
#
# with open('file_sources/encrypted.bin', 'rb') as file, open('file_sources/passwords.txt') as passwords:
#     encrypted = file.read()
#     passwords = list(map(str.strip, passwords.readlines()))
#
#
# for password in passwords:
#     try:
#         print(decrypt(password, encrypted).decode('utf-8'))
#     except:
#         continue
