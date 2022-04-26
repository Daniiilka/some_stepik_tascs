"""Случайная строка
Вам доступен текстовый файл lines.txt из нескольких строк. Напишите программу, которая выводит на экран случайную
строку из этого файла."""
# import random
# file = open('file_sources/lines.txt', encoding='utf-8')
# print(random.choice(file.readlines()))
# file.close()

"""Сумма двух-1
Вам доступен текстовый файл numbers.txt из двух строк, на каждой из них записано целое число. Напишите программу,
выводящую на экран сумму этих чисел."""

# with open('file_sources/numbers.txt', encoding='utf-8') as file:
#     nums = file.readlines()
#     print(int(nums[0]) + int(nums[1]))

"""Сумма двух-2
Вам доступен текстовый файл nums.txt. В файле записано два целых числа, они могут быть разделены символами пробела и
конца строки. Напишите программу, выводящую на экран сумму этих чисел."""

# with open('file_sources/nums.txt', encoding='utf-8') as file:
#     result = sum(map(int, file.read().split()))
#     print(result)

"""Общая стоимость
Вам доступен текстовый файл prices.txt с информацией о заказе из интернет магазина. В нем каждая строка с помощью
символа табуляции (\t) разделена на три колонки:

наименование товара;
количество товара (целое число);
цена (в рублях) товара за 11 шт (целое число).
Напишите программу, выводящую на экран общую стоимость заказа."""

# with open('file_sources/prices.txt', encoding='utf-8') as file:
#     result = 0
#     # отрезаю срезом наименование товара и составляю список [количество, цена]
#     list_of_prices = [el.split()[1:] for el in file.readlines()]
#     for el in list_of_prices:
#         result += int(el[0]) * int(el[1])
#     print(result)
#

"""Переворот строки
Вам доступен текстовый файл text.txt с одной строкой текста. Напишите программу, которая выводит на экран эту строку в
обратном порядке."""

# with open('file_sources/text.txt', encoding='utf-8') as file:
#     text = file.readline().rstrip()
#     print(text[::-1])


"""Обратный порядок
Вам доступен текстовый файл data.txt, в котором записаны строки текста. Напишите программу, выводящую все строки
данного файла в обратном порядке: сначала последнюю, затем предпоследнюю и т.д."""

# with open('file_sources/data.txt', encoding='utf-8') as file:
#     sentences = list(map(str.rstrip, file.readlines()))
#     print(*sentences[::-1], sep='\n')

"""Длинные строки
Вам доступен текстовый файл lines.txt, в котором записаны строки текста. Напишите программу, которая выводит все строки
наибольшей длины из файла, не меняя их порядок."""

# with open('file_sources/lines.txt', encoding='utf-8') as file:
#     list_of_lines = list(map(str.rstrip, file.readlines()))
# max_len = max(map(len, list_of_lines))
# [print(el) for el in list_of_lines if len(el) == max_len]

"""Сумма чисел в строках
Вам доступен текстовый файл numbers.txt, каждая строка которого может содержать одно или несколько целых чисел,
разделенных одним или несколькими пробелами.

Напишите программу, которая вычисляет сумму чисел в каждой строке и выводит эту сумму на экран (для каждой строки
выводится сумма чисел в этой строке)."""

# with open('file_sources/numbers.txt', encoding='utf-8') as file:
#     for line in file:
#         result = sum([int(i) for i in line.split()])
#         print(result)


"""Сумма чисел в файле
Вам доступен текстовый файл nums.txt. В файле могут быть записаны целые неотрицательные числа и все, что угодно.
Числом назовем последовательность одной и более цифр, идущих подряд (число всегда неотрицательно).

Напишите программу, которая вычисляет сумму всех чисел, записанных в файле."""

# with open('file_sources/nums.txt', encoding='utf-8') as file:
#     result_string = ''.join(i if i.isdigit() else ' ' for i in file.read())
# print(sum([int(i) for i in result_string.split()]))


"""Статистика по файлу
Вам доступен текстовый файл file.txt, набранный латиницей. Напишите программу, которая выводит количество букв
латинского алфавита, слов и строк. Выведите три найденных числа в формате, приведенном в примере."""

# with open('file_sources/file.txt', encoding='utf-8') as file:
#     len_of_all_text = file.read()
#
# count_words = len(len_of_all_text.split())
# count_lines = len_of_all_text.count('\n') + 1
# letters = len([i for i in len_of_all_text if i.isalpha()])
#
# print(f'Input file contains:\n{letters} letters\n{count_words} words\n{count_lines} lines ')

"""Random name and surname
Вам доступны два текстовых файла first_names.txt и last_names.txt, один с именами, другой с фамилиями.

Напишите программу, которая c помощью модуля random создает 33 случайные пары имя + фамилия, а затем выводит их,
каждую на отдельной строке."""
# import random
# with open('file_sources/first_names.txt') as fn, open('file_sources/last_names.txt') as ln:
#     fn_lines, ln_lines = fn.readlines(), ln.readlines()
# random.shuffle(fn_lines)
# random.shuffle(ln_lines)
# [print(f'{fn_lines.pop().strip()} {ln_lines.pop().strip()}') for _ in range(3)]

"""Необычные страны
Вам доступен текстовый файл population.txt с названиями стран и численностью их населения, разделенными символом
табуляции '\t'.

Напишите программу выводящую все страны, название которых начинается с буквы 'G', численность населения которых больше
чем 500 \, 000500000 человек, не меняя их порядок."""

# with open('file_sources/population.txt') as population:
#     list_of_population = ([el.strip().split('\t') for el in population])
# result_list = list(filter(lambda el: int(el[-1]) > 500000 and el[0][0] == 'G', list_of_population))
# [print(el[0]) for el in result_list]

"""CSV-файл
Вам доступен CSV-файл data.csv, содержащий информацию в csv формате. Напишите функцию read_csv для чтения данных из
этого файла. Она должна возвращать список словарей, интерпретируя первую строку как имена ключей, а каждую последующую
строку как значения этих ключей."""

# def read_csv():
#     result = []
#     with open('file_sources/data.csv') as data:
#         keys = data.readline().strip().split(',')
#
#     for line in data:
#         result.append(dict(zip(keys, line.strip().split(','))))
#
#     return result
#
#
# print(read_csv())

"""Случайные числа
Напишите программу, записывающую в текстовый файл random.txt 25 случайных чисел в диапазоне от 111 до 777
(включительно), каждое с новой строки."""

# import random
#
# with open('file_sources/random.txt', 'w') as file:
#     result = [f'{random.randint(111, 777)}\n' for _ in range(25)]
#     file.writelines(result)

"""Нумерация строк
Вам доступен текстовый файл input.txt, состоящий из нескольких строк. Напишите программу для записи содержимого этого
файла в файл output.txt в виде нумерованного списка, где перед каждой строкой стоит ее номер, символ ) и пробел.
Нумерация строк должна начинаться с 1."""

# with open('file_sources/input.txt') as inp, open('file_sources/output.txt', 'w') as out:
#     inp_lines = [f'{i}) {j}' for i, j in enumerate(inp.readlines(), 1)]
#     out.writelines(inp_lines)

"""Подарок на новый год
Вам доступен текстовый файл class_scores.txt с оценками за итоговый тест на строках вида: фамилия оценка (фамилия и
оценка разделены пробелом). Оценка - целое число от 00 до 100100 включительно.

Напишите программу для добавления 55 баллов к каждому результату теста и вывода фамилий и новых результатов тестов в
файл new_scores.txt."""

# with open('file_sources/class_scores.txt', encoding='utf-8') as class_scores, \
#         open('file_sources/new_scores.txt', 'w') as new_scores:
# # создаю список из необходимых данных, обрезая лишние символы
#     scores_lines = [el.strip().split() for el in class_scores.readlines()]
#     result = list(map(lambda el: f'{el[0]} {min(100, int(el[1]) + 5)}', scores_lines))
#
#     print(*result, sep='\n', file=new_scores)

"""Загадка от Жака Фреско 🌶️
Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех
возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов разных цветов.
Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию загадки от
Жака Фреско."""

# with open('file_sources/goats.txt') as file, open('file_sources/answer.txt', 'w') as answer:
#     # отрезаю лишнюю часть
#     for row in file:
#         if row.startswith('GOATS'):
#             goats = [el.strip() for el in file.readlines()]
#     # создаю список из подходящих элементов
#     result_goats = [key for key in set(goats) if int(goats.count(key)/len(goats) * 100) > 7]
#     print(*sorted(result_goats), sep='\n', file=answer)

"""Конкатенация файлов 🌶️
На вход программе подается натуральное число nn и nn строк с названиями файлов. Напишите программу, которая создает
файл output.txt и выводит в него содержимое всех файлов с указанными именами, не меняя их порядка."""

# with open('output.txt', 'w') as file:
#     for _ in range(int(input())):
#         with open(input()) as r_file:
#             result = r_file.read()
#         print(result, file=file)
#
# with open('output.txt', 'w') as file:
#     for _ in range(int(input())):
#         with open(input()) as r_file:
#             file.write(r_file.read())

"""Лог файл 🌶️
Вам доступен текстовый файл logfile.txt с информацией о времени входа пользователя в систему и выхода из нее. Каждая
строка файла содержит три значения, разделенные запятыми и символом пробела: имя пользователя, время входа, время
выхода, где время указано в 2424-часовом формате.

Напишите программу, которая создает файл output.txt и выводит в него имена всех пользователей (не меняя порядка
следования), которые были в сети не менее часа.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Считайте, что каждый пользователь был только раз в системе, то есть в файле нет двух строк с одинаковым
пользователем."""

# with open('file_sources/logfile.txt', encoding='utf-8') as log:
#     lists_of_users = [el.strip().split(',') for el in log.readlines()]
#     for el in lists_of_users:
#         raw_num_1 = el[1].split(':')
#         raw_num_2 = el[2].split(':')
#         num_1 = int(raw_num_1[0]) * 60 + int(raw_num_1[1])
#         num_2 = int(raw_num_2[0]) * 60 + int(raw_num_2[1])
#         if num_2 - num_1 >= 60:
#             with open('output.txt', 'a', encoding='utf-8') as output:
#                 print(el[0], file=output)

"""Вам дается текстовый файл, содержащий некоторое количество непустых строк.
На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке."""

# with open('file_sources/dataset_24465_4.txt') as inner, open('file_sources/result.txt', 'w') as outer:
#     inner_lines = inner.read().splitlines()
#     print(*list(reversed(inner_lines)), sep='\n', file=outer)


"""Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.

Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории, в которых есть
хотя бы один файл с расширением ".py".

Ответом на данную задачу будет являться файл со списком таких директорий, отсортированных в лексикографическом
порядке."""
# import os
#
#
# def finder(directory):
#     result_dirs = set()
#     for current_dir, _, files in os.walk(directory):
#         for file in files:
#             if file.endswith('.py'):
#                 result_dirs.add(current_dir)
#     return sorted(list(result))
#
#
# with open('result.txt', 'w') as result:
#     print(*finder('main'), sep='\n', file=result)
