"""Требовалось написать программу, которая:

преобразует список floats в список чисел, возведенных в квадрат и округленных с точностью до одного десятичного знака;
фильтрует список words  и оставляет только палиндромы длиной более 44 символов;
находит произведение чисел из списка numbers.
Программист торопился и написал программу неправильно. Доработайте его программу."""

# from functools import reduce
#
# floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
# words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
# numbers = [4, 6, 9, 23, 5]
#
# # Исправьте этот код
# map_result = list(map(lambda num: round(num ** 2, 1), floats))
# filter_result = list(filter(lambda name: name == name[::-1] and len(name) > 4, words))
# reduce_result = reduce(lambda num1, num2: num1 * num2, numbers, 1)
#
# print(map_result)
# print(filter_result)
# print(reduce_result)


"""Напишите программу, которая с помощью встроенных функций filter(), map(), sorted() и reduce() выводит в алфавитном
порядке список primary городов с населением более 10 000 000 человек, в формате:

Cities: Beijing, Buenos Aires, ..."""

# from functools import reduce
#
# data = [['Tokyo', 35676000, 'primary'],
#         ['New York', 19354922, 'nan'],
#         ['Mexico City', 19028000, 'primary'],
#         ['Mumbai', 18978000, 'admin'],
#         ['Sao Paulo', 18845000, 'admin'],
#         ['Delhi', 15926000, 'admin'],
#         ['Shanghai', 14987000, 'admin'],
#         ['Kolkata', 14787000, 'admin'],
#         ['Los Angeles', 12815475, 'nan'],
#         ['Dhaka', 12797394, 'primary'],
#         ['Buenos Aires', 12795000, 'primary'],
#         ['Karachi', 12130000, 'admin'],
#         ['Cairo', 11893000, 'primary'],
#         ['Rio de Janeiro', 11748000, 'admin'],
#         ['Osaka', 11294000, 'admin'],
#         ['Beijing', 11106000, 'primary'],
#         ['Manila', 11100000, 'primary'],
#         ['Moscow', 10452000, 'primary'],
#         ['Istanbul', 10061000, 'admin'],
#         ['Paris', 9904000, 'primary']]
#
# sorted_cities = list(filter(lambda el: el[1] > 10000000 and el[2] == 'primary', data))
# names_of_cities = sorted(list(map(lambda el: el[0], sorted_cities)))
# result = reduce(lambda x, y: x + ', ' + y, names_of_cities)
#
# print('Cities: ' + result)

"""Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и возвращает
значение True, если он делится без остатка на 1919 или на 1313 и False в противном случае."""

# func = lambda el: el % 19 == 0 or el % 13 == 0

# is_non_negative_num = lambda x: True if x in '.0123456789' and x.count('.') < 2 and not x.startswith('-') else False

# is_num = lambda s: '-' not in s[1:] and s.count('.') <= 1 and set(s) <= set('-.1234567890')
#
# print(is_num('10.34ab'))
# print(is_num('10.45'))
# print(is_num('-18'))
# print(is_num('-34.67'))
# print(is_num('987'))
# print(is_num('abcd'))
# print(is_num('123.122.12'))
# print(is_num('-123.122'))
# print(is_num('--13.2'))
"""Напишите программу, которая с помощью встроенных функций map() и filter() удаляет из списка numbers все нечетные
элементы, большие 4747, а все четные элементы нацело делит на два (целочисленное деление – //). Полученные числа
следует вывести на одной строке, разделив символом пробела и сохранив исходный порядок. """
# numbers = [46, 61, 34, 17, 56, 26, 93, 1, 3, 82, 71, 37, 80, 27, 77, 94, 34, 100, 36, 81, 33, 81, 66, 83, 41, 80,
# 80, 93, 40, 34, 32, 16, 5, 16, 40, 93, 36, 65, 8, 19, 8, 75, 66, 21, 72, 32, 41, 59, 35, 64, 49, 78, 83, 27, 57,
# 53, 43, 35, 48, 17, 19, 40, 90, 57, 77, 56, 80, 95, 90, 27, 26, 6, 4, 23, 52, 39, 63, 74, 15, 66, 29, 88, 94, 37,
# 44, 2, 38, 36, 32, 49, 5, 33, 60, 94, 89, 8, 36, 94, 46, 33]
#
# numbers = filter(lambda x: x if x <= 47 else x % 2 == 0, numbers)
# numbers = map(lambda x: x // 2 if x % 2 == 0 else x, numbers)
# print(*numbers)

"""Список data содержит информацию о численности населения некоторых штатов США. Напишите программу сортировки по
убыванию списка data на основании последнего символа в названии штата. Затем распечатайте элементы этого списка,
каждый на новой строке в формате:

<название штата>: <численность населения>

Vermont: 626299
Massachusetts: 7029917
..."""
# data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
#         (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
#         (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
#         (7029917, 'Massachusetts'), (6910840, 'Tennessee')]
#
#
# data.sort(key=lambda x: x[1][-1], reverse=True)
# [print(f'{el[1]}: {el[0]}') for el in data]

"""Список data содержит слова на русском языке. Напишите программу его сортировки по возрастанию длины слов, а затем в
лексикографическом порядке. Отсортированные слова следует вывести на одной строке, разделив символом пробела."""
# data = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг',
#         'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребенок', 'сила', 'конец', 'вид',
#         'система', 'часть', 'город', 'отношение', 'женщина', 'деньги']
# data.sort()
# data.sort(key=lambda x: len(x))
# print(*data)


"""Список mixed_list содержит целочисленные и строковые значения. Напишите программу, которая с помощью встроенной
функции max() находит и выводит наибольшее числовое значение в указанном списке.

Примечание 1. Для решения задачи используйте анонимную функцию и необязательный аргумент key  функции max()."""
# mixed_list = ['tuesday', 'abroad', 'abuse', 'beside', 'monday', 'abate', 'accessory', 'absorb', 1384878, 'sunday',
# 'about', 454805, 'saturday', 'abort', 2121919, 2552839, 977970, 1772933, 1564063, 'abduct', 901271, 2680434,
# 'bicycle', 'accelerate', 1109147, 942908, 'berry', 433507, 'bias', 'bestow', 1875665, 'besides', 'bewilder',
# 1586517, 375290, 1503450, 2713047, 'abnormal', 2286106, 242192, 701049, 2866491, 'benevolent', 'bigot', 'abuse',
# 'abrupt', 343772, 'able', 2135748, 690280, 686008, 'beyond', 2415643, 'aboard', 'bet', 859105, 'accident', 2223166,
# 894187, 146564, 1251748, 2851543, 1619426, 2263113, 1618068, 'berth', 'abolish', 'beware', 2618492, 1555062,
# 'access', 'absent', 'abundant', 2950603, 'betray', 'beverage', 'abide', 'abandon', 2284251, 'wednesday', 2709698,
# 'thursday', 810387, 'friday', 2576799, 2213552, 1599022, 'accept', 'abuse', 'abound', 1352953, 'bid', 1805326,
# 1499197, 2241159, 605320, 2347441]
#
# print(max(mixed_list, key=lambda x: x if str(x).isdigit() else 0))

"""Список mixed_list содержит целочисленные и строковые значения. Напишите программу его сортировки по неубыванию
значений элементов, при этом числа должны следовать до строк.  Элементы отсортированного списка выведите на одной
строке, разделив символом пробела."""
# mixed_list = ['a', 'ab', 3, 5, 1, 8, 0, 'c', 'ac', 'aab']
# mixed_list.sort(key=lambda x: (type(x) == str, x))
# print(*mixed_list)
"""Противоположный цвет
В цветовой схеме RGB цвета задаются с помощью трех компонентов:

R — интенсивность красной составляющей цвета;
G — интенсивность зеленой составляющей цвета;
B — интенсивность синей составляющей цвета.
Противоположные цвета задаются как RGB и (255-R)(255-G)(255-B). Считается, что такие цвета хорошо гармонируют друг с
другом.

Напишите программу, которая по трем компонентам заданного цвета, находит компоненты противоположного цвета. """
# rgb = [int(i) for i in input().split()]
# print(*map(lambda x: abs(255 - x), rgb))

"""Значение многочлена 🌶️
На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число xx на
 торой строке. Напишите программу, которая вычисляет значение указанного многочлена при заданном значении xx."""
# from functools import reduce
#
#
# def evaluate(coefficients, x):
#     result = list(map(lambda num, n: num * (x ** n), coefficients, range(len(coefficients) - 1, -1, -1)))
#     r = reduce(lambda x, y: x + y, result)
#     return r
#
#
# c = [int(i) for i in input().split()]
# n = int(input())
# print(evaluate(c, n))

"""Реализуйте функцию mod_checker(x, mod=0), которая будет генерировать лямбда функцию от одного аргумента y,
которая будет возвращать True, если остаток от деления y на x равен mod, и False иначе.
"""


# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod
#
#
# mod_3 = mod_checker(3)
#
# print(mod_3(3)) # True
# print(mod_3(4)) # False
#
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4)) # True

"""
Реализация функции partial и ее аналога на lambda
"""
# from functools import partial
# from util import hyperbola
#
# if __name__ == '__main__':
#     x_values = range(0, 100)
#
#     res = list(map(lambda el: hyperbola(el, 100), x_values))
#     print(res)
#
#     res_partial = list(map(partial(hyperbola, y=100), x_values))
#     print(res_partial)
