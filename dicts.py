"""Напишите функцию number_to_words(num), которая принимает в качестве
аргумента натуральное число num и возвращает его словесное описание на русском языке."""
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


""" Камень, ножницы, бумага
Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили
сыграть в камень, ножницы и бумагу. Помогите ребятам бросить честный жребий и определить, кто будет делать
очередной модуль нового курса."""

# rules = {'камень-камень': 'ничья', 'камень-ножницы': 'Тимур', 'камень-бумага': 'Руслан',
#      'ножницы-ножницы': 'ничья','ножницы-бумага': 'Тимур', 'ножницы-камень': 'Руслан',
#      "бумага-бумага": 'ничья','бумага-камень': 'Тимур','бумага-ножницы': 'Руслан'}
#
# tim_rus = f'{input()}-{input()}'
# print(rules[tim_rus])

"""Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке),
чей номер оканчивается на 88."""
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


"""Дополните приведенный код, чтобы он вывел имена всех пользователей (в алфавитном порядке), у которых
нет информации об электронной почте. """
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


"""Набор сообщений
На мобильных кнопочных телефонах текстовые сообщения можно отправлять с помощью цифровой клавиатуры. Поскольку
с каждой клавишей связано несколько букв, для большинства букв требуется несколько нажатий клавиш. При однократном
нажатии цифры генерируется первый символ, указанный для этой клавиши. Нажатие цифры 2, 3, 42,3,4 или 55 раз
генерирует второй, третий, четвертый или пятый символ клавиши."""

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

"""Код Морзе
Код Морзе для представления цифр и букв использует тире и точки.

Напишите программу для кодирования текстового сообщения в соответствии с кодом Морзе."""

# letters = [c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']
# morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---',
#          '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
#          '...--', '....-', '.....', '-....', '--...', '---..', '----.']
# decrypt = {key: value for key, value in zip(letters, morse)}
#
# encrypt = ''.join([i.upper() for i in input() if i not in '.,;:-?! +=-'])
# for letter in encrypt:
#     print(decrypt[letter], end=' ')

"""Дополните приведенный код так, чтобы он объединил содержимое двух словарей dict1 и dict2 по ключам,
складывая значения по одному и тому же ключу, в случае, если ключ присутствует в обоих словарях. Результирующий
словарь необходимо присвоить переменной result."""
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
"""Дополните приведенный код, чтобы он вывел наиболее часто встречающееся слово строки s. Если таких слов несколько,
должно быть выведено то, что меньше в лексикографическом порядке."""

# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange
# ' \ 'barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry
# apricot ' \ 'currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon
# ' \ 'pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple
# ' \ 'barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit ' \
# 'banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate ' \
# 'barley '

# temp = {word: s.count(word) for word in set(s.split())}
# result = []
# max_value = max(temp.values())
# for key, value in temp.items():
#     if temp[key] == max_value:
#         result.append(key)
# print(min(result))
"""Вам доступен список pets, содержащий информацию о собаках и их владельцах.  Каждый элемент списка – это кортеж в
ида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).

Дополните приведенный код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут
перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список
кличек собак (сохранив исходный порядок следования)."""

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

"""Самое редкое слово 🌶️
На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего,
без учета регистра. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке."""

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
"""Исправление дубликатов 🌶️
На вход программе подается строка, содержащая строки-идентификаторы. Напишите программу, которая исправляет их так,
чтобы в результирующей строке не было дубликатов. Для этого необходимо прибавлять к повторяющимся идентификаторам
постфикс _n, где n – количество раз, сколько такой идентификатор уже встречался."""

# words = [i for i in input().split()]
# dict_of_words = {}
# for word in words:
#     dict_of_words[word] = dict_of_words.get(word, -1) + 1
#     if dict_of_words[word] > 0:
#         print(f'{word}_{dict_of_words[word]}', end=' ')
#     else:
#         print(word, end=' ')

"""Словарь программиста
Программисты, как вы уже знаете, постоянно учатся, а в общении между собой используют весьма специфический язык.
Чтобы систематизировать ваш пополняющийся профессиональный лексикон, мы придумали эту задачу. Напишите программу
создания небольшого словаря сленговых программерских выражений, чтобы она потом по запросу возвращала значения из
этого словаря."""

# words_dict = {}
# for _ in range(int(input())):
#     row = input().split(': ')
#     words_dict[row[0].lower()] = row[1]
# for _ in range(int(input())):
#     result = words_dict.get(input().lower(), 'Не найдено')
#     print(result)

"""Анаграммы 1
Анаграмма – слово (словосочетание), образованное путём перестановки букв, составляющих другое слово
(или словосочетание). Например, английские слова evil и live – это анаграммы.

На вход программе подаются два слова. Напишите программу, которая определяет, являются ли они анаграммами."""
# first, second = input(), input()
# f_dict = {i: first.count(i) for i in first}
# s_dict = {i: second.count(i) for i in second}
# print('YES' if f_dict == s_dict else 'NO')

"""Анаграммы 2
На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами
или нет. Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы."""

# first, second = input().lower(), input().lower()
# f_dict = {i: first.count(i) for i in first if i.isalpha()}
# s_dict = {i: second.count(i) for i in second if i.isalpha()}
# print('YES' if f_dict == s_dict else 'NO')

"""Словарь синонимов
Вам дан словарь, состоящий из пар слов-синонимов. Повторяющихся слов в словаре нет. Напишите программу,
которая для одного данного слова определяет его синоним."""

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


"""Страны и города
На вход программе подается список стран и городов каждой страны. Затем даны названия городов. Напишите программу,
которая для каждого города выводит, в какой стране он находится."""
# cities = dict()
# for _ in range(int(input())):
#     key, *values = input().split()
#     cities.update(cities.fromkeys(values, key))
# [print(cities[input()]) for _ in range(int(input()))]

"""Телефонная книга
Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу, которая поможет Тимуру
находить все номера определённого друга.
"""
# phone_numbers = dict()
# for _ in range(int(input())):
#     number, name = input().lower().split()
#     phone_numbers.setdefault(name, []).append(number)
# for _ in range(int(input())):
#     print(*phone_numbers.get(input().lower(), ['абонент не найден']))

"""Секретное слово
Напишите программу для расшифровки секретного слова методом частотного анализа."""

# encripted = input()
# dict_of_transcripted = dict()
# for _ in range(int(input())):
#     letter, count = input().split(': ')
#     dict_of_transcripted[letter] = count
# for letter in encripted:
#     for key, value in dict_of_transcripted.items():
#         if str(encripted.count(letter)) == dict_of_transcripted[key]:
#             print(key, end='')

"""Используя генератор, дополните приведенный код, чтобы получить словарь result , где ключом будет элемент списка
numbers, а значением – отсортированный по возрастанию список всех его делителей начиная с 11.
Примечание 1. Если бы список numbers имел вид: numbers = [1, 6, 18], то результатом был бы словарь
result = {1: [1], 6: [1, 2, 3, 6], 18: [1, 2, 3, 6, 9, 18]}"""

# numbers = [1, 6, 18]
# result = {i: [x for x in range(1, i + 1) if i % x == 0] for i in sorted(numbers)}
# print(result)

"""Дополните приведенный код, используя генератор, так, чтобы получить словарь result , в котором ключом будет
строка – элемент списка words, а значением – список соответствующих кодов ASCII символов данной строки.
Примечание 1. Если бы список words имел вид: words = ['yes', 'hello'], то результатом был бы словарь
result = {'yes': [121, 101, 115], 'hello': [104, 101, 108, 108, 111]}"""

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
"""Порядковый номер
Дана строка текста на русском языке, состоящая из слов и символов пробела. Словом считается последовательность букв,
слова разделены одним пробелом или несколькими.

Напишите программу, определяющую для каждого слова порядковый номер его вхождения в текст именно в этой форме, с
учетом регистра. Для первого вхождения слова программа выведет 11, для второго вхождения того же слова — 22 и т. д."""
# sentence = input().split()
# sentence_count = dict()
# for word in sentence:
#     sentence_count[word] = sentence_count.get(word, 0) + 1
#     print(sentence_count[word], end=' ')

"""Scrabble game
В игре Scrabble каждая буква приносит определенное количество баллов. Общая стоимость слова – сумма баллов его букв.
Чем реже буква встречается, тем больше она ценится:"""
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

"""Строка запроса
Строка запроса (query string) — часть URL адреса, содержащая ключи и их значения. Она начинается после вопросительного
знака и идет до конца адреса. Например:

https://beegeek.ru?name=timur     # строка запроса: name=timur
Если параметров в строке запроса несколько, то они отделяются символом амперсанда &:

https://beegeek.ru?name=timur&color=green     # строка запроса: name=timur&color=green
Напишите функцию build_query_string(), которая принимает на вход словарь с параметрами и возвращает строку запроса,
сформированную из этих параметров."""

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

"""Слияние словарей 🌶️
Напишите функцию merge(), объединяющую словари в один общий. Функция должна принимать список словарей и возвращать
словарь, каждый ключ которого содержит множество (тип данных set) уникальных значений собранных из всех словарей
переданного списка."""

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

"""Опасный вирус 😈
В файловую систему компьютера, на котором развернута наша ❤️ платформа Stepik, проник опасный вирус и сломал контроль
прав доступа к файлам. Говорят, вирус написал один из студентов курса Python для начинающих.

Для каждого файла известно, с какими действиями можно к нему обращаться:

запись W (write, доступ на запись в файл);
чтение R (read, доступ на чтение из файла);
запуск X (execute, запуск на исполнение файла).

Напишите программу для восстановления контроля прав доступа к файлам. Ваша программа для каждого запроса должна будет
возвращать OK если выполняется допустимая операция, и Access denied, если операция недопустима."""
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

"""Покупки в интернет-магазине 🌶️
Напишите программу для подсчета количества единиц каждого вида товара из приобретенных каждым покупателем
интернет-магазина."""
# result = dict()
# for _ in range(int(input())):
#     name, item, count = input().split()
#     result[name] = result.get(name, {})
#     result[name][item] = result.get(name, {}).get(item, 0) + int(count)
# for el in sorted(result):
#     print(f'{el}:', sep='\n')
#     for sub_el in sorted(result[el]):
#         print(f'{sub_el} {result[el][sub_el]}')
