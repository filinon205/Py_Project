# # задание 1
#
# class Matrix:
#
#     def __init__(self, list1):
#         self.list1 = list1
#
#     def __str__(self):
#         list2 = []
#         for lst in self.list1:
#             for el in lst:
#                 list2.append(el)
#         for v, t in enumerate(list2):
#             if v % 2 == 0:
#                 "\n".join(str(t))
#                 print(f"({t}", end="   ")
#             else:
#                 str(t)
#                 print(f"{t})")
#         return ""
#     def __add__(self, other):
#         all = []
#         for z, lst in enumerate(self.list1):
#             all.append([])
#             for x in range(len(lst)):
#                 all[z].append(self.list1[z][x] + other.list1[z][x])
#         return all
#
# matrix_1 = Matrix([[1, 2], [3, 4], [5, 6]])
# matrix_2 = Matrix([[10, 20], [30, 40], [50, 60]])
#
# print(matrix_1 + matrix_2)
# print(matrix_2)
# print(matrix_1)

# # задание 2
# from abc import ABC, abstractmethod
#
#
# class Odezhda(ABC):
#     def __init__(self, размер, рост):
#         self.размер = размер
#         self.рост = рост
#
#     @abstractmethod
#     def rasxod(self):
#         return (self.размер / 6.5 + 0.5) + 2 * self.рост + 0.3
#
#     def __add__(self, other):
#         return (self.размер + other.размер, self.рост + other.рост)
#
#
# class Palto(Odezhda):
#     def __init__(self, размер, рост):
#         super().__init__(размер, рост)
#
#     def rasxod(self):
#         return (self.размер / 6.5 + 0.5)
#
#
# class Costum(Odezhda):
#     def __init__(self, размер, рост):
#         super().__init__(размер, рост)
#
#     def rasxod(self):
#         return (2 * self.рост + 0.3)
#
#
#
# paltishko = Palto(50, 150)
# print(f"Размер пальто 1: {round(paltishko.rasxod(), 2)}")
#
# costumchik = Costum(0, 180)
# print(f"Размер костюма: {round(costumchik.rasxod(), 2)}")
#
# paltishko2 = Palto(80, 170)
# print(f"Размер пальто 2: {round(paltishko2.rasxod(), 2)}")
#
# print(f"Затрачено материала: {round(paltishko.rasxod() + costumchik.rasxod() + paltishko2.rasxod() , 2)}")

# задание 3

class Kletka:
    def __init__(self, parametry):
        self.parametry = parametry

    def make_order(self, yach):
        x = self.parametry // yach
        schet = 0
        vivod = ""
        while schet != x:
            vivod = yach * "*" + "\n" + vivod
            schet += 1
        ostatok = self.parametry % yach
        ostatok = ostatok * "*" + "\n"
        return vivod + ostatok
        return ((yach - x) * "*") + (("*" * x) + "\n")

    def __add__(self, other):
        return (self.parametry + other.parametry)

    def __sub__(self, other):
        return self.parametry - other.parametry if self.parametry - other.parametry > 0 else "Ячеек в первой клетке меньше чем во второй!"

    def __mul__(self, other):
        return self.parametry * other.parametry

    def __truediv__(self, other):
        return self.parametry / other.parametry

kletki_1 = Kletka(18)
kletki_2 = Kletka(15)
print(f"Количество клеток в организме 1:\n{kletki_1.make_order(5)}")
print(f"Количество новых клеток в новом организме: {kletki_1 + kletki_2}\n{kletki_1.make_order(5) + kletki_2.make_order(5)}")
print(f"Количество новых клеток в редуцированном организме: {kletki_1 - kletki_2}")
print(f"Произведение новых клеток в новом организме: {kletki_1 * kletki_2}")
print(f"Деление клеток в новом организме: {kletki_1 / kletki_2}")