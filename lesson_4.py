# from sys import argv
# # задание 1
# script_name, норма_час, часы, РК_и_СН, Процент_премии = argv
#
# print("script_name", script_name)
# print("норма_час", норма_час)
# print("часы", часы)
# print("РК_и_СН", РК_и_СН)
# print("Процент_премии", Процент_премии)
#
# норма_час = int(argv[1])
# часы = int(argv[2])
# РК_и_СН = float(argv[3])
# Процент_премии = float(argv[4])
#
# zp = норма_час * часы * Процент_премии * РК_и_СН * 1.32
# print(zp)`

# # задание 2
# список_1 = [54, 98, 5, 8, 2, 1, 82, 9, 3]
# список_2 = [int(список_1[z]) for z, el in enumerate(список_1) if el > int(список_1[z - 1])]
# print(список_2)

# # Задание 3
# print([el for el in range(20, 241) if el % 20 == 0])

# # Задание 4
# list3 = []
# list1 = [2, 5, 6, 9, 2, 10, 9, 8, 3, 7, 0, 0]
# list2 = [z for z, el in enumerate(list1) if list1.count(el) != 2]
# print(list2)
# for x in list2:
#     list3.append(list1[x])
# print(list3)

# # Задание 5
# from functools import reduce
# список4 = [el for el in range(100, 105, 2)]
# z = 1
# def proizv(*args):
#     global z
#     for i in (args):
#         i = i * (i + 2)
#         z = z * i
#     return z
# print(reduce(proizv, список4))

# задание 6

from itertools import count, cycle
список5 = []
for el in count(1):
    if el <= 10:
        список5.append(el)
    else:
        break
print(список5)

список6 = [1, 2, 3, 4, 5]
count1 = 1
for i in cycle(список6):
    if count1 > 10:
        break
    print(i, end=" ")
    count1 += 1





# print(список4)
# def gen():
#     for el in (10, 20, 30):
#         yield el
#
# g = gen()
# print(g)
# for i in g:
# print(i)
