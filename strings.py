"""Нужно проверить, являются ли строчки 'a' и 'b' перестановками"""
# def is_permutation(a: str, b: str) -> bool:
#
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


"""Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два
слова word1 и word2 и возвращает значение True если слова имеют одинаковую длину и о
тличаются ровно в 1 символе и False в противном случае."""

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

"""Напишите функцию is_correct_bracket(text), которая принимает в качестве
аргумента непустую строку text, состоящую из символов ( и ) и возвращает значение
True если поступившая на вход строка является правильной скобочной последовательностью
и False в противном случае."""

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
"""Напишите функцию convert_to_python_case(text), которая принимает в
качестве аргумента строку в «верблюжьем регистре» и преобразует
его в «змеиный регистр»."""
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

"""Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно
панграммы используют для презентации шрифтов, чтобы можно было в одной фразе
рассмотреть все глифы.

Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку
текста на английском языке и возвращает значение True если текст является панграммой
 и False в противном случае."""

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


"""Кремниевая долина 🌶️🌶️
Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в
качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.

Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней
присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то
холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы"""
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


"""Вашей программе на вход подаются три строки s, a, b, состоящие из строчных латинских букв.
За одну операцию вы можете заменить все вхождения строки a в строку s на строку b.

Например, s = "abab", a = "ab", b = "ba", тогда после выполнения одной операции строка s перейдет в строку "baba",
после выполнения двух и операций – в строку "bbaa", и дальнейшие операции не будут изменять строку s.

Необходимо узнать, после какого минимального количества операций в строке s не останется вхождений строки a. Если
пераций потребуется более 1000, выведите Impossible.

Выведите одно число – минимальное число операций, после применения которых в строке s не останется вхождений строки a,
или Impossible, если операций потребуется более 1000."""

# if __name__ == '__main__':
#     counter = 0
#     s, a, b = (input() for _ in range(3))
#     while a in s:
#         s = s.replace(a, b)
#         counter += 1
#         if counter > 1000:
#             counter = 'impossible'
#             break
#     print(counter)

"""Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"
"""

# `if __name__ == '__main__':
#     s, t = input(), input()
#     counter = 0
#     for i in range(len(s) + 1):
#         if s.startswith(t, i):
#             counter += 1
#
#     print(counter)`
