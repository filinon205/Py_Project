# # задание 1
# list_1 = [25, "", 254, "10%", "численность", 2020]
# for i in list_1:
#     print(f"Указан тип {type(i)}")
#
# list_2 = [1, 2, 3, 4, 5, 6]
# print(list_2)
# list_2.sort(reverse = True)
# print(list_2)
#
# # задание 2
# values = input("Введите значения через запятую ")
# лист1 = list(values.split(","))
# print(f"{лист1}")
# количество_итераций = len(лист1) // 2
# print(f"Количество итераций: {количество_итераций}")
# a = 0;
# b = 1;
# n = 0
# while n != количество_итераций:
#     лист1[a], лист1[b] = лист1[b], лист1[a]
#     a = a + 2
#     b = b + 2
#     n = n + 1
# print(лист1)
#
# #Задание 3
# список_времен_года = [None, "Зима", "Зима", "Весна", "Весна", "Весна", "Лето", "Лето", "Лето", "Осень", "Осень",
#                       "Осень", "Зима"]
# while True:
#     номер_месяца = int(input("Введите номер месяца от 1 до 12 "))
#     if номер_месяца > 0 and номер_месяца <= 12:
#         print(f"Данный месяц относится к времени года: {список_времен_года[номер_месяца]}")
#         break
#     else:
#         print('Вы ввели неправильно номер месяца')
#
# словарь_времена_года = {1: "Зима", 2: "Зима", 3: "Весна", 4: "Весна", 5: "Весна", 6: "Лето", 7: "Лето", 8: "Лето",
#                         9: "Осень", 10: "Осень", 11: "Осень", 12: "Зима"}
# while True:
#     номер_месяца = int(input("Введите номер месяца от 1 до 12 "))
#     if номер_месяца > 0 and номер_месяца <= 12:
#         print(словарь_времена_года.get(номер_месяца))
#         break
#     else:
#         print('Вы ввели неправильно номер месяца')
#
# #Задание 4
# value = input("Введите слова через пробел ")
# список = list(value.split(" "))
# список2 = list()
# for i in (список):
#     razmer = len(i)
#     if razmer >= 10:
#         i = i[:10:]
#         список2.append(i)
#     else:
#         список2.append(i)
# for id, i in enumerate(список2,1):
#     print(id, i)

# # Задание 5
# a = int(input("Введите значение "))
# список_знач  = [7,6,6,5,4,3,2,1]
# index = 0
# povtor = список_знач.count(a)
# for i in (список_знач):
#     if a < i:
#         index = index + 1
#     elif a == i and povtor > 1:
#         index = index + povtor - 1
#         список_знач.insert(index,a)
#         print(список_знач, end=" ")
#         break
#     elif a == i and povtor == 1:
#         index = index
#         список_знач.insert(index, a)
#         print(список_знач, end=" ")
#         break
#     else:
#         список_знач.insert(index, a)
#         print(список_знач, end=" ")
#         break
# # Задание 6 не успел сделать.

# def my_fun(s1, s2, s4=55):
#     sum = s1 + s2 * s4
#     print(f"Sum {sum}")
# my_fun(33, 34, s4=55)

# def my_fun():
#     pass
# print(my_fun())

# def my_fun(s):
#     ss = s ** 2
#     return ss
# print(my_fun(6))

# def my_fun(s):
#     ss = s ** 2
#     num = 33
#     return ss, num
# print(my_fun(6))

# #неопр. число неименованных параметров
# def my_fun(*args):
#    return args
# print(my_fun(6, 7, 5 ,8 ,5, 9))

# # неопр. число именованных параметров
# def my_fun(**kwargs):
#    return kwargs
# print(my_fun(k1=1, k2=1, k3=1))

# # анонимная функция
# my_fun = lambda s1, s2: s1 ** s2
# print(my_fun(2,3))

# my_list = [1, 434, 35, 53, 5, 9]
# print(max(my_list))

# a = list(range(1, 8, 2))
# print(a)


# def my_fun ():
#     global s2, s3 # объявление глобальных переменных для вывода из функции
#     s1 = int(input())
#     s2 = s1 + 100
#     s3 = s1 * s1
#     s4 = s2 + s3
#     return s4
# print(my_fun())
# print(s2)

# def my_fun():
#     s2 = 11
#
#     def in_fun():
#         nonlocal s2
#         s2 += 1
#     return s2
# f1 = my_fun
# print(f1())
# print()

# def my_fun(p1 = 0, p2 = 1):
#     """division.
#
#      params:
#      p1 -- 0.0
#      p2 -- 1.0
#
#      """
#     return p1 / p2


# num = input("enter num ")
# try:
#     num = int(num)
#     print(num)
# except ValueError:
#     print("non type - str!")