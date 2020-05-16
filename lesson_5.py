# # Задание 1
# lines = (input('Введите данные через пробел '))
# список = list(lines.split(" "))
# with open("New text.txt", "w+") as new_obj:
#     for val in список:
#         new_obj.write(val + '\n')
#     new_obj.seek(0)
#     dannie = new_obj.read()
# print(dannie)

# # Задание 2
# with open("задание2.txt", "r") as задание_2:
#     chto2 = ""
#     for z, line in enumerate((задание_2),1):
#         kol_vo_strok = z
#     задание_2.seek(0)
#     for chto in задание_2:
#         chto = chto.replace("\n", "")
#         chto2 = chto2 + " " + chto
#         listok = ["".join(chto2)]
#     задание_2.seek(0)
#     for val in listok:
#         listok2 = val.split(" ")
#     задание_2.seek(0)
#     for x, el in enumerate((listok2),1):
#         count_slova = x
# print(f"Количество строк = {kol_vo_strok} \nКоличество слов = {count_slova - 1}")

# # Задание 3
# with open(r"text_3.txt", "r+", encoding="utf-8") as okladi:
#     global x
#     x = []
#     for el in okladi:
#         el = el.replace("\n", '')
#         el = el.split(" ")
#         # el = ' '.join(el)
#         x.append(el)
#     def listmerge1(*args): # преобразование массива двумерного в одномерный
#         all = []
#         for lst in args:
#             for el in lst:
#                 for x in el:
#                     all.append(x)
#         return all
#     x = listmerge1(x)
#     da = len(x)
#     dict = {}
#     for chisl in range(0, da, 2): # наполнение словаря
#         d = {x[chisl]: x[chisl + 1]}
#         dict.update(d)
#     for key, value in dict.items():
#         value = float(value)
#         if value < 20000:
#             print(f"Зарплата ниже 20 тысяч рублей у {key}.\nРеально располагаемая зарплата составляет: {value} рублей.")
#     sum = 0
#     sum = float(sum)
#     for key, value2 in dict.items():
#         value2 = float(value2)
#         sum = value2 + sum
#     print(f"Средняя заработная плата сотрудников =  {round(sum / ((chisl+2) / 2), 2)}")

# #Задание 4
# with open("text_4.txt", "r+", encoding="utf-8") as chisla:
#     slovar_perevod = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
#     global x
#     x = []
#     for el in chisla:
#         el = el.replace("\n", '')
#         el = el.split(" ")
#         x.append(el)
#     # print(el, end=" ")
#     def listmerge1(*args):  # преобразование массива двумерного в одномерный
#         all = []
#         for lst in args:
#             for el in lst:
#                 for x in el:
#                     all.append(x)
#         return all
#     x = listmerge1(x)
#     print(x)
#     for c, el in enumerate(x):
#         for key, val in slovar_perevod.items():
#             if el == key:
#                 x.insert(c, val)
#                 x.remove(el)
#     print(x)
#     x = ' '.join(x)
#     print(x)
# with open("text4_2.txt", "w+", encoding="utf-8") as newText:
#     newText.writelines(x)

# #Задание 5
#
# with open("text_5.txt", "w+", encoding="utf-8") as chisla2:
#     x = [str(z) for z in range(1,21)]
#     x = ' '.join(x)
#     print(x)
#     chisla2.writelines(x)
# with open("text_5.txt", "r+", encoding="utf-8") as podschet_chisel:
#     sum = 0
#     for i in podschet_chisel:
#         i = i.split(" ")
#         for z in i:
#             z = int(z)
#             sum = sum + z
#     print(f"Сумма чисел = {sum}")

#Задание 6 не успел доделать
with open(r"text_6.txt", "r+", encoding="utf-8") as slovar:
    global x
    x = []
    p = []
    sum = ""
    for el in slovar:
        el = el.replace("\n", '')
        el = el.split(" ")
        el = ' '.join(el)
        x.append(el)
    # print(x)
    for i in x:
        for c in i:
            if c == "-":
                continue
            for t in c:
                if type(int(t)) == type(int(1)):
                    t = int(t)
                    t = str(t)
                    sum = sum + t
                    if len(sum) == 2:
                        # p.append(sum)
                        print(p)
                        # sum = ""
                        c = ""
                        break
            p.append(sum)
            sum = ""
        p.append(c)
    print(p)




