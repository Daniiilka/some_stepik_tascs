"""Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается целым числом – количеством монет, которые можно
положить в копилку. Класс должен поддерживать информацию о количестве монет в копилке, предоставлять возможность
добавлять монеты в копилку и узнавать, можно ли добавить в копилку ещё какое-то количество монет, не превышая ее
вместимость.


При создании копилки, число монет в ней равно 0.
Примечание:
Гарантируется, что метод add(self, v) будет вызываться только если can_add(self, v) – True﻿."""

# class MoneyBox:
#
#     x = 0
#
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#         self.money = 0
#         self.capacity = capacity
#
#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         if v <= (self.capacity - self.money):
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         # положить v монет в копилку
#         self.money += v
#
#     @classmethod
#     def smth(cls, x):
#         cls.x = x * 100
#
#     @staticmethod
#     def square(y):
#         return y*y
#
#
# if __name__ == '__main__':
#     m = MoneyBox(10)
#     n = MoneyBox(20)
#
#     MoneyBox.smth(5)
#
#     print(MoneyBox.x)
#
#     print(MoneyBox.square(MoneyBox.x))
#
#     print(m.x)
#     print(n.x)


"""Вам дается последовательность целых чисел и вам нужно ее обработать и вывести на экран сумму первой пятерки чисел
из этой последовательности, затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени к вам поступают её последовательные части.
Например, сначала первые три элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы последовательности и выводить сумму пятерок
последовательных элементов по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в себе больше элементов, чем ему действительно
необходимо, т. е. он не должен хранить элементы, которые уже вошли в пятерку, для которой была выведена сумма.

Класс должен иметь следующий вид

class Buffer:
    def __init__(self):
        # конструктор без аргументов
    
    def add(self, *a):
        # добавить следующую часть последовательности

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены"""

# class Buffer:
#
#     def __init__(self):
#         self.list = []
#
#     def add(self, *args):
#         for el in args:
#             if len(self.list) == 4:
#                 self.list.append(el)
#                 print(sum(self.list))
#                 self.list.clear()
#             else:
#
#                 self.list.append(el)
#
#     def get_current_part(self):
#         print(self.list)
#
#
# buf = Buffer()
#
# buf.add(1, 2, 3)
# buf.get_current_part() # вернуть [1, 2, 3]
# buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
# buf.get_current_part() # вернуть [6]
# buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
# buf.get_current_part() # вернуть []
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.get_current_part() # вернуть [1]

"""Реализуйте структуру данных, представляющую собой расширенную структуру стек. Необходимо поддерживать добавление
элемента на вершину стека, удаление с вершины стека, и необходимо поддерживать операции сложения, вычитания, умножения
и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний элемент (top1), затем снимается
следующий верхний элемент (top2), и затем как результат операции сложения на вершину стека кладется элемент,
равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) и целочисленного деления
(top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от стандартного класса list.
"""

# class ExtendedStack(list):
#     def sum(self):
#         x = self.pop()
#         y = self.pop()
#         self.append(x + y)
#
#     def sub(self):
#         x = self.pop()
#         y = self.pop()
#         self.append(x - y)
#
#     def mul(self):
#         x = self.pop()
#         y = self.pop()
#         self.append(x * y)
#
#     def div(self):
#         x = self.pop()
#         y = self.pop()
#         self.append(x // y)

"""Одно из применений множественного наследование – расширение функциональности класса каким-то заранее определенным
способом. Например, если нам понадобится логировать какую-то информацию при обращении к методам класса.

Рассмотрим класс Loggable:"""

# import time
#
#
# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))


"""У него есть ровно один метод log, который позволяет выводить в лог (в данном случае в stdout) какое-то сообщение,
добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким образом, чтобы при добавлении элемента
в список посредством метода append в лог отправлялось сообщение, состоящее из только что добавленного элемента.
"""


# class LoggableList(list, Loggable):
#     def append(self, el):
#         super(LoggableList, self).append(el)
#         self.log(el)
#
#
# a = LoggableList()
# a.append('msg 1')
# a.append('msg 2')
# print(a)

# class Tree:
#     def __init__(self, name):
#         self.name = name
#         self.age = 1
#         self.height = 1
#
#     def info(self):
#         return self.name, self.age, self.height
#
#     def grow(self):
#         self.age += 1
#         self.height += 2
#
#
# class FruitTree(Tree):
#     def __init__(self, name):
#         super(FruitTree, self).__init__(name)
#
#     def get_fruits(self):
#         return self.age/2
#
#
# if __name__ == '__main__':
#
#     tr = Tree('Olega')
#     print(tr.info())
#     tr.grow()
#     print(tr.info())
#     frt = FruitTree('Serega')
#     print(frt.get_fruits())
#     print(frt.info())
