# class MailBox:
#     def __init__(self):
#         self.inbox_list = []
#
#     def recieve(self):
#         lst_in = ['sc_lib@list.ru; От Балакирева; Успехов в IT!',
#                   'mail@list.ru; Выгодное предложение; Вам одобрен кредит.',
#                   'Python ООП; Балакирев С.М.; 2022',
#                   'mail123@list.ru; Розыгрыш; Вы выиграли 1 млн. руб. Переведите 30 тыс. руб., чтобы его получить.']
#         # lst_in = list(map(str.strip, sys.stdin.readlines()))
#         self.inbox_list = [MailItem(*row.split("; ")) for row in lst_in]
#
#
# class MailItem:
#     def __init__(self, mail_from, title, content):
#         self.mail_from = mail_from
#         self.title = title
#         self.content = content
#         self.is_read = False
#
#     def set_read(self, fl_read):
#         self.is_read = fl_read
#
#     def __bool__(self):
#         return self.is_read
#
#
# mail = MailBox()
# mail.recieve()
# [mail.inbox_list[i].set_read(True) for i in (0, -1)]
# inbox_list_filtered = list(filter(bool, mail.inbox_list))


# class Line:
#     def __init__(self, x1, y1, x2, y2):
#         self.x1 = x1
#         self.y1 = y1
#         self.x2 = x2
#         self.y2 = y2
#
#     def __len__(self):
#         return int(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)
#
#
# print(len(Line(1, 2, 3, 4)))


# class Ellipse:
#     def __init__(self, *args):
#         if args and len(args) == 4:
#             self.x1 = args[0]
#             self.y1 = args[1]
#             self.x2 = args[2]
#             self.y2 = args[3]
#
#     def __bool__(self):
#         return all([hasattr(self, "x1"), hasattr(self, "y1"), hasattr(self, "x2"), hasattr(self, "y2")])
#
#     def get_coords(self):
#         if not self:
#             raise AttributeError('нет координат для извлечения')
#         return (self.x1, self.y1, self.x2, self.y2)
#
#
# lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
# [ellipse.get_coords() for ellipse in lst_geom if ellipse]


# from random import sample
#
#
# class GamePole:
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self, n, m, total_mines):
#         self.__pole_cells = tuple([tuple([Cell() for mi in range(m)]) for ni in range(n)])
#         self.__total_mines = total_mines
#         self.n, self.m = n, m
#
#     @property
#     def pole(self):
#         return self.pole_cells
#
#     @property
#     def pole(self):
#         return self.__pole_cells
#
#     def init_pole(self):
#         [[setattr(obj, "is_open", False) for obj in row] for row in self.pole]
#         mines_list = tuple([(x // self.m, x % self.m) for x in sample(range(self.n * self.m), self.__total_mines)])
#         [setattr(self.pole[x][y], "is_mine", True) for x, y in mines_list]
#         mines_check = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
#         [[setattr(self.pole[n][m], "number", sum([self.pole[n + i][m + j].is_mine for i, j in mines_check if
#                                                         0 <= n + i <= self.n - 1 and 0 <= m + j <= self.m - 1])) for m
#           in range(self.m)] for n in range(self.n)]
#
#     def open_cell(self, i, j):
#         if not isinstance(i, int) or not isinstance(j, int) or 0 > i > self.n - 1 or 0 > j > self.m - 1:
#             raise IndexError('некорректные индексы i, j клетки игрового поля')
#         setattr(self.pole[i][j], "is_open", True)
#
#     def show_pole(self):
#         for row in self.pole:
#             for cell in row:
#                 print(cell, end=" ")
#             print()
#
#
# class Cell:
#     def __init__(self):
#         self.is_mine = False
#         self.number = 0
#         self.is_open = False
#
#     @property
#     def is_mine(self):
#         return self.__is_mine
#
#     @is_mine.setter
#     def is_mine(self, flag):
#         if not isinstance(flag, bool):
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_mine = flag
#
#     @property
#     def number(self):
#         return self.__number
#
#     @number.setter
#     def number(self, number):
#         if not isinstance(number, int) or not 0 <= number <= 8:
#             raise ValueError("недопустимое значение атрибута")
#         self.__number = number
#
#     @property
#     def is_open(self):
#         return self.__is_open
#
#     @is_open.setter
#     def is_open(self, flag):
#         if not isinstance(flag, bool):
#             raise ValueError("недопустимое значение атрибута")
#         self.__is_open = flag
#
#     def __bool__(self):
#         return not self.is_open
#
#     def __str__(self):
#         return "*" if self.is_mine else str(self.number)
#
#
# gp1 = GamePole(10, 20, 10)
# gp1.init_pole()
# gp1.show_pole()


# class Vector:
#     def __init__(self, *args):
#         self.coord = [*args]
#
#     def validate(self, other):
#         if len(self.coord) != len(other.coord):
#             raise ArithmeticError('размерности векторов не совпадают')
#
#     def __add__(self, other):
#         self.validate(other)
#         return Vector(*map(sum, zip(self.coord, other.coord)))
#
#     def __iadd__(self, other):
#         if isinstance(other, Vector):
#             self.validate(other)
#             self.coord = list(map(sum, zip(self.coord, other.coord)))
#             return self
#         self.coord = [a + other for a in self.coord]
#         return self
#
#     def __sub__(self, other):
#         self.validate(other)
#         return Vector(*[a - b for a, b in zip(self.coord, other.coord)])
#
#     def __isub__(self, other):
#         if isinstance(other, Vector):
#             self.validate(other)
#             self.coord = [a - b for a, b in zip(self.coord, other.coord)]
#             return self
#         self.coord = [a - other for a in self.coord]
#         return self
#
#     def __mul__(self, other):
#         self.validate(other)
#         return Vector(*[a * b for a, b in zip(self.coord, other.coord)])
#
#     def __eq__(self, other):
#         self.validate(other)
#         return self.coord == other.coord
#
#
# v1 = Vector(1, 2, 3, 4, 5)
# v2 = Vector(1, 2, 3, 4, 5)
# v3 = v1 - v2
# print(v3.coord)
# v1 += v2
# print(v1.coord)


# class Record:
#     def __init__(self, **kwargs):
#         self.__dict__ = kwargs
#
#     def validate(self, item):
#         if item > len(self.__dict__):
#             raise IndexError('неверный индекс поля')
#
#     def __getitem__(self, item):
#         self.validate(item)
#         return self.__dict__[[*self.__dict__.keys()][item]]
#
#     def __setitem__(self, key, value):
#         self.validate(key)
#         setattr(self, (*self.__dict__.keys(),)[key], value)
#
#
# r = Record(pk=1, title='Python ООП', author='Балакирев')
# print(*r.__dict__.keys())
# r[1] = "sjg"
# print(r[1])


# class Track:
#     def __init__(self, start_x, start_y):
#         self.start_x = start_x
#         self.start_y = start_y
#         self.points = []
#
#     def add_point(self, x, y, speed):
#         self.points.append([(x, y), speed])
#
#     def validate(self, indx):
#         if not 0 <= indx < len(self.points):
#             raise IndexError('некорректный индекс')
#
#     def __getitem__(self, key):
#         self.validate(key)
#         return self.points[key]
#
#     def __setitem__(self, key, value):
#         self.validate(key)
#         self.points[key][1] = value
#
#
# tr = Track(10, -5.4)
# tr.add_point(20, 0, 100)  # первый линейный сегмент: indx = 0
# tr.add_point(50, -20, 80)  # второй линейный сегмент: indx = 1
# tr.add_point(63.45, 1.24, 60.34)  # третий линейный сегмент: indx = 2
# print(tr.points)
# tr[2] = 60
# c, s = tr[2]
# print(c, s)
#
# res = tr[3]  # IndexError


# class Array:
#     def __init__(self, max_length, cell):
#         self.max_length = max_length
#         self.cell = cell
#         self.array = [Integer() for _ in range(self.max_length)]
#
#     def __str__(self):
#         return " ".join([str(cell.value) for cell in self.array])
#
#     def validate(self, item):
#         if not isinstance(item, int) or not 0 <= item < self.max_length:
#             raise IndexError('неверный индекс для доступа к элементам массива')
#
#     def __getitem__(self, item):
#         self.validate(item)
#         return self.array[item].value
#
#     def __setitem__(self, key, value):
#         self.validate(key)
#         self.array[key].value = value
#
#
# class Integer:
#     def __init__(self, start_value=0):
#         self.value = start_value
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         if not isinstance(value, int):
#             raise ValueError('должно быть целое число')
#         self.__value = value
#
#
# ar_int = Array(10, cell=Integer)
# print(ar_int[3])
# print(ar_int)  # должны отображаться все значения массива в одну строчку через пробел
# ar_int[1] = 10
# print(ar_int)
# ar_int[1] = 10.5 # должно генерироваться исключение ValueError
# ar_int[10] = 1 # должно генерироваться исключение IndexError


# class IntegerValue:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, int):
#             raise ValueError('возможны только целочисленные значения')
#         setattr(instance, self.name, value)
#
#
# class CellInteger:
#     value = IntegerValue()
#
#     def __init__(self, start_value=0):
#         self.value = start_value
#
#
# class TableValues:
#     def __init__(self, rows, cols, **kwargs):
#         if not kwargs:
#             raise ValueError('параметр cell не указан')
#         self.cell = kwargs["cell"]
#         self.cells = tuple([tuple([self.cell() for c in range(cols)]) for r in range(rows)])
#
#     def __getitem__(self, indx):
#         return self.cells[indx[0]][indx[1]].value
#
#     def __setitem__(self, key, value):
#         self.cells[key[0]][key[1]].value = value
#
#
# table = TableValues(2, 3, cell=CellInteger)
# print(table[0, 1])
# table[1, 1] = 10
# print(table[1, 1])


# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, next):
#         if isinstance(next, StackObj) or next is None:
#             self.__next = next
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.last = None
#
#     def push(self, obj):
#         if self.last:
#             self.last.next = obj
#         self.last = obj
#         if self.top is None:
#             self.top = obj
#
#     def pop(self):
#         if self.top is None:
#             return
#         curr = self.top
#         while curr and curr.next != self.last:
#             curr = curr.next
#         if curr:
#             curr.next = None
#         last = self.last
#         self.last = curr
#         if self.last is None:
#             self.top = None
#         return last
#
#     def get_data(self):
#         data_lst = []
#         curr_obj = self.top
#         while curr_obj:
#             data_lst.append(curr_obj.data)
#             curr_obj = curr_obj.next
#         return data_lst
#
#     def __add__(self, other):
#         self.push(other)
#         return self
#
#     def __mul__(self, other):
#         for x in other:
#             self.push(StackObj(x))
#         return self
#
#     @staticmethod
#     def check_index(indx):
#         if not isinstance(indx, int):
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.check_index(item)
#         if not self.top:
#             raise IndexError('неверный индекс')
#         curr_obj = self.top
#         for i in range(0, item + 1):
#             if i == item:
#                 return curr_obj
#             curr_obj = curr_obj.next
#             if not curr_obj:
#                 raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         if not self.top:
#             raise IndexError('неверный индекс')
#         curr_obj = self.top
#         if key == 0:
#             self.top = value
#             self.top.next = curr_obj.next
#             if not self.top.next:
#                 self.last = self.top
#             return
#         for i in range(0, key + 1):
#             if i == key:
#                 prev.next = value
#                 value.next = curr_obj.next
#                 if not value.next:
#                     self.last = value
#                 break
#             prev = curr_obj
#             curr_obj = curr_obj.next
#             if not curr_obj:
#                 raise IndexError('неверный индекс')
#
#
# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
# st[1] = StackObj("new obj2")
# print(st[2].data)  # obj3
# print(st[1].data)  # new obj2
# res = st[3]  # исключение IndexError


# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = [*args]
#
#     def __getitem__(self, item):
#         return tuple(self.coords[item]) if isinstance(item, slice) else self.coords[item]
#
#     def __setitem__(self, key, value):
#         self.coords[key] = value
#
#
# v = RadiusVector(1, 1, 1, 1)
# # print(v[1])  # 1
# v[::] = 1, 2, 3, 4
# print(v[2])  # 3
# print(v[1:])  # (2, 3, 4)
# v[0] = 10.5
# print(v[1:3])


# class TicTacToe:
#     def __init__(self):
#         self.pole = tuple([tuple([Cell() for _ in "..."]) for _ in "..."])
#
#     def clear(self):
#         [[setattr(cell, "is_free", True) for cell in row] for row in self.pole]
#         [[setattr(cell, "value", 0) for cell in row] for row in self.pole]
#
#     @staticmethod
#     def check_indx(indx):
#         if any(x not in range(3) for x in indx if not isinstance(x, slice)):
#             raise IndexError('неверный индекс клетки')
#
#     def __setitem__(self, key, value):
#         self.check_indx(key)
#         if not self.pole[key[0]][key[1]]:
#             raise ValueError('клетка уже занята')
#         self.pole[key[0]][key[1]].value = value
#         self.pole[key[0]][key[1]].is_free = False
#
#     def __getitem__(self, item):
#         self.check_indx(item)
#         if isinstance(item[0], slice):
#             return tuple([self.pole[i][item[1]].value for i in range(3)])
#         if isinstance(item[1], slice):
#             return tuple([self.pole[item[0]][i].value for i in range(3)])
#         return self.pole[item[0]][item[1]].value
#
#
# class Cell:
#     def __init__(self, is_free=True, value=0):
#         self.is_free = is_free
#         self.value = value
#
#     def __bool__(self):
#         return self.is_free
#
#
# g = TicTacToe()
# g.clear()
# assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
# g[1, 1] = 1
# g[2, 1] = 2
# assert g[1, 1] == 1 and g[
#     2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"
#
# try:
#     res = g[3, 0]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"
#
# try:
#     g[3, 0] = 5
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"
#
# g.clear()
# g[0, 0] = 1
# g[1, 0] = 2
# g[2, 0] = 3
# print(g[0, :])
# print(g[1, :])
# print(g[:, 0])
# assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
#     1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"
#
# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
# res = cell.is_free
# cell.is_free = True
# assert bool(cell), "функция bool вернула False для свободной клетки"


# class Bag:
#     def __init__(self, max_weight):
#         self.max_weight = max_weight
#         self.thing_list = []
#
#     def add_thing(self, thing):
#         if thing.weight + self.count_weight() > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
#         self.thing_list.append(thing)
#
#     def count_weight(self):
#         return sum([thing.weight for thing in self.thing_list])
#
#     def __getitem__(self, item):
#         self.check_indx(item)
#         return self.thing_list[item]
#
#     def __setitem__(self, key, value):
#         self.check_indx(key)
#         if self.count_weight() - self.thing_list[key].weight + value.weight > self.max_weight:
#             raise ValueError('превышен суммарный вес предметов')
#         self.thing_list[key] = value
#
#     def __delitem__(self, key):
#         self.check_indx(key)
#         self.thing_list.pop(key)
#
#     def check_indx(self, indx):
#         if len(self.thing_list) - 1 < indx or indx < 0:
#             raise IndexError('неверный индекс')
#
#
# class Thing:
#     def __init__(self, name, weight):
#         self.name = name
#         self.weight = weight
#
#
# bag = Bag(1000)
# bag.add_thing(Thing('книга', 100))
# bag.add_thing(Thing('носки', 200))
# bag.add_thing(Thing('рубашка', 500))
# print(bag.count_weight())
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
# print(bag[2].name)  # рубашка
# bag[1] = Thing('платок', 1000)
# print(bag[1].name)  # платок
# del bag[0]
# print(bag[0].name)  # платок
# print([thing.weight for thing in bag.thing_list])
# t = bag[2]  # генерируется исключение IndexError

# непринятая задачка
# class SparseTable:
#     def __init__(self):
#         self.rows = 0
#         self.cols = 0
#         self.table = {}
#
#     def add_data(self, row, col, data):
#         self.table[(row, col)] = data
#         self.count_rows_cols()
#
#     def remove_data(self, row, col):
#         try:
#             del self.table[(row, col)]
#             self.count_rows_cols()
#         except KeyError:
#             raise IndexError('ячейка с указанными индексами не существует')
#
#     def count_rows_cols(self):
#         self.rows = max(row for row, col in self.table.keys()) + 1
#         self.cols = max(col for row, col in self.table.keys()) + 1
#
#     def __getitem__(self, item):
#         try:
#             return self.table[(item[0], item[1])].value
#         except KeyError:
#             raise ValueError('данные по указанным индексам отсутствуют')
#
#     def __setitem__(self, key, value):
#         print(key, "key")
#         self.table[(key[0], key[1])] = Cell(value)
#         self.count_rows_cols()
#
#
# class Cell:
#     def __init__(self, value):
#         self.value = value
#
#
# st = SparseTable()
# st.add_data(2, 5, Cell(25))
# st.add_data(1, 1, Cell(11))
# assert st.rows == 3 and st.cols == 6, "неверные значения атрибутов rows и cols"
#
# try:
#     v = st[3, 2]
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# st[3, 2] = 100
# assert st[3, 2] == 100, "неверно отработал оператор присваивания нового значения в ячейку таблицы"
# assert st.rows == 4 and st.cols == 6, "неверные значения атрибутов rows и cols"
#
# st.remove_data(1, 1)
# try:
#     v = st[1, 1]
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"


# class Person:
#     def __init__(self, fio, job, old, salary, year_job):
#         self.fio = fio
#         self.job = job
#         self.old = old
#         self.salary = salary
#         self.year_job = year_job
#         self.attr = ("fio", "job", "old", "salary", "year_job")
#
#     def __getitem__(self, item):
#         if item not in range(5):
#             raise IndexError('неверный индекс')
#         return self.__dict__[self.attr[item]]
#
#     def __setitem__(self, key, value):
#         if key not in range(5):
#             raise IndexError('неверный индекс')
#         self.__dict__[self.attr[key]] = value
#
#     def __iter__(self):
#         return iter(self.__dict__.values())
#
#
# pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
# print(pers[0])
# pers[0] = 'Балакирев С.М.'
# for v in pers:
#     print(v)
# pers[5] = 123 # IndexError


# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         for i in range(len(self.lst)):
#             for j in range(i+1):
#                 yield self.lst[i][j]
#
#
# class TriangleListIterator:
#     def __init__(self, lst):
#         self.lst = lst
#
#     def __iter__(self):
#         self.idx = [0, 0]
#         return self
#
#     def __next__(self):
#         r, c = self.idx
#         if r > len(self.lst) - 1:
#             raise StopIteration
#         self.idx = (r, c + 1) if c < r else (r + 1, 0)
#         return self.lst[r][c]
#
#
# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11'],
#        ['x20', 'x21', 'x22', 'x23', 'x24'],
#        ['x30', 'x31', 'x32', 'x33']]
# t = TriangleListIterator(lst)
# i = iter(t)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# class IterColumn:
#     def __init__(self, lst, column):
#         # self.lst = lst
#         # self.column = column
#         self.data = [item[column] for item in lst]
#
#     def __iter__(self):
#         # self.coords = (0, self.column)
#         return iter(self.data)
#
#     # def __next__(self):
#     #     r, c = self.coords
#     #     if r > len(self.lst) - 1:
#     #         raise StopIteration
#     #     self.coords = (r + 1, c)
#     #     return self.lst[r][c]
#
#
# lst = [['x00', 'x01', 'x02'],
#        ['x10', 'x11', 'x12'],
#        ['x20', 'x21', 'x22'],
#        ['x30', 'x31', 'x32']]
# it = IterColumn(lst, 1)
# for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
#     print(x)


# class StackObj:
#     def __init__(self, data):
#         self.__data = data
#         self.__next = None
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#     @property
#     def next(self):
#         return self.__next
#
#     @next.setter
#     def next(self, next):
#         if isinstance(next, StackObj) or next is None:
#             self.__next = next
#
#
# class Stack:
#     def __init__(self):
#         self.top = None
#         self.last = None
#
#     def push_back(self, obj):
#         if self.last:
#             self.last.next = obj
#         self.last = obj
#         if self.top is None:
#             self.top = obj
#
#     def push_front(self, obj):
#
#         if self.top and self.last:
#             obj.next = self.top
#             self.top = obj
#         else:
#             self.top = self.last = obj
#
#     def pop(self):
#         if self.top is None:
#             return
#         curr = self.top
#         while curr and curr.next != self.last:
#             curr = curr.next
#         if curr:
#             curr.next = None
#         last = self.last
#         self.last = curr
#         if self.last is None:
#             self.top = None
#         return last
#
#     def get_data(self):
#         data_lst = []
#         curr_obj = self.top
#         while curr_obj:
#             data_lst.append(curr_obj.data)
#             curr_obj = curr_obj.next
#         return data_lst
#
#     def __add__(self, other):
#         self.push(other)
#         return self
#
#     def __mul__(self, other):
#         for x in other:
#             self.push(StackObj(x))
#         return self
#
#     @staticmethod
#     def check_index(indx):
#         if not isinstance(indx, int):
#             raise IndexError('неверный индекс')
#     def get_obj_by_index(self, indx):
#     def __getitem__(self, item):
#         self.check_index(item)
#         if not self.top:
#             raise IndexError('неверный индекс')
#         curr_obj = self.top
#         for i in range(0, item + 1):
#             if i == item:
#                 return curr_obj.data
#             curr_obj = curr_obj.next
#             if not curr_obj:
#                 raise IndexError('неверный индекс')
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         if not self.top:
#             raise IndexError('неверный индекс')
#         curr_obj = self.top
#         for i in range(0, key + 1):
#             if i == key:
#                 curr_obj.data = value
#                 return
#             curr_obj = curr_obj.next
#             if not curr_obj:
#                 raise IndexError('неверный индекс')
#
#     def __iter__(self):
#         self.curr = self.top
#         return self
#
#     def __next__(self):
#         curr = self.curr
#         if not curr:
#             raise StopIteration
#         self.curr = self.curr.next
#         return curr
#
#
# st = Stack()
# st.push_back(StackObj("1"))
# st.push_front(StackObj("2"))
#
# assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"
#
# st[0] = "0"
# assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание " \
#                      "нового значения объекту стека "
#
# for obj in st:
#     assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"
#
# try:
#     a = st[3]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"


# class Cell:
#     def __init__(self, data=0):
#         self.data = data
#
#     @property
#     def data(self):
#         return self.__data
#
#     @data.setter
#     def data(self, data):
#         self.__data = data
#
#
# class TableValues:
#     def __init__(self, rows, cols, type_data=int):
#         self.rows = rows
#         self.cols = cols
#         self.type_data = type_data
#         self.table = tuple(tuple(Cell() for _ in range(cols)) for _ in range(rows))
#
#     def check_index(self, indx):
#         r, c = indx
#         if not 0 <= r < self.rows or not 0 <= c < self.cols:
#             raise IndexError('неверный индекс')
#
#     def __getitem__(self, item):
#         self.check_index(item)
#         return self.table[item[0]][item[1]].data
#
#     def __setitem__(self, key, value):
#         self.check_index(key)
#         if type(value) != self.type_data:
#             raise TypeError('неверный тип присваиваемых данных')
#         self.table[key[0]][key[1]].data = value
#
#     def __iter__(self):
#         for row in self.table:
#             yield (cell.data for cell in row)
#
#
# table = TableValues(2, 5)
# print(table[0, 0])
# table[0, 0] = 10
# print(table[0, 0])
#
# for row in table:  # перебор по строкам
#     for value in row:  # перебор по столбцам
#         print(value, end=' ')  # вывод значений ячеек в консоль
#     print()

# from operator import add, sub
#
#
# class Matrix:
#     def __init__(self, *args):
#         if len(args) == 3:
#             if not isinstance(args[0], int) or not isinstance(args[1], int) or not isinstance(args[2], (int, float)):
#                 raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
#             self.rows = args[0]
#             self.cols = args[1]
#             self.fill_value = args[2]
#             self.matrix = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
#         else:
#             if len(args) == 1 and isinstance(args[0], list):
#                 if not all([len(row) == len(args[0][0]) for row in args[0]]) or \
#                         not all([all([type(item) in (int, float) for item in row]) for row in args[0]]):
#                     raise TypeError('список должен быть прямоугольным, состоящим из чисел')
#             self.rows = len(args[0])
#             self.cols = len(args[0][0])
#             self.matrix = args[0]
#
#     def check_indx(self, indx):
#         if not 0 <= indx[0] < self.rows or not 0 <= indx[1] < self.cols:
#             raise IndexError('недопустимые значения индексов')
#
#     def __getitem__(self, item):
#         self.check_indx(item)
#         return self.matrix[item[0]][item[1]]
#
#     def __setitem__(self, key, value):
#         self.check_indx(key)
#         if not type(value) in (int, float):
#             raise TypeError('значения матрицы должны быть числами')
#         self.matrix[key[0]][key[1]] = value
#
#     def __make_calc(self, other, op):
#         if isinstance(other, Matrix):
#             if self.cols != other.cols or self.rows != other.rows:
#                 raise ValueError('операции возможны только с матрицами равных размеров')
#             return self.__class__(
#                 [[op(self.matrix[row][col], other.matrix[row][col]) for col in range(self.cols)] for row in
#                  range(self.rows)])
#         elif type(other) in (int, float):
#             return self.__class__(
#                 [[op(self.matrix[row][col], other) for col in range(self.cols)] for row in range(self.rows)])
#
#     def __add__(self, other):
#         return self.__make_calc(other, add)
#
#     def __sub__(self, other):
#         return self.__make_calc(other, sub)
#
#
# list2D = [[1, 2], [3, 4], [5, 6]]
# list2D2 = [[1, 2], [3, 4], [5, 6]]
# matrix = Matrix(list2D)
# matrix2 = Matrix(list2D2)
# print(matrix.matrix)
# matrix = matrix + matrix2
# print(matrix.matrix)
# print(matrix[1, 0])


#
# from random import choice
#
#
# class Cell:
#     def __init__(self):
#         self.value = 0
#
#     def __bool__(self):
#         return self.value == 0
#
#
# class TicTacToe:
#     FREE_CELL = 0  # свободная клетка
#     HUMAN_X = 1  # крестик (игрок - человек)
#     COMPUTER_O = 2  # нолик (игрок - компьютер)
#
#     def __init__(self):
#         self.pole = tuple(tuple(Cell() for _ in range(3)) for _ in range(3))
#         self.win_cond = (
#             ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 1), (2, 2)),
#             ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
#         self.__is_human_win = False
#         self.__is_computer_win = False
#         self.__is_draw = False
#
#     @property
#     def is_human_win(self):
#         return self.__is_human_win
#
#     @property
#     def is_computer_win(self):
#         return self.__is_computer_win
#
#     @property
#     def is_draw(self):
#         return self.__is_draw
#
#     def __bool__(self):
#         if self.is_computer_win or self.is_human_win or self.__is_draw:
#             return False
#         return True
#
#     def show(self):
#         for i in range(3):
#             print(str(self.pole[i][0].value) + " | " + str(self.pole[i][1].value) + " | " + str(self.pole[i][2].value))
#         print()
#
#     @staticmethod
#     def check_indx(indx):
#         if not 0 <= indx[0] <= 2 or not 0 <= indx[1] <= 2:
#             raise IndexError('некорректно указанные индексы')
#
#     def __getitem__(self, item):
#         self.check_indx(item)
#         return self.pole[item[0]][item[1]].value
#
#     def __setitem__(self, key, value):
#         self.check_indx(key)
#         self.pole[key[0]][key[1]].value = value
#         if any([all([self.pole[cell[0]][cell[1]].value == self.HUMAN_X for cell in row]) for row in self.win_cond]):
#             self.__is_human_win = True
#         elif any(
#                 [all([self.pole[cell[0]][cell[1]].value == self.COMPUTER_O for cell in row]) for row in self.win_cond]):
#             self.__is_computer_win = True
#
#         elif all([all([cell.value != self.FREE_CELL for cell in row]) for row in
#                   self.pole]) and not self.is_human_win and not self.__is_computer_win:
#             self.__is_draw = True
#
#     def init(self):
#         [[setattr(cell, "value", 0) for cell in row] for row in self.pole]
#         self.__is_human_win = False
#         self.__is_computer_win = False
#         self.__is_draw = False
#
#     def human_go(self):
#         h_move = input()
#         self.pole[int(h_move[1]) - 1][int(h_move[0]) - 1].value = 1
#
#     def computer_go(self):
#         choice([cell for row in self.pole for cell in row if cell]).value = 2
#
#
# # pole = TicTacToe()
# # pole.show()
# # pole.init()
# # pole.computer_go()
# # pole.show()
# game = TicTacToe()
# game.init()
#
# test = [[0, 0, 0],
#         [1, 1, 0],
#         [0, 0, 0]]
#
# for i in range(3):
#     for j in range(3):
#         print(i, j)
#         game[i, j] = test[i][j]
#
# game.show()
# print(game.is_human_win)
# print(game.is_computer_win)
# print(game.is_draw)
# if game.is_human_win:
#     print("Поздравляем! Вы победили!")
# elif game.is_computer_win:
#     print("Все получится, со временем")
# else:
#     print("Ничья.")


# class Animal:
#     def __init__(self, name, old):
#         self.name = name
#         self.old = old
#
#     def get_info(self):
#         print(self.name + ": " + ', '.join(map(str, list(self.__dict__.values())[1:])))
#
#
# class Cat(Animal):
#     def __init__(self, name, old, color, weight):
#         super().__init__(name, old)
#         self.color = color
#         self.weight = weight
#
#
# class Dog(Animal):
#     def __init__(self, name, old, breed, size):
#         super().__init__(name, old)
#         self.breed = breed
#         self.size = size
#
#
# d = Dog('пёс', 4, 'хаски', (2, 3))
# d.get_info()
# a = {"1": 1, "2": 2}
# print(*a.values())


# class Thing:
#     ID = -1
#
#     def __init__(self, *args):
#         self.id = self.get_id()
#         self.name, self.price, self.weight, self.dims, self.memory, self.frm = args
#
#     @staticmethod
#     def get_id():
#         Thing.ID += 1
#         return Thing.ID
#
#     def get_data(self):
#         return tuple(list(self.__dict__.values())[1:])
#
#
# class Table(Thing):
#     def __init__(self, name, price, weight, dims, memory=None, frm=None):
#         super().__init__(name, price, weight, dims, memory, frm)
#
#
# class ElBook(Thing):
#     def __init__(self, name, price, memory, frm, weight=None, dims=None):
#         super().__init__(name, price, weight, dims, memory, frm)
#
#
# table = Table("Круглый", 1024, 812.55, (700, 750, 700))
# book = ElBook("Python ООП", 2000, 2048, 'pdf')
# print(table.get_data())
# print(table.__dict__)
#
# print(book.get_data())


# class GenericView:
#     def __init__(self, methods=('GET',)):
#         self.methods = methods
#
#     def get(self, request):
#         return ""
#
#     def post(self, request):
#         pass
#
#     def put(self, request):
#         pass
#
#     def delete(self, request):
#         pass
#
#
# class DetailView(GenericView):
#     def render_request(self, request, method):
#         if not method in self.methods:
#             raise TypeError('данный запрос не может быть выполнен')
#         return self.__getattribute__(method.lower())(request)
#
#     def get(self, request):
#         if not isinstance(request, dict):
#             raise TypeError('request не является словарем')
#         if not request.get("url"):
#             raise TypeError('request не содержит обязательного ключа url')
#         return f"url: {request['url']}"
#
#
# dv = DetailView()
# html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')
# print(html)


# class Singleton:
#     __instance = None
#     __instance_base = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls == Singleton:
#             cls.__instance_base = object.__new__(cls)
#             return cls.__instance_base
#         if cls.__instance is None:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
#
# class Game(Singleton):
#     def __init__(self, name):
#         if "name" not in self.__dict__:
#             self.name = name
#
#
# class Game2(Singleton):
#     def __init__(self, name):
#         if "name" not in self.__dict__:
#             self.name = name
#
#
# game = Game("tictactoe")
# game2 = Game2("ig")
# game3 = Game("sjgr")
# print


# class Validator:
#     def __init__(self, min_value, max_value):
#         self.min_value = min_value
#         self.max_value = max_value
#
#     def _is_valid(self, data):
#         return isinstance(data, self.TYPE) and self.min_value <= data <= self.max_value
#
#     def __call__(self, data):
#         if not self._is_valid(data):
#             raise ValueError('данные не прошли валидацию')
#         return True
#
#
# class IntegerValidator(Validator):
#     TYPE = int
#
#
# class FloatValidator(Validator):
#     TYPE = float
#
# integer_validator = IntegerValidator(-10, 10)
# float_validator = FloatValidator(-1, 1)
# res1 = integer_validator(10)  # исключение не генерируется (проверка проходит)
# res2 = float_validator(10)    # исключение ValueError


# class Layer:
#     next_layer = None
#
#     def __init__(self):
#         self.name = "Layer"
#
#     def __call__(self, layer):
#         self.next_layer = layer
#         return layer
#
#
# class Input(Layer):
#     def __init__(self, inputs):
#         super().__init__()
#         self.inputs = inputs
#         self.name = "Input"
#
#
# class Dense(Layer):
#     def __init__(self, inputs, outputs, activation):
#         super().__init__()
#         self.name = "Dense"
#         self.inputs = inputs
#         self.outputs = outputs
#         self.activation = activation
#
#
# class NetworkIterator:
#     def __init__(self, start):
#         self.start = start
#
#     def __iter__(self):
#         self.obj = self.start
#         return self
#
#     def __next__(self):
#         if not self.obj:
#             raise StopIteration
#         curr, self.obj = self.obj, self.obj.next_layer
#         return curr
#
#
# network = Input(128)
# layer = network(Dense(network.inputs, 1024, 'linear'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))
# for x in NetworkIterator(network):
#     print(x.name)


# from operator import add, sub
#
#
# class Vector:
#     COORD_TYPES = (int, float)
#     ERROR_MESSAGE = "любыми числами"
#
#     def __init__(self, *args):
#         self._check_coords(args)
#         self.coord = args
#
#     def _calc(self, other, op):
#         if len(self.coord) != len(other.coord):
#             raise TypeError('размерности векторов не совпадают')
#         calc = [op(s, o) for s, o in zip(self.get_coords(), other.get_coords())]
#         return calc
#
#     def get_coords(self):
#         return self.coord
#
#     def _check_coords(self, coords):
#         if any(type(x) not in self.COORD_TYPES for x in coords):
#             raise ValueError('координаты должны быть ' + self.ERROR_MESSAGE)
#         return True
#
#     def __add__(self, other):
#         return Vector(*self._calc(other, add))
#
#     def __sub__(self, other):
#         return Vector(*self._calc(other, sub))
#
#
# class VectorInt(Vector):
#     COORD_TYPES = (int,)
#     ERROR_MESSAGE = "целыми числами"
#
#     def __add__(self, other):
#         try:
#             self._check_coords(other.get_coords())
#         except ValueError:
#             return super().__add__(other)
#         return self.__class__(*super()._calc(other, add))
#
#     def __sub__(self, other):
#         try:
#             self._check_coords(other.get_coords())
#         except ValueError:
#             return super().__sub__(other)
#         return self.__class__(*super()._calc(other, sub))
#
#
# v1 = VectorInt(1, 2, 3)
# v2 = Vector(3, 4, 5)
# v = v1 + v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
# v = v1 - v2  # формируется новый вектор (объект класса Vector) с соответствующими координатами
# print(v.get_coords())


# class ListInteger(list):
#     def __init__(self, lst):
#         for i in lst:
#             self._check_data(i)
#         super().__init__(lst)
#
#     @staticmethod
#     def _check_data(data):
#         if not isinstance(data, int):
#             raise TypeError('можно передавать только целочисленные значения')
#
#     def __setitem__(self, key, value):
#         self._check_data(value)
#         super().__setitem__(key, value)
#
#     def append(self, obj):
#         self._check_data(obj)
#         super().append(obj)
#
#
# s = ListInteger((1, 2, 3))
# s[1] = 10
# s.append(11)
# s[0] = 10.5  # TypeError


# class Thing:
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     def __hash__(self):
#         return hash((self.name, self.price, self.weight))
#
#
# class DictShop(dict):
#     def __init__(self, things=None):
#         things = {} if not things else things
#         if not isinstance(things, dict):
#             raise TypeError('аргумент должен быть словарем')
#         [self._check_keys(key) for key in things]
#         super().__init__(things)
#
#     def __setitem__(self, key, value):
#         self._check_keys(key)
#         super().__setitem__(key, value)
#
#     @staticmethod
#     def _check_keys(key):
#         if not isinstance(key, Thing):
#             raise TypeError('ключами могут быть только объекты класса Thing')
#
#
# th_1 = Thing('Лыжи', 11000, 1978.55)
# th_2 = Thing('Книга', 1500, 256)
# dict_things = DictShop()
# print(dict_things)
# dict_things[th_1] = th_1
# dict_things[th_2] = th_2
#
# for x in dict_things:
#     print(x.name)
#
# dict_things[1] = th_1  # исключение TypeError


# class Protists:
#     def __init__(self, name: object, weight: object, old: object) -> object:
#         self.name = name
#         self.weight = weight
#         self.old = old
#
#
# class Plants(Protists):
#     pass
#
#
# class Animals(Protists):
#     pass
#
#
# class Mosses(Plants):
#     pass
#
#
# class Flowering(Plants):
#     pass
#
#
# class Worms(Animals):
#     pass
#
#
# class Mammals(Animals):
#     pass
#
#
# class Human(Mammals):
#     pass
#
#
# class Monkeys(Mammals):
#     pass
#
#
# class Monkey(Monkeys):
#     pass
#
#
# class Person(Human):
#     pass
#
#
# class Flower(Flowering):
#     pass
#
#
# class Worm(Worms):
#     pass
#
#
# lst_objs = [Monkey("мартышка", 30.4, 7), Monkey("шимпанзе", 24.6, 8), Person("Балакирев", 88, 34),
#             Person("Верховный жрец", 67.5, 45), Flower("Тюльпан", 0.2, 1), Flower("Роза", 0.1, 2),
#             Worm("червь", 0.01, 1), Worm("червь 2", 0.02, 1)]
#
#
# lst_animals = [obj for obj in lst_objs if isinstance(obj, Animals)]
# lst_plants = [obj for obj in lst_objs if isinstance(obj, Plants)]
# lst_mammals = [obj for obj in lst_objs if isinstance(obj, Mammals)]


# class Tuple(tuple):
#     def __add__(self, other):
#         return Tuple(tuple(self)+tuple(other))
#
# t = Tuple([1, 2, 3])
# print(t)
# t = Tuple([1, 2, 3])
# t = t + "Python"
# print(t)   # (1, 2, 3, 'P', 'y', 't', 'h', 'o', 'n')
# t = (t + "Python") + "ООП"
# print(t)


# class VideoItem:
#     def __init__(self, title, descr, path):
#         self.title = title
#         self.descr = descr
#         self.path = path
#         self.rating = VideoRating()
#
#
# class VideoRating:
#     def __init__(self):
#         self.rating = 0
#
#     @property
#     def rating(self):
#         return self.__rating
#
#     @rating.setter
#     def rating(self, rating):
#         self._check_rating(rating)
#         self.__rating = rating
#
#     @staticmethod
#     def _check_rating(rating):
#         if not 0 <= rating <= 5:
#             raise ValueError('неверное присваиваемое значение')
#
# v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
# print(v.rating.rating) # 0
# v.rating.rating = 5
# print(v.rating.rating) # 5
# title = v.title
# descr = v.descr
# v.rating.rating = 6  # ValueError


# class IteratorAttrs:
#     def __iter__(self):
#         return iter(self.__dict__.items())
#
#
# class SmartPhone(IteratorAttrs):
#     def __init__(self, model, size, memory):
#         self.model = model
#         self.size = size
#         self.memory = memory
#
#
# phone = SmartPhone(1,2,3)
# for attr, value in phone:
#     print(attr, value)


# class Book:
#     def __init__(self, title, author, pages, year):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#
# class DigitBook(Book):
#     def __init__(self, title, author, pages, year, size, frm):
#         super().__init__(title, author, pages, year)
#         self.size = size
#         self.frm = frm


# class SellItem:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# class House(SellItem):
#     def __init__(self, name, price, material, square):
#         super().__init__(name, price)
#         self.material = material
#         self.square = square
#
#
# class Flat(SellItem):
#     def __init__(self, name, price, size, rooms):
#         super().__init__(name, price)
#         self.size = size
#         self.rooms = rooms
#
#
# class Land(SellItem):
#     def __init__(self, name, price, square):
#         super().__init__(name, price)
#         self.square = square
#
#
# class Agency:
#     def __init__(self, name):
#         self.name = name
#         self.objects = []
#
#     def add_obj(self, obj):
#         if isinstance(obj, (House, Flat, Land)):
#             self.objects.append(obj)
#
#     def remove_obj(self, obj):
#         self.objects.remove(obj)
#
#     def get_objects(self):
#         return self.objects


# class Router:
#     app = {}
#
#     @classmethod
#     def get(cls, path):
#         return cls.app.get(path)
#
#     @classmethod
#     def add_callback(cls, path, func):
#         cls.app[path] = func
#
#
# class Callback:
#     def __init__(self, path, router):
#         self.path = path
#         self.router = router
#
#     def __call__(self, func):
#         self.router.add_callback(self.path, func)
#
#
# @Callback('/', Router)
# def index():
#     return '<h1>Главная</h1>'
#
#
# route = Router.get('/')
# if route:
#     ret = route()
#     print(ret)


# def integer_params(cls):
#     methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
#     for k, v in methods.items():
#         setattr(cls, k, integer_params_decorated(v))
#
#     return cls
#
#
# def integer_params_decorated(func):
#     def wrapper(self, *args, **kwargs):
#         if not all(isinstance(item, int) for item in args) or kwargs:
#             raise TypeError("аргументы должны быть целыми числами")
#         return func(self, *args, **kwargs)
#
#     return wrapper
#
#
# @integer_params
# class Vector:
#     def __init__(self, *args):
#         self.__coords = list(args)
#
#     def __getitem__(self, item):
#         return self.__coords[item]
#
#     def __setitem__(self, key, value):
#         self.__coords[key] = value
#
#     def set_coords(self, *coords, reverse=False):
#         c = list(coords)
#         self.__coords = c if not reverse else c[::-1]
#
#
# vector = Vector(1, 2)
# # print(vector[1])
# # vector[1] = 20.4  # TypeError
# vector.set_coords(1, 2, reverse=True)


# class SoftList(list):
#     def __getitem__(self, item):
#         if -len(self) <= item < len(self):
#             return super().__getitem__(item)
#         return False


# class StringDigit(str):
#     def __init__(self, string):
#         if not string.isdigit():
#             raise ValueError("в строке должны быть только цифры")
#         super().__init__()
#
#     def __add__(self, other):
#         return StringDigit(str(self) + other)
#
#     def __radd__(self, other):
#         return StringDigit(other + str(self))
#
#
# sd = StringDigit("123")
# sd = sd + "456"  # StringDigit: 123456
# sd = "789" + sd  # StringDigit: 789123456
# sd = sd + "12f"  # ValueError


# class ItemAttrs(list):
#     pass
#
#
# class Point(ItemAttrs):
#     def __init__(self, x, y):
#         super().__init__([x, y])
#
#
# pt = Point(1, 2.5)
# x = pt[0]  # 1
# y = pt[1]  # 2.5
# pt[0] = 10


# class Animal:
#     def __init__(self, name, kind, old):
#         self.name = name
#         self.kind = kind
#         self.old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def kind(self):
#         return self.__kind
#
#     @kind.setter
#     def kind(self, value):
#         self.__kind = value
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, value):
#         self.__old = value
#
#
# animals = [Animal('Васька', 'дворовый кот', 5), Animal('Рекс', 'немецкая овчарка', 8), Animal('Кеша', 'попугай', 3)]


# class Furniture:
#     attrs = ("_name", "_weight")
#
#     def __init__(self, *args):
#         [setattr(self, name, arg) for name, arg in zip(self.attrs, args)]
#
#     @staticmethod
#     def __verify_name(name):
#         if not isinstance(name, str):
#             raise TypeError('название должно быть строкой')
#
#     @staticmethod
#     def __verify_weight(weight):
#         if not isinstance(weight, int) or weight <= 0:
#             raise TypeError('вес должен быть положительным числом')
#
#     def __setattr__(self, key, value):
#         if key == "_name":
#             self.__verify_name(value)
#         if key == "_weight":
#             self.__verify_weight(value)
#         super().__setattr__(key, value)
#
#     def get_attrs(self):
#         return tuple(self.__dict__[name] for name in self.attrs)
#
#
# class Closet(Furniture):
#     attrs = ("_name", "_weight", "_tp", "_doors")
#
#
# class Chair(Furniture):
#     attr = ("_name", "_weight", "_height")
#
#
# class Table(Furniture):
#     attrs = ("_name", "_weight", "_height", "_square")
#
#
# fr = Table("jsydf", 10, 57, 37)
# print(fr.get_attrs())
# f = Furniture("ksjdgv", 10)


class Observer:
    def update(self, data):
        pass

    def __hash__(self):
        return hash(id(self))


class Subject:
    def __init__(self):
        self.__observers = {}
        self.__data = None

    def add_observer(self, observer):
        self.__observers[observer] = observer

    def remove_observer(self, observer):
        if observer in self.__observers:
            self.__observers.pop(observer)

    def __notify_observer(self):
        for ob in self.__observers:
            ob.update(self.__data)

    def change_data(self, data):
        self.__data = data
        self.__notify_observer()


class Data:
    def __init__(self, temp, press, wet):
        self.temp = temp  # температура
        self.press = press  # давление
        self.wet = wet  # влажность


class TemperatureView(Observer):
    pass


class PressureView(Observer):
    pass


class WetView(Observer):
    pass


subject = Subject()
tv = TemperatureView()
pr = PressureView()
wet = WetView()

subject.add_observer(tv)
subject.add_observer(pr)
subject.add_observer(wet)

# subject.change_data(Data(23, 150, 83))
# # выведет строчки:
# # Текущая температура 23
# # Текущее давление 150
# # Текущая влажность 83
# subject.remove_observer(wet)
# subject.change_data(Data(24, 148, 80))
# # выведет строчки:
# # Текущая температура 24
# # Текущее давление 148
