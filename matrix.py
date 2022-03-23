"""
Подсписки списка 🌶️🌶️
Подсписок — часть другого списка. Подсписок может содержать один элемент, несколько, и даже ни одного. Например,
[1], [2], [3] и [4] — подсписки списка [1, 2, 3, 4]. Список [2, 3] — подсписок списка [1, 2, 3, 4], но список [2, 4]
не подсписок списка [1, 2, 3, 4], так как элементы 22 и 44 во втором списке не смежные. Пустой список — подсписок
 любого списка. Сам список — подсписок самого себя, то есть список [1, 2, 3, 4] подсписок списка [1, 2, 3, 4].

На вход программе подается строка текста, содержащая символы. Из данной строки формируется список. Напишите программу,
которая выводит список, содержащий все возможные подсписки списка, включая пустой список.
"""
# nums = input().split()
# result = [[]]
# for i in range(1, len(nums) + 1):
#     for j in range(len(nums) - i + 1):
#         result.append(nums[j:j + i])
# print(result)

"""Вывести матрицу 1
На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество
строк и столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке;
подряд идут элементы сначала первой строки, затем второй, и т.д.

Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы."""
#
# rows, cols = int(input()), int(input())
# result = [[None] * cols for _ in range(rows)]
# for row in range(rows):
#     for col in range(cols):
#         result[row][col] = input()
# for el in result:
#     print(*el, end='\n')

"""На вход программе подаются два натуральных числа nn и mm, каждое на отдельной строке — количество строк и
столбцов в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы
сначала первой строки, затем второй, и т.д.

Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую
строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый
столбец, и так далее."""

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

"""След матрицы
Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу,
которая выводит след заданной квадратной матрицы."""

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = 0
# for i in range(n):
#     result += matrix[i][i]
# print(result)

"""Больше среднего
Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке,
больших среднего арифметического элементов данной строки."""
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

"""Максимальный в области 1
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы."""
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = []
# for row in range(n):
#     for col in range(n):
#         if row >= col:
#             result.append(matrix[row][col])
# print(max(result))
#
"""Максимальный в области 2 🌶️
Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.
 """
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# result = []
# for row in range(n):
#     for col in range(n):
#         if col <= row <= n - 1 - col or col >= row >= n - 1 - col:
#             result.append(matrix[row][col])
# print(max(result))

"""Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю,
левую и правую.
Напишите программу, которая вычисляет сумму элементов: верхней четверти; правой четверти;
нижней четверти; левой четверти."""
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

"""Таблица умножения
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице. Создайте матрицу
 mult размером n×m и заполните её таблицей умножения по формуле mult[i][j] = i * j."""
# rows, cols = int(input()), int(input())
# mult = [[str(row * col).ljust(3) for col in range(cols)] for row in range(rows)]
# [print(*el) for el in mult]

"""Максимум в таблице
На вход программе подаются два натуральных числа nn и mm — количество строк и столбцов в матрице,
затем nn строк по mm целых чисел в каждой, отделенных символом пробела."""
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

"""Обмен столбцов
Напишите программу, которая меняет местами столбцы в матрице."""
# rows, cols = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(rows)]
# i, j = [int(num) for num in input().split()]
# for row in range(rows):
#     matrix[row][i], matrix[row][j] = matrix[row][j], matrix[row][i]
# [print(*el) for el in matrix]

"""Симметричная матрица
Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали."""
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# transp_matrix = [[None] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         transp_matrix[j][i] = matrix[i][j]
# print('YES' if transp_matrix == matrix else 'NO')

"""Обмен диагоналей
Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной
и побочной диагонали, при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно
поменять местами элемент на главной диагонали и на побочной диагонали)."""

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[n - 1 - i][i] = matrix[n - 1 - i][i], matrix[i][i]
# [print(*el) for el in matrix]

"""Зеркальное отображение
Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы
относительно горизонтальной оси симметрии."""

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# matrix.reverse()
# [print(*el) for el in matrix]

"""Поворот матрицы
Напишите программу, которая поворачивает квадратную матрицу чисел на 90∘ по часовой стрелке."""
# n = int(input())
# matrix = [[i for i in input().split()] for _ in range(n)]
# t_matrix = [[None] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         t_matrix[j][i] = matrix[i][j]
#
# [print(*reversed(el)) for el in t_matrix]

"""Ходы коня
На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и
все клетки, которые бьет конь. Клетку, где стоит конь, отметьте английской буквой N, клетки, которые бьет конь,
отметьте символами *, остальные клетки заполните точками."""
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

"""Магический квадрат 🌶️
Магическим квадратом порядка nn называется квадратная таблица размера n \times nn×n, составленная из всех чисел
1, 2, 3, \ldots, n^21,2,3,…,n
2
  так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. Напишите программу,
которая проверяет, является ли заданная квадратная матрица магическим квадратом."""
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

"""Шахматная доска
На вход программе подаются два натуральных числа nn и mm. Напишите программу для создания матрицы размером n×m,
заполнив её символами . и * в шахматном порядке. В левом верхнем углу должна стоять точка. Выведите полученную
матрицу на экран, разделяя элементы пробелами."""

# m, n = (int(i) for i in input().split())
# table = [[None] * n for _ in range(m)]
# for i in range(m):
#     for j in range(n):
#         if (i + j) % 2 != 0:
#             table[i][j] = '*'
#         else:
#             table[i][j] = '.'
# [print(*el) for el in table]


"""Побочная диагональ
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу размером n×n и
заполняет её по следующему правилу:

числа на побочной диагонали равны 11;
числа, стоящие выше этой диагонали, равны 00;
числа, стоящие ниже этой диагонали, равны 22.
Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом."""

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

"""Заполнение
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу
размером n×m и заполняет её числами от 1 до n⋅m в соответствии с образцом."""

# n, m = (int(i) for i in input().split())
# matrix = []
# for i in range(n):
#     matrix.append([j + i for j in range(1, m * n + 1, n)])
# [print(*el) for el in matrix]
"""5 5
1  6   11  16  21
2  7   12  17  22
3  8   13  18  23
4  9   14  19  24
5  10  15  20  25"""
# ------------------------------------------------------------------------
# n = int(input())
# matrix = [[0] * n for _ in range(n)]
# for i in range(n):
#     matrix[i][i], matrix[i][n - i - 1] = 1, 1
# [print(*el) for el in matrix]
"""5
1 0 0 0 1
0 1 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 0 0 1
"""
# ------------------------------------------------------------------------
# n = int(input())
# matrix = [[1 if n - 1 - j >= i <= j or n - 1 - j <= i >= j else 0 for j in range(n)] for i in range(n)]
# [print(*el) for el in matrix]
"""5
1 1 1 1 1
0 1 1 1 0
0 0 1 0 0
0 1 1 1 0
1 1 1 1 1"""
# ------------------------------------------------------------------------
# n, m = (int(i) for i in input().split())
# row = [i for i in range(1, m + 1)]
# for i in range(n):
#     print(*row)
#     temp = row.pop(0)
#     row.append(temp)
"""5 5
1 2 3 4 5
2 3 4 5 1
3 4 5 1 2
4 5 1 2 3
5 1 2 3 4"""
# ------------------------------------------------------------------------
"""Заполнение змейкой
На вход программе подаются два натуральных числа nn и mm. Напишите программу, которая создает матрицу
размером n×m заполнив её "змейкой" в соответствии с образцом."""
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

"""Заполнение диагоналями 🌶️"""
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
"""5 5
1  2  4  7  11
3  5  8  12 16
6  9  13 17 20
10 14 18 21 23
15 19 22 24 25
"""

"""Спиральная матрица или улитка    !ПРОВАЛ!   """
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


"""Сложение матриц
Напишите программу для вычисления суммы двух матриц."""
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

"""Умножение матриц 🌶️
Напишите программу, которая перемножает две матрицы."""
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

"""Возведение матрицы в степень 🌶️
Напишите программу, которая возводит квадратную матрицу в mm-ую степень."""
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

"""Каждый n-ый элемент
На вход программе подается строка текста, содержащая символы и число nn. Из данной строки формируется
список. Напишите программу, которая разделяет список на вложенные подсписки так, что nn последовательных
элементов принадлежат разным подспискам."""
# nums = [i for i in input().split()]
# result = []
# n = int(input())
# for i in range(n):
#     result.append(nums[i::n])
# print(result)

"""Найти максимум ниже побочной диагонали квадратной матрицы"""
# size = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(size)]
# max_value = 0
# for i in range(size):
#     for j in range(size):
#         if i >= size - 1 - j and matrix[i][j] > max_value:
#             max_value = matrix[i][j]
# print(max_value)

"""Транспонирование матрицы
Напишите программу, которая транспонирует квадратную матрицу."""
# size = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(size)]
# t_matrix = [[None] * size for _ in range(size)]
# for i in range(size):
#     for j in range(size):
#         t_matrix[i][j] = matrix[j][i]
#
# [print(*el) for el in t_matrix]

"""Снежинка
На вход программе подается нечетное натуральное число nn. Напишите программу,
которая создает матрицу размером n \times nn×n заполнив её символами . . Затем заполните символами * среднюю строку
 и столбец матрицы, главную и побочную диагональ матрицы. Выведите полученную матрицу на экран,
 разделяя элементы пробелами."""

# size = int(input())
# matrix = [['*' if i == j or i + j + 1 == size or i == size//2 or j == size//2 else '.' for j in range(size)]
#           for i in range(size)]
# [print(*el) for el in matrix]
"""5
* . * . *
. * * * .
* * * * *
. * * * .
* . * . *"""

"""Симметричная матрица
Напишите программу проверки симметричности квадратной матрицы относительно побочной диагонали."""

# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# transp_matrix = [[None] * n for _ in range(n)]
# matrix.reverse()
# for i in range(n):
#     for j in range(n):
#         transp_matrix[j][i] = matrix[i][j]
# print('YES' if transp_matrix == matrix else 'NO')

""" Латинский квадрат 🌶️
Латинским квадратом порядка nn называется квадратная матрица размером n \times nn×n, каждая строка и каждый
столбец которой содержат все числа от 11 до nn. Напишите программу, которая проверяет, является ли заданная
квадратная матрица латинским квадратом."""
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

"""Ходы ферзя
На шахматной доске 8 \times 88×8 стоит ферзь. Отметьте положение ферзя на доске и все клетки, которые бьет
 ферзь. Клетку, где стоит ферзь, отметьте буквой Q, клетки, которые бьет ферзь, отметьте символами *, остальные
 клетки заполните точками."""
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

"""Диагонали параллельные главной
На вход программе подается натуральное число nn. Напишите программу, которая создает матрицу
размером n \times nn×n и заполняет её по следующему правилу:

на главной диагонали на месте каждого элемента должно стоять число 00;
на двух диагоналях, прилегающих к главной, число 11;
на следующих двух диагоналях число 22, и т.д."""
# size = int(input())
# table = [[abs(i - j) for j in range(size)] for i in range(size)]
# [print(*el) for el in table]
