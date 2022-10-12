# class SuperShop:
#
#
#     def __init__(self, name, goods: list = []):
#         self.name = name
#         self.goods = goods
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class StringValue:
#     def __init__(self, min_len, max_len):
#         self.min_len = min_len
#         self.max_len = max_len
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value, str) and self.min_len <= len(value) <= self.max_len:
#             setattr(instance, self.name, value)
#
#
# class PriceValue:
#     def __init__(self, max_value):
#         self.max_value = max_value
#
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if isinstance(value, (int, float)) and 0 <= value <= self.max_value:
#             setattr(instance, self.name, value)
#
#
# class Product:
#     name = StringValue(min_len=2, max_len=50)
#     price = PriceValue(max_value=10000)
#
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#
# shop = SuperShop("У Балакирева")
# shop.add_product(Product("Курс по Python", 0))
# shop.add_product(Product("Курс по Python ООП", 2000))
# for p in shop.goods:
#     print(f"{p.name}: {p.price}")
#
# class Bag:
#     def __init__(self, max_weigth):
#         self.max_weigth = max_weigth
#         self.__things = []
#
#     @property
#     def things(self):
#         return self.__things
#
#     def add_thing(self, thing):
#         if self.get_total_weight()+thing.weight<=self.max_weigth:
#             self.things.append(thing)
#
#     def remove_thing(self, indx):
#         if indx in len(self.__things):
#             self.__things.pop(indx)
#
#     def get_total_weight(self):
#         return sum([x.weight for x in self.things])
#
#
# class Thing:
#     def __init__(self, name: str, weight):
#         if isinstance(name, str):
#             self.name = name
#         if isinstance(weight, (int, float)):
#             self.weight = weight
#
#
# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# w = bag.get_total_weight()
# print(w)
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")
#
#
# class TVProgram:
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_telecast(self, tl):
#         self.items.append(tl)
#
#     def remove_telecast(self, indx):
#         self.items = [x for x in self.items if x.uid != indx]
#
#
# class Telecast:
#     def __init__(self, id, name, duration):
#         self.__id = id
#         self.__name = name
#         self.__duration = duration
#
#     @property
#     def uid(self):
#         return self.__id
#
#     @uid.setter
#     def uid(self, id):
#         self.__id = id
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def duration(self):
#         return self.__duration
#
#     @duration.setter
#     def duration(self, duration):
#         self.__duration = duration
#
#
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(2, "Новости", 2000))
# pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
# pr.remove_telecast(2)
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")
#
# class Book:
#     title: str
#     author: str
#     pages: int
#     year: int
#
#     def __init__(self, title="", author="", pages=0, year=0):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     def __setattr__(self, key, value):
#         if not isinstance(value, self.__annotations__.get(key, object)):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         object.__setattr__(self, key, value)
#
#
# book = Book("Python ООП", "Сергей Балакирев", 123, 2022)
# print(book.__dict__)
# from typing import Union
#
#
# class Shop:
#     def __init__(self, name):
#         self.name = name
#         self.goods = []
#
#     def add_product(self, product):
#         self.goods.append(product)
#
#     def remove_product(self, product):
#         self.goods.remove(product)
#
#
# class Product:
#     count = 0
#
#     def __init__(self, name: str, weight: int | float, price: int | float):
#         self.id = self.id_increase()
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     @classmethod
#     def id_increase(cls):
#         cls.count += 1
#         return cls.count
#
#     def __setattr__(self, key, value):
#         if (key == "name" and type(value) is not str) or (
#                 key in ("weight", "price") and type(value) not in (int, float)) or (
#                 key in ("weight", "price") and value < 0):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item == "id":
#             raise AttributeError("Атрибут id удалять запрещено.")
#         object.__delattr__(self, item)
#
#
# shop = Shop("Балакирев и К")
# book = Product("Python ООП", 100, 1024)
# shop.add_product(book)
# shop.add_product(Product("Python", 150, 512))
# for p in shop.goods:
#     print(f"{p.name}, {p.weight}, {p.price}")
#
#
# class Course:
#     def __init__(self, name):
#         self.name = name
#         self.modules = []
#
#     def add_module(self, module):
#         self.modules.append(module)
#
#     def remove_module(self, indx):
#         if indx < len(self.modules):
#             self.modules.pop(indx)
#
#
# class Module:
#     def __init__(self, name):
#         self.name = name
#         self.lessons = []
#
#     def add_lesson(self, lesson):
#         self.lessons.append(lesson)
#
#     def remove_lesson(self, indx):
#         if indx < len(self.lessons):
#             self.lessons.pop(indx)
#
#
# class LessonItem:
#     def __init__(self, title: (str,), practices: (int, float) , duration: (int,)):
#         self.title = title
#         self.practices = practices
#         self.duration = duration
#
#     def __setattr__(self, key, value):
#         if type(value) in self.__init__.__annotations__[key]:
#             object.__setattr__(self, key, value)
#         else:
#             raise TypeError("Неверный тип присваиваемых данных.")
#
#     def __getattr__(self, item):
#         return False
#
#     def __delattr__(self, item):
#         if item in ("title", "practices", "duration"):
#             return False
#         object.__delattr__(self, item)
#
#
# lesson = LessonItem("Урок 1", 7, 1000)
# print(lesson.__dict__)
# print(lesson.__init__.__annotations__)
#
#
# class Museum:
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, obj):
#         self.exhibits.append(obj)
#
#     def remove_exhibit(self, obj):
#         self.exhibits.remove(obj)
#
#     def get_info_exhibit(self, indx):
#         return f"Описание экспоната {self.exhibits[indx].name}: {self.exhibits[indx].descr}"
#
#
# class Exhibitions:
#     def __init__(self, name, variable, descr):
#         self.name = name
#         self.variable = variable
#         self.descr = descr
#
#     def __setattr__(self, key, value):
#         if key == "variable":
#             key = self.variable_attr
#         object.__setattr__(self, key, value)
#
#
# class Picture(Exhibitions):
#     variable_attr = "author"
#     pass
#
#
# class Mummies(Exhibitions):
#     variable_attr = "name"
#     pass
#
#
# class Papyri(Exhibitions):
#     variable_attr = "date"
#     pass
#
#
# class SmartPhone:
#     def __init__(self, model):
#         self.model = model
#         self.apps = []
#
#     def add_app(self, app):
#         if app.__class__ not in (i.__class__ for i in self.apps):
#             self.apps.append(app)
#
#     def remove_app(self, app):
#         self.apps.remove(app)
#
#
# class AppVK:
#     def __init__(self):
#         self.name = "ВКонтакте"
#
#
# class AppYouTube:
#     def __init__(self, memory_max):
#         self.name = "YouTube"
#         self.memory_max = memory_max
# class AppPhone:
#     def __init__(self, phone_list):
#         self.name = "Phone"
#         self.phone_list = phone_list
#
#
# sm = SmartPhone("Honor 1.0")
# sm.add_app(AppVK())
# sm.add_app(AppVK())  # второй раз добавляться не должно
# sm.add_app(AppYouTube(2048))
# for a in sm.apps:
#     print(a.name)
#
#
# class Circle:
#     def __init__(self, x, y, radius):
#         self.__x = x
#         self.__y = y
#         self.__radius = radius
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         self.__x = x
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, y):
#         self.__y = y
#
#     @property
#     def radius(self):
#         return self.__radius
#
#     @radius.setter
#     def radius(self, radius):
#         self.__radius = radius
#
#     def __setattr__(self, key, value):
#         if not isinstance(value, (int, float)):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == "_Circle__radius" and value <= 0:
#             return
#         super().__setattr__(key, value)
#
#     def __getattr__(self, item):
#         return False
#
# circle = Circle(10.5, 7, -22)
# circle.radius = 10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
# x, y = circle.x, circle.y
# res = circle.name  # False, т.к. атрибут name не существует
# print(circle.__dict__)
#
#
# class SomeDescriptor:
#     def __set_name__(self, owner, name):
#         self.name = "__" + name
#
#     def __get__(self, instance, owner):
#         if instance:
#             return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         setattr(instance, self.name, value)
#
#
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 1000
#
#     def __init__(self, a, b, c):
#         self.__a = a
#         self.__b = b
#         self.__c = c
#
#     @classmethod
#     def validate(cls, value):
#         return cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION
#
#     def __setattr__(self, key, value):
#         if key in ("MAX_DIMENSION", "MIN_DIMENSION"):
#             raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
#         super().__setattr__(key, value)
#
#
# d = Dimensions(10.5, 20.1, 30)
# d.a = 8
# d.b = 15
# d.c = 30
# a, b, c = d.a, d.b, d.c  # a=10.5, b=15, c=30
# print(d.__dict__)
# d.MAX_DIMENSION = 10  # исключение AttributeError
#
#
# import time
#
#
# class GeyserClassic:
#     MAX_DATE_FILTER = 100
#     FILTER_SLOTS = {"Mechanical": 1, "Aragon": 2, "Calcium": 3}
#     FILTER_LIST = [None, None, None]
#
#     def add_filter(self, slot_num, filter):
#         if isinstance(filter, (Mechanical, Aragon, Calcium)) and \
#                 self.FILTER_SLOTS[filter.__class__.__name__] == slot_num:
#             self.FILTER_LIST[slot_num - 1] = filter
#
#     def remove_filter(self, slot_num):
#         self.FILTER_LIST[slot_num - 1] = None
#
#     def get_filters(self):
#         return tuple(*[self.FILTER_LIST])
#
#     def water_on(self):
#         return all(self.FILTER_LIST) and \
#                all([0 <= time.time() - filt.date <= self.MAX_DATE_FILTER for filt in self.FILTER_LIST])
#
#
# class Filter:
#     def __init__(self, date):
#         self.date = date
#
#     def __setattr__(self, key, value):
#         if key == 'date' and key in self.__dict__:
#             return
#         super().__setattr__(key, value)
#
#
# class Mechanical(Filter):
#     pass
#
#
# class Aragon(Filter):
#     pass
#
#
# class Calcium(Filter):
#     pass
#
#
# my_water = GeyserClassic()
# my_water.add_filter(1, Mechanical(time.time()))
# my_water.add_filter(2, Aragon(time.time()))
# print(my_water.get_filters())
# w = my_water.water_on()  # False
# my_water.add_filter(3, Calcium(time.time()))
# w = my_water.water_on()  # True
# f1, f2, f3 = my_water.get_filters()  # f1, f2, f3 - ссылки на соответствующие объекты классов фильтров
# my_water.add_filter(3, Calcium(time.time()))  # повторное добавление в занятый слот невозможно
# my_water.add_filter(2, Calcium(time.time()))  # добавление в "чужой" слот также невозможно
# print()
# from random import choices, randint
#
#
# class RandomPassword:
#     def __init__(self, psw_chars, min_length, max_length):
#         self.psw_chars = psw_chars
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, *args, **kwargs):
#         return "".join(choices(self.psw_chars, k=randint(self.min_length, self.max_length)))
#
#
# min_length = 5
# max_length = 20
# psw_chars = "qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*"
# rnd = RandomPassword(psw_chars, min_length, max_length)
# lst_pass = [rnd() for i in range(3)]
# print(lst_pass)
#
#
# class ImageFileAcceptor:
#     def __init__(self, extensions: tuple):
#         self.extensions = extensions
#
#     def __call__(self, file_name):
#         return file_name.split(".")[-1] in self.extensions
#
#
# class LengthValidator:
#     def __init__(self, min_length, max_length):
#         self.min_length = min_length
#         self.max_length = max_length
#
#     def __call__(self, string):
#         return self.min_length <= len(string) <= self.max_length
#
#
# class CharsValidator:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         return all([c in self.chars for c in string])
#
#
# class DigitRetrieve:
#     def __call__(self, string):
#         try:
#             int(string)
#         except ValueError:
#             return None
#         else:
#             return int(string)
#
#
# dg = DigitRetrieve()
# st = ["123", "abc", "-56.4", "0", "-5"]
# digits = list(map(dg, st))  # [123, None, None, 0, -5]
# print(digits)
#
#
# class RenderList:
#     def __init__(self, type_list):
#         self.type_list = "ol" if type_list == "ol" else "ul"
#
#     def __call__(self, lst):
#         return f"<{self.type_list}>\n<li>{lst[0]}</li>\n<li>{lst[1]}</li>\n<li>{lst[2]}</li>\n</{self.type_list}>"
#
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst)
# print(html)
#
#
# class HandlerGET:
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self, request):
#         if request.get("method", "GET") == "GET":
#             return self.get(self.fn, request)
#         return None
#
#     def get(self, func, request):
#         return f"GET: {func(request)}"
#
#
# class Handler:
#     def __init__(self, methods=("GET",)):
#         self.methods = methods
#
#     def __call__(self, func):
#         def wrapper(request):
#             if request.get("method", "GET") in self.methods:
#                 method = request.get("method", "GET")
#                 return self.__getattribute__(method.lower())(func, request)
#
#         return wrapper
#
#     def get(self, func, request):
#         return f"GET: {func(request)}"
#
#     def post(self, func, request):
#         return f"POST: {func(request)}"
#
#
# @Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
# def contact(request):
#     return "Сергей Балакирев"
#
#
# res = contact({"method": "PUT", "url": "contact.html"})
# print(res)
#
#
# class InputDigits:
#     def __init__(self, func):
#         self.fn = func
#
#     def __call__(self):
#         return [*map(int, self.fn().split())]
#
#
# input_dg = InputDigits(input)
# res = input_dg()
# print(res)
#
#
# class RenderDigit:
#     def __call__(self, string):
#         try:
#             return int(string)
#         except:
#             return None
#
#
# class InputValues:
#     def __init__(self, render=RenderDigit):
#         self.render = render
#
#     def __call__(self, func):
#         def wrapper(*args):
#             return list(map(self.render, func(*args).split()))
#
#         return wrapper
#
# render = RenderDigit()
# input_dg = InputValues(render)(input)
# res = input_dg()
# print(res)
#
#
# class RenderList:
#     def __init__(self, type_lst):
#         self.type_lst = type_lst
#
#     def __call__(self, lst):
#         l_type = "ol" if self.type_lst == "ol" else "ul"
#         return f"<{l_type}>\n" + "\n".join([f"<li>{x}</li>" for x in lst]) + f"\n<{l_type}>"
#
#
# lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
# render = RenderList("ol")
# html = render(lst)
# print(html)
#
#
# class HandlerGET:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, request):
#         return self.get(self.func, request) if request.get("method", "GET") == "GET" else None
#
#     def get(self, func, request):
#         return f"GET:{func(request)}"
#
#
# @HandlerGET
# def contact(request):
#     return "Сергей Балакирев"
#
#
# res = contact({"method": "GET", "url": "contact.html"})
# print(res)
#
#
# class Handler:
#     def __init__(self, methods="GET"):
#         self.methods = methods
#
#     def __call__(self, func):
#         def wrapper(request):
#             m = request.get("method")
#             return self.__getattribute__(m.lower())(func, request) if m in self.methods else None
#         return wrapper
#
#     def get(self, func, request):
#         return f"GET{func(request)}"
#
#     def post(self, func, request):
#         return f"POST:{func(request)}"
#
#
# @Handler(methods=('GET', 'POST'))  # по умолчанию methods = ('GET',)
# def contact(request):
#     return "Сергей Балакирев"
#
#
# res = contact({"method": "POST", "url": "contact.html"})
# print(res)
#
#
# class InputDigits:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         return [*map(int, self.func().split())]
#
#
# input_dg = InputDigits(input)
# res = input_dg()
# print(res)
#
#
# class RenderDigit:
#     def __call__(self, str):
#         try:
#             return int(str)
#         except:
#             return None
#
#
# class InputValues:
#     def __init__(self, render):
#         self.render = render
#
#     def __call__(self, func):
#         def wrapper():
#             return [*map(self.render, func().split())]
#
#         return wrapper
#
#
# render = RenderDigit()
# input_dg = InputValues(render)(input)
# res = input_dg()
# print(res)
#
# class Book:
#     def __init__(self, title, author, pages):
#         self.author = author
#         self.title = title
#         self.pages = pages
#
#     def __str__(self):
#         return f"Книга: {self.title}; {self.author}; {self.pages}"
#
#
# class Model:
#     def query(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __str__(self):
#         return "Model: " + ", ".join(f"{key} = {item}" for key, item in self.__dict__.items()) \
#             if self.__dict__ else "Model"
#
#
# model = Model()
# # model.query(field_1=1, field_2=2, field_N=3)
# print(model)
#
#
# class WordString:
#     def __init__(self, *args):
#         if args:
#             self.__string = args[0]
#
#     @property
#     def string(self):
#         return self.__string
#
#     @string.setter
#     def string(self, string):
#         self.__string = string
#
#     def __len__(self):
#         return len(self.__string.split())
#
#     def words(self, indx):
#         return self.__string.split()[indx]
#
#     def __call__(self, indx):
#         return self.string.split()[indx]
#
#
# words = WordString()
# words.string = "Курс по Python ООП"
# n = len(words)
# first = "" if n == 0 else words(0)
# print(words.string)
# print(f"Число слов: {n}; первое слово: {first}")
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = self.tail = None
#
#     def add_obj(self, obj):
#         if self.head:
#             if self.tail:
#                 self.tail.next = obj
#                 obj.prev = self.tail
#                 self.tail = obj
#             else:
#                 self.head.next = self.tail = obj
#                 obj.prev = self.head
#         else:
#             self.head = obj
#
#     def get_obj_by_indx(self, indx):
#         obj = self.head
#         count = 0
#         while obj and count < indx:
#             obj = obj.next
#             count += 1
#         return obj
#
#     def remove_obj(self, indx):
#         obj = self.get_obj_by_indx(indx)
#         if obj is None:
#             return
#         if indx + 1 < self.__len__() and indx > 0:
#             p, n = obj.prev, obj.next
#             p.next = n
#             n.prev = p
#         elif indx == 0:
#             if self.__len__()==1:
#                 self.head = self.tail = None
#             else:
#                 n = obj.next
#                 n.prev = None
#                 self.head = n
#         elif indx + 1 == self.__len__():
#             p = obj.prev
#             p.next = None
#             self.tail = p
#
#     def __call__(self, indx):
#         return self.get_obj_by_indx(indx).data
#
#     def __len__(self):
#         if self.head:
#             curr_obj = self.head
#             count = 0
#             while curr_obj:
#                 curr_obj = curr_obj.next
#                 count += 1
#             return count
#         return 0
#
#
# class ObjListDesc:
#     def __set_name__(self, owner, name):
#         self.name = f"_{owner.__name__}__{name}"
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.name] = value
#
#
# class ObjList:
#     # data = ObjListDesc()
#     # prev = ObjListDesc()
#     # next = ObjListDesc()
#
#     def __init__(self, data):
#         self.data = data
#         self.prev = self.next = None
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
#         self.__next = next
#
#     @property
#     def prev(self):
#         return self.__prev
#
#     @prev.setter
#     def prev(self, prev):
#         self.__prev = prev
#
# linked_lst = LinkedList()
# linked_lst.add_obj(ObjList("Sergey"))
# linked_lst.add_obj(ObjList("Balakirev"))
# linked_lst.add_obj(ObjList("Python"))
# linked_lst.remove_obj(0)
# linked_lst.add_obj(ObjList("Python ООП"))
# n = len(linked_lst)  # n = 3
# s = linked_lst(1)  # s = Balakirev
# print(n, s)
#
# def validator(func):
#     types = (int, float)
#
#     def wrapper(self, value):
#         if type(value) not in types:
#             raise ValueError("Неверный тип данных.")
#         func(self, value)
#     return wrapper
#
#
# class Complex:
#     def __init__(self, real, img):
#         self.real = real
#         self.img = img
#
#     @property
#     def real(self):
#         return self.__real
#
#     @real.setter
#     @validator
#     def real(self, real):
#         self.__real = real
#
#     @property
#     def img(self):
#         return self.__img
#
#     @img.setter
#     @validator
#     def img(self, img):
#         self.__img = img
#
#     def __abs__(self):
#         return (self.real ** 2 + self.img ** 2) ** 0.5
#
#     # def __setattr__(self, key, value):
#     #     if not isinstance(value, (int, float)):
#     #         raise ValueError("Неверный тип данных.")
#     #     object.__setattr__(self, key, value)
#
#
# cmp = Complex(7, 8)
# cmp.real = 3
# cmp.img = 4
# c_abs = abs(cmp)
#
# class RadiusVector:
#     def __init__(self, *args):
#         self.coords = [0] * args[0] if len(args) == 1 else [*args]
#
#     def set_coords(self, *args):
#         self.coords = list(args[:len(self.coords)]) + self.coords[len(args):]
#
#     def get_coords(self):
#         return tuple(self.coords)
#
#     def __len__(self):
#         return len(self.coords)
#
#     def __abs__(self):
#         return sum(x ** 2 for x in self.coords) ** 0.5
#
#
#
# r = RadiusVector(5)
# print(r.__dict__)
# r.set_coords(1, 2, 3, 4, 5, 6, 7, 8)
# print(r.get_coords())
#
# import time
#
#
# class DeltaClock:
#     def __init__(self, clock1, clock2):
#         self.c1 = clock1
#         self.c2 = clock2
#
#     def __str__(self):
#         return time.strftime("%H: %M: %S", time.gmtime(len(self))) if len(self) > 0 else "00: 00: 00"
#
#     def __len__(self):
#         return self.c1.get_time() - self.c2.get_time()
#
#
# class Clock:
#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#
#     def __setattr__(self, key, value):
#         if isinstance(value, int) and value >= 0:
#             object.__setattr__(self, key, value)
#
#     def get_time(self):
#         return self.hours * 3600 + self.minutes * 60 + self.seconds
#
# dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
# print(dt) # 01: 30: 00
# len_dt = len(dt) # 5400
# print(len_dt)
#
#
# class Recipe:
#     def __init__(self, *args):
#         self.ing = [*args]
#
#     def add_ingredient(self, ing):
#         self.ing.append(ing)
#
#     def remove_ingredient(self, ing):
#         self.ing.remove(ing)
#
#     def get_ingredients(self):
#         return tuple(self.ing)
#
#     def __len__(self):
#         return len(self.ing)
#
#
# class Ingredient:
#     def __init__(self, name: str, volume: float, measure: str):
#         self.name = name
#         self.volume = float(volume)
#         self.measure = measure
#
#     def __setattr__(self, key, value):
#         if isinstance(value, self.__init__.__annotations__[key]):
#             object.__setattr__(self, key, value)
#
#     def __str__(self):
#         return f"{self.name}: {int(self.volume)}, {self.measure}"
#
#
# recipe = Recipe()
# recipe.add_ingredient(Ingredient("Соль", 1, "столовая ложка"))
# recipe.add_ingredient(Ingredient("Мука", 1, "кг"))
# recipe.add_ingredient(Ingredient("Мясо баранины", 10, "кг"))
# ings = recipe.get_ingredients()
# n = len(recipe)  # n = 3
# print(Ingredient("Соль", 1, "столовая ложка").__dict__)
# i4 = Ingredient("Масло", 100, "гр")
# print(str(i4))
#
#
# class PolyLine:
#     def __init__(self, *args):
#         self.coords = [*args]
#
#     def add_coord(self, x, y):
#         self.coords.append((x, y))
#
#     def remove_coord(self, indx):
#         self.coords.pop(indx)
#
#     def get_coords(self):
#         return self.coords
#
#
# poly = PolyLine((1, 2), (3, 5), (0, 10), (-1, 8))
#
#
# class NewList:
#     def __init__(self, lst=None):
#         self.lst = lst[:] if lst and type(lst) == list else []
#
#     def __sub__(self, other):
#         temp_other = other.get_list() if type(other) == NewList else other
#         temp_other = [(x, type(x)) for x in temp_other]
#         temp_lst = [(x, type(x)) for x in self.get_list()]
#         for i in temp_other:
#             if i in temp_lst:
#                 temp_lst.remove(i)
#         return NewList([x[0] for x in temp_lst])
#
#     def __rsub__(self, other):
#         return NewList(other) - self
#
#     def get_list(self):
#         return self.lst
#
#
# lst = NewList()
# lst1 = NewList([0, 1, -3.4, "abc", True])
# lst2 = NewList([1, 0, True])
#
# assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"
#
# res1 = lst1 - lst2
# print(lst1.get_list())
# res2 = lst1 - [0, True]
# print(res2.get_list())
# res3 = [1, 2, 3, 4.5] - lst2
# lst1 -= lst2
#
# assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
# assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
# assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
# assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
#
# lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
# lst_2 = NewList([10, True, False, True, 1, 7.87])
# res = lst_1 - lst_2
# print(res.get_list())
# assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"
#
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a  # NewList: [1, 2]
# assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
#
#
# class ListMath:
#     def __init__(self, lst=None):
#         self.lst_math = [x for x in lst if type(x) in (int, float)] if lst else []
#
#     def __add__(self, other):
#         return ListMath([x + other for x in self.lst_math])
#
#     def __radd__(self, other):
#         return ListMath(self.lst_math) + other
#
#     def __iadd__(self, other):
#         for i, _ in enumerate(self.lst_math):
#             self.lst_math[i] = self.lst_math[i] + other
#         return self
#
#     def __sub__(self, other):
#         return ListMath([x - other for x in self.lst_math])
#
#     def __rsub__(self, other):
#         return ListMath([other - x for x in self.lst_math])
#
#     def __isub__(self, other):
#         for i, _ in enumerate(self.lst_math):
#             self.lst_math[i] = self.lst_math[i] - other
#         return self
#
#     def __mul__(self, other):
#         return ListMath([x * other for x in self.lst_math])
#
#     def __rmul__(self, other):
#         return ListMath(self.lst_math) * other
#
#     def __imul__(self, other):
#         for i, _ in enumerate(self.lst_math):
#             self.lst_math[i] = self.lst_math[i] * other
#         return self
#
#     def __truediv__(self, other):
#         return ListMath([x / other for x in self.lst_math])
#
#     def __rtruediv__(self, other):
#         return ListMath([other / x for x in self.lst_math])
#
#     def __itruediv__(self, other):
#         for i, _ in enumerate(self.lst_math):
#             self.lst_math[i] = self.lst_math[i] / other
#         return self
#
#
# lst1 = ListMath()
# lp = [1, False, 2, -5, "abc", 7]
# lst2 = ListMath(lp)
# lst3 = ListMath(lp)
#
# assert id(lst2.lst_math) != id(lst3.lst_math), "внутри объектов класса ListMath должна создаваться копия списка"
#
# assert lst1.lst_math == [] and lst2.lst_math == [1, 2, -5, 7], "неверные значения в списке объекта класса ListMath"
#
# res1 = lst2 + 76
# lst = ListMath([1, 2, 3])
# lst += 5
# assert lst.lst_math == [6, 7, 8] and res1.lst_math == [77, 78, 71,
#                                                        83], "неверные значения, полученные при операциях сложения"
# lst = ListMath([0, 1, 2])
# res3 = lst - 76
# res4 = 7 - lst
# print(res3.lst_math, res4.lst_math)
# assert res3.lst_math == [-76, -75, -74] and res4.lst_math == [7, 6, 5], "неверные значения, полученные при операциях вычитания"
#
# lst -= 3
# assert lst.lst_math == [-3, -2, -1], "неверные значения, полученные при операции вычитания -="
#
# lst = ListMath([1, 2, 3])
# res5 = lst * 5
# res6 = 3 * lst
# lst *= 4
# assert res5.lst_math == [5, 10, 15] and res6.lst_math == [3, 6, 9], "неверные значения, полученные при операциях умножения"
# assert lst.lst_math == [4, 8, 12], "неверные значения, полученные при операциях умножения"
#
# lst = lst / 2
# lst /= 13.0


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
#     def pop_back(self):
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
#         self.push_back(other)
#         return self
#
#
#     def __mul__(self, other):
#         for x in other:
#             self.push_back(StackObj(x))
#         return self
#

#
# assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"
#
# st = Stack()
# top = StackObj("1")
# st.push_back(top)
# assert st.top == top, "неверное значение атрибута top"
#
# st = st + StackObj("2")
# st = st + StackObj("3")
# obj = StackObj("4")
# st += obj
#
# st = st * ['data_1', 'data_2']
# st *= ['data_3', 'data_4']
#
# d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
# h = top
# i = 0
# while h:
#     assert h._StackObj__data == d[
#         i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
#     h = h._StackObj__next
#     i += 1
#
# assert i == len(d), "неверное число объектов в стеке"


# class Lib:
#     def __init__(self):
#         self.book_list = []
#
#     def __add__(self, other):
#         self.book_list.append(other)
#         return self
#
#     def __sub__(self, other):
#         if isinstance(other, Book):
#             self.book_list.remove(other)
#         else:
#             self.book_list.pop(other)
#         return self
#
#     def __len__(self):
#         return len(self.book_list)
#
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year


# class Budget:
#     def __init__(self):
#         self.item_list = []
#
#     def add_item(self, item):
#         self.item_list.append(item)
#
#     def remove_item(self, indx):
#         self.item_list.pop(indx)
#
#     def get_items(self):
#         return self.item_list
#
#
# class Item:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#
#     def __add__(self, other):
#         return self.money + other.money
#
#     def __radd__(self, other):
#         return self.money + other


# class Box3D:
#     def __init__(self, width, height, depth):
#         self.width = width
#         self.height = height
#         self.depth = depth
#
#     def __add__(self, other):
#         return Box3D(self.width + other.width, self.height + other.height, self.depth + other.depth)
#
#     def __mul__(self, other):
#         return Box3D(self.width * other, self.height * other, self.depth * other)
#
#     def __rmul__(self, other):
#         return self * other
#
#     def __sub__(self, other):
#         return Box3D(self.width - other.width, self.height - other.height, self.depth - other.depth)
#
#     def __floordiv__(self, other):
#         return Box3D(self.width // other, self.height // other, self.depth // other)
#
#     def __mod__(self, other):
#         return Box3D(self.width % other, self.height % other, self.depth % other)


# class MaxPooling:
#     def __init__(self, step=(2, 2), size=(2, 2)):
#         self.step = step
#         self.size = size
#
#     def matrix_check(self, matrix):
#         if not all([len(i) == len(matrix[0]) for i in matrix]) or \
#                 not all([all([isinstance(x, (int, float)) for x in matrix[y]]) for y in range(len(matrix))]):
#             raise ValueError("Неверный формат для первого параметра matrix.")
#
#     def __call__(self, matrix):
#         self.matrix_check(matrix)
#         result = [[0 for _ in range(len(matrix[0]) // self.step[0])] for _ in range(len(matrix) // self.step[1])]
#
#         for y in range(len(result)):
#             for x in range(len(result[0])):
#                 step_cells = []
#                 for y1 in range(self.size[1]):
#                     for x1 in range(self.size[0]):
#                         step_cells.append(matrix[x * self.size[0] + x1][y * self.size[1] + y1])
#                 result[x][y] = max(step_cells)
#         return result
#
#
# mp = MaxPooling(step=(2, 2), size=(2, 2))
# res = mp([[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]])  # [[6, 8], [9, 7]]
# print(res)


# class Track:
#     def __init__(self, start_x=0, start_y=0):
#         self.track_list = []
#         self.track_list.append(TrackLine(start_x, start_y, 0))
#
#     def __setattr__(self, key, value):
#         if isinstance(value, (int, float)) or key == "track_list":
#             super.__setattr__(self, key, value)
#
#     def add_track(self, tr):
#         self.track_list.append(tr)
#
#     def get_tracks(self):
#         return tuple(self.track_list)
#
#     def __len__(self):
#         x0, y0 = self.track_list[0].to_x, self.track_list[0].to_y
#         lenght = 0
#         for i in range(1, len(self.track_list)):
#             x1, y1 = self.track_list[i].to_x, self.track_list[i].to_y
#             lenght += ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
#             x0, y0 = x1, y1
#         return int(lenght)
#
#     def __eq__(self, other):
#         return len(self) == len(other)
#
#     def __lt__(self, other):
#         return len(self) < len(other)
#
#
# class TrackLine(Track):
#     def __init__(self, to_x, to_y, max_speed):
#         self.to_x = to_x
#         self.to_y = to_y
#         self.max_speed = max_speed
#
#     def __setattr__(self, key, value):
#         if key in ("to_x", "to_y") and isinstance(value, (int, float)) or key == "max_speed" and isinstance(value, int):
#             object.__setattr__(self, key, value)
#
#
# track1, track2 = Track(), Track(0, 1)
# track1.add_track(TrackLine(2, 4, 100))
# track1.add_track(TrackLine(5, -4, 100))
# track2.add_track(TrackLine(3, 2, 90))
# track2.add_track(TrackLine(10, 8, 90))

# res_eq = track1 == track2


# from functools import total_ordering
#
#
# @total_ordering
# class Dimensions:
#     MIN_DIMENSION = 10
#     MAX_DIMENSION = 10000
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         if self.MIN_DIMENSION <= a <= self.MAX_DIMENSION:
#             self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         if self.MIN_DIMENSION <= b <= self.MAX_DIMENSION:
#             self.__b = b
#
#     @property
#     def c(self):
#         return self.__c
#
#     @c.setter
#     def c(self, c):
#         if self.MIN_DIMENSION <= c <= self.MAX_DIMENSION:
#             self.__c = c
#
#     def volume(self):
#         return self.a * self.b * self.c
#
#     def __eq__(self, other):
#         return self.volume() == other.volume()
#
#     def __lt__(self, other):
#         return self.volume() <= other.volume()
#
#
# class ShopItem:
#     def __init__(self, name, price, dim):
#         self.name = name
#         self.price = price
#         self.dim = dim
#
#
# trainers = ShopItem('кеды', 1024, Dimensions(40, 30, 120))
# umbrella = ShopItem('зонт', 500.24, Dimensions(10, 20, 50))
# fridge = ShopItem('холодильник', 40000, Dimensions(2000, 600, 500))
# chair = ShopItem('табуретка', 2000.99, Dimensions(500, 200, 200))
# lst_shop = (trainers, umbrella, fridge, chair)
# lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
# from functools import total_ordering
#
#
# @total_ordering
# class StringText:
#     def __init__(self, lst_words):
#         self.lst_words = lst_words
#
#     def __len__(self):
#         return len(self.lst_words)
#
#     def __eq__(self, other):
#         return self.__len__() == other.__len__()
#
#     def __lt__(self, other):
#         return self.__len__() < other.__len__()
#
#     def __str__(self):
#         return " ".join(st for st in self.lst_words)
#
#
# stich = ["Я к вам пишу – чего же боле?",
#          "Что я могу еще сказать?",
#          "Теперь, я знаю, в вашей воле",
#          "Меня презреньем наказать.",
#          "Но вы, к моей несчастной доле",
#          "Хоть каплю жалости храня,",
#          "Вы не оставите меня."]
# lst_text = [StringText([x.strip("-?!,.") for x in y.split()]) for y in stich]
# lst_text_sorted = sorted(lst_text, reverse=True)
# lst_text_sorted = [str(obj) for obj in lst_text_sorted]


# class FileAcceptor:
#     def __init__(self, *args):
#         self.ext_list = [*args]
#
#     def __add__(self, other):
#         return FileAcceptor(*set(self.ext_list + other.ext_list))
#
#     def __call__(self, filename):
#         if "." in filename:
#             return filename[filename.rfind(".") + 1:] in self.ext_list
#         return False
#
#
# filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png",
#              "eq_2.xls"]
# acceptor_images = FileAcceptor("jpg", "jpeg", "png")
# acceptor_docs = FileAcceptor("txt", "doc", "xls")
# print(acceptor_images.ext_list)
# filenames = list(filter(acceptor_docs, filenames))
# print(filenames)


# from functools import total_ordering
#
#
# @total_ordering
# class Money:
#
#     def __init__(self, volume):
#         self.__volume = volume
#         self.__cb = None
#
#     @property
#     def volume(self):
#         return self.__volume
#
#     @volume.setter
#     def volume(self, volume):
#         self.__volume = volume
#
#     @property
#     def cb(self):
#         return self.__cb
#
#     @cb.setter
#     def cb(self, cb):
#         self.__cb = cb
#
#     def __eq__(self, other):
#         return round(self.value(), 1) == round(other.value(), 1)
#
#     def __lt__(self, other):
#         return round(self.value(), 1) < round(other.value(), 1)
#
#
# class MoneyR(Money):
#     def __init__(self, volume=0):
#         super().__init__(volume)
#         self.currency = "rub"
#
#     def value(self):
#         if not self.cb:
#             raise ValueError("Неизвестен курс валют.")
#         return self.volume
#
#
# class MoneyD(Money):
#     def __init__(self, volume=0):
#         super().__init__(volume)
#         self.currency = "dollar"
#
#     def value(self):
#         if not self.cb:
#             raise ValueError("Неизвестен курс валют.")
#         return self.volume * self.cb.rates["rub"]
#
#
# class MoneyE(Money):
#     def __init__(self, volume=0):
#         super().__init__(volume)
#         self.currency = "euro"
#
#     def value(self):
#         if not self.cb:
#             raise ValueError("Неизвестен курс валют.")
#         return self.volume * self.cb.rates["rub"] * self.cb.rates[self.currency]
#
#
# class CentralBank:
#     rates = {'rub': 72.5, 'dollar': 1.0, 'euro': 1.15}
#
#     def __new__(cls, *args, **kwargs):
#         return None
#
#     @classmethod
#     def register(cls, money):
#         money.cb = cls
#
#
# r = MoneyR(45000)
# d = MoneyD(500)
#
# CentralBank.register(r)
# CentralBank.register(d)
# print(r.__dict__)
# if r > d:
#     print("неплохо")
# else:
#     print("нужно поднажать")
# print(r==d)
# print(r>d)


# from functools import total_ordering
#
#
# @total_ordering
# class Body:
#     def __init__(self, name, ro, volume):
#         self.name = name
#         self.ro = ro
#         self.volume = volume
#
#     def mass(self):
#         return self.ro * self.volume
#
#     def __eq__(self, other):
#         if isinstance(other, Body): other = other.mass()
#         return self.mass() == other
#
#     def __lt__(self, other):
#         if isinstance(other, Body): other = other.mass()
#         return self.mass() < other


# class Box:
#     def __init__(self):
#         self.content = []
#
#     def add_thing(self, obj):
#         self.content.append(obj)
#
#     def get_thing(self):
#         return self.content
#
#     def __eq__(self, other):
#         return sorted(self.content) == sorted(other.content)
#
#
# class Thing:
#     def __init__(self, name, mass):
#         self.name = name
#         self.mass = mass
#
#     def __eq__(self, other):
#         return self.mass == other.mass and self.name.lower() == other.name.lower()
#
#     def __lt__(self, other):
#         return (self.name, self.mass) < (other.name, other.mass)
#
#
# b1 = Box()
# b2 = Box()
#
# b1.add_thing(Thing('мел', 100))
# b1.add_thing(Thing('тряпка', 200))
# b1.add_thing(Thing('доска', 2000))
#
# b2.add_thing(Thing('тряпка', 200))
# b2.add_thing(Thing('мел', 100))
# b2.add_thing(Thing('доска', 2000))
#
# res = b1 == b2  # True
# print(res)


# class Rect:
#     def __init__(self, x, y, width, height):
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def __hash__(self):
#         return hash((self.width, self.height))


# class Shopitem:
#     def __init__(self, name, weight, price):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.weight, self.price))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = ['Системный блок: 1500 75890.56',
#           'Монитор Samsung: 2000 34000',
#           'Клавиатура: 200.44 545',
#           'Монитор Samsung: 2000 34000']
# shop_items = {}
# for string in lst_in:
#     name, weight_price = string.split(": ")
#     obj = Shopitem(name, *weight_price.split())
#     shop_items.setdefault(obj, [obj, 0])[1] += 1


# class DataBase:
#     def __init__(self, path):
#         self.path = path
#         self.dict_db = {}
#
#     def write(self, record):
#         self.dict_db.setdefault(record, []).append(record)
#
#     def read(self, pk):
#         for item in self.dict_db.values():
#             for i in item:
#                 if i.pk == pk:
#                     return i
#
#
# class Record:
#     PK = 0
#
#     def __init__(self, fio, descr, old):
#         self.fio = fio
#         self.descr = descr
#         self.old = int(old)
#         self.pk = self.__get_PK()
#     @classmethod
#     def __get_PK(cls):
#         cls.PK+=1
#         return cls.PK
#
#     def __hash__(self):
#         return hash((self.fio.lower(), self.old))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = ['Балакирев С.М.; программист; 33',
#           'Кузнецов Н.И.; разведчик-нелегал; 35',
#           'Суворов А.В.; полководец; 42',
#           'Иванов И.И.; фигурант всех подобных списков; 26',
#           'Балакирев С.М.; преподаватель; 33'
#           ]
# lst_out = [Record(*row.split("; ")) for row in lst_in]
# db = DataBase("jsdf")
# for obj in lst_out:
#     db.write(obj)
# print(db.dict_db)


# class BookStudy:
#     def __init__(self, name, author, year):
#         self.name = name
#         self.author = author
#         self.year = year
#
#     def __hash__(self):
#         return hash((self.name.lower(), self.author.lower()))
#
#     def __eq__(self, other):
#         return hash(self) == hash(other)
#
#
# lst_in = [
#     'Python; Балакирев С.М.; 2020',
#     'Python ООП; Балакирев С.М.; 2021',
#     'Python ООП; Балакирев С.М.; 2022',
#     'Python; Балакирев С.М.; 2021',
# ]
#
# lst_bs = [BookStudy(*row.split("; ")) for row in lst_in]
# unique_books = len({*lst_bs})


# class Dimensions:
#     def __init__(self, a, b, c):
#         self.a = float(a)
#         self.b = float(b)
#         self.c = float(c)
#
#     def __setattr__(self, key, value):
#         if value <= 0:
#             raise ValueError("габаритные размеры должны быть положительными числами")
#         object.__setattr__(self, key, value)
#
#     def __hash__(self):
#         return hash((self.a, self.b, self.c))
#
#
# inp = "1 2 3; 4 5 6.78; 1 2 3; 2 1 2.5"
# lst_dims = sorted([Dimensions(*elem.split()) for elem in inp.split("; ")], key=hash)


# class Desc:
#     def __set_name__(self, owner, name):
#         self.name = "_" + name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, self.name)
#
#     def __set__(self, instance, value):
#         if not isinstance(value, (int, float)) or value > 0:
#             raise ValueError("длины сторон треугольника должны быть положительными числами")
#         setattr(instance, self.name, value)
#
#
# class Triangle:
#     a = Desc()
#     b = Desc()
#     c = Desc()
#
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.is_triangle(a, b, c)
#
#     @staticmethod
#     def is_triangle(a, b, c):
#         a, b, c = sorted([a, b, c])
#         if not a + b > c:
#             raise ValueError("с указанными длинами нельзя образовать треугольник")
#
#     def __len__(self):
#         return int(self.a + self.b + self.c)
#
#     def __call__(self):
#         p = len(self) / 2
#         return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
#
#
# tr = Triangle(4, 2, -3)
# print(tr.__dict__)


# class Player:
#     def __init__(self, name, old, score):
#         self.name = name
#         self.old = int(old)
#         self.score = int(score)
#
#     def __bool__(self):
#         return self.score > 0
#
#
# lst_in = ['Балакирев; 34; 2048',
#           'Mediel; 27; 0',
#           'Влад; 18; 9012',
#           'Nina P; 33; 0']
# players = [Player(*row.split("; ")) for row in lst_in]
#
# players_filtered = list(filter(None, players))
