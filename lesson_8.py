# # задание 4,5,6
# class Sklad:
#
#     def __init__(self, keys, item, count):
#         self.keys = keys
#         self.item = item
#         self.count = count
#         self.sklad = {"Тип устройства": keys, "Модель": item, "Количество": count}
#         self.podrazdeleniya = {"Подразделение 1": [], "Подразделение 2": []}
#         # self.podrazdelenie1 = []
#         # self.podrazdelenie2 = []
#
#
#     def передача_в_подразделение(self):
#         for key in self.sklad:
#             if key == "Тип устройства":
#                 peredacha = self.sklad.get(key)
#                 print(f"Рассмотрение к передаче: {peredacha}")
#             if key == "Количество":
#                 peredacha2 = self.sklad.get(key)
#                 print(f"На складе имеется в наличии оборудование: {peredacha}, в размере {peredacha2} единиц.")
#                 try:
#                     kol = int(input("Сколько передать? "))
#                 except:
#                     ValueError
#                     print("Введено текстовое значение, необходимо числовое!")
#                     break
#                 if peredacha2 - kol > 0:
#                     ostatok = peredacha2 - kol
#                 else:
#                     print("Отсутствует необходимое кол-во товара на складе!")
#                     break
#                 print(f"Было на складе {peredacha}: {peredacha2}")
#                 print(f"Остаток {peredacha} на складе: {ostatok}")
#                 podr = input("Введите Подразделение 1 или Подразделение 2: ")
#                 if podr == "Подразделение 1":
#                     for kluch in self.podrazdeleniya:
#                         if kluch == 'Подразделение 1':
#                             self.podrazdeleniya.update({"Подразделение 1":[peredacha, kol]})
#                             # self.podrazdelenie1.append(peredacha)
#                             # self.podrazdelenie1.append(kol)
#                             # print(f"Подразделение 1 список :{self.podrazdelenie1}")
#                             return (f"Передано в {kluch} оборудование: {peredacha}, в размере {kol} единиц.")
#                 elif podr == 'Подразделение 2':
#                     for kluch in self.podrazdeleniya:
#                         if kluch == 'Подразделение 2':
#                             self.podrazdeleniya.update({"Подразделение 2": [peredacha, kol]})
#                             # self.podrazdelenie2.append(peredacha)
#                             # self.podrazdelenie2.append(kol)
#                             # print(f"Подразделение 2 список :{self.podrazdelenie2}")
#                             return (f"Передано в {kluch} оборудование: {peredacha}, в размере {kol} единиц.")
#
# class Orgtexnika(Sklad):
#     def __init__(self, keys, item, count):
#         super().__init__(keys, item, count)
#         self.keys = keys
#         self.item = item
#         self.count = count
#
# class Printer(Orgtexnika):
#     def __init__(self, keys, item, count):
#         super().__init__(keys, item, count)
#
#
# class Skaner(Orgtexnika):
#     def __init__(self, keys, item, count):
#         super().__init__(keys, item, count)
#
#
# class Kserox(Orgtexnika):
#     def __init__(self, keys, item, count):
#         super().__init__(keys, item, count)
#
#
# item1 = Printer("Принтер", "модель 1", 50)
# print(item1.передача_в_подразделение())
#
# item2 = Skaner("Сканер", "модель 1", 20)
# print(item2.передача_в_подразделение())
#
# item3 = Kserox("Ксерокс", "модель 1", 30)
# print(item3.передача_в_подразделение())

# # задание 1
# class Data:
#     def __init__(self, spisok_data):
#         self.spisok_data = str(spisok_data)
#
#     @classmethod
#     def obrabotka(cls, spisok_data):
#         data = []
#         for i in spisok_data.split():
#             if i != '-':
#                 data.append(i)
#         return print(f"Текущая дата: {int(data[0])}.{int(data[1])}.{int(data[2])}")
#
#     @staticmethod
#     def proverka_validacii(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2100 >= year >= 1910:
#                     return ""
#                 else:
#                     return "Неправильно указан год!"
#             else:
#                 return "Неправильно указан месяц!"
#         else:
#             return "Неправильно казан день!"
#
#     def __str__(self):
#         return f'Текущая дата {Data.obrabotka(self.spisok_data)}'
#
#
# segodnya = Data('25 - 05 - 2020')
# print(segodnya)
# print(Data.proverka_validacii(11, 14, 2020))
# print(Data.proverka_validacii(1, 11, 2219))
# print(Data.obrabotka('08 - 10 - 2016'))
# print(segodnya.obrabotka('05 - 06 - 2020'))

# # задание 2
#
# class Деление_на_ноль:
#     def __init__(self, числитель, знаменатель):
#         self.числитель = числитель
#         self.знаменатель = знаменатель
#
#     @staticmethod
#     def деление(числитель, знаменатель):
#         try:
#             return (числитель / знаменатель)
#         except:
#             ZeroDivisionError
#             return (f"Деление на ноль недопустимо")
#
#
# delit = Деление_на_ноль(0, 0)
# print(Деление_на_ноль.деление(1, 0))
# print(Деление_на_ноль.деление(1, 1))
# print(delit.деление(0, 0))

# # задание 3
# class Proverka_chisel:
#     def __init__(self):
#         self.spisok = []
#
#     def proverka(self):
#         while True:
#             dannie = input("Введите значение ")
#             if dannie == "stop":
#                 break
#             self.spisok.append(dannie)
#             print(self.spisok)
#             for i in self.spisok:
#                 try:
#                     i = int(i)
#                     print(i)
#                 except:
#                     self.spisok.remove(i)
#                     print("Введено символьное выражение")
#
# dannie = Proverka_chisel()
# dannie.proverka()

# # задание 7
#
# class Copleksnie_chisla:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         self.i = "i"
#     def __add__(self, other):
#         print(f"Результат: {(self.a + other.a)} + {(self.b + other.b)}{self.i}")
#
#     def __mul__(self, other):
#         print(f"Результат: {(self.a * other.a)} + {(self.b * other.b)}{self.i}")
#
# ch1 = Copleksnie_chisla(2, 5)
# ch2 = Copleksnie_chisla(4, 5)
# (ch1 + ch2)
# (ch1 * ch2)