# задание 4,5,6
class Sklad:

    def __init__(self, keys, item, count):
        self.keys = keys
        self.item = item
        self.count = count
        self.sklad = {"Тип устройства": keys, "Модель": item, "Количество": count}
        self.podrazdeleniya = {"Подразделение 1": [], "Подразделение 2": []}
        # self.podrazdelenie1 = []
        # self.podrazdelenie2 = []


    def передача_в_подразделение(self):
        for key in self.sklad:
            if key == "Тип устройства":
                peredacha = self.sklad.get(key)
                print(f"Рассмотрение к передаче: {peredacha}")
            if key == "Количество":
                peredacha2 = self.sklad.get(key)
                print(f"На складе имеется в наличии оборудование: {peredacha}, в размере {peredacha2} единиц.")
                try:
                    kol = int(input("Сколько передать? "))
                except:
                    ValueError
                    print("Введено текстовое значение, необходимо числовое!")
                    break
                if peredacha2 - kol > 0:
                    ostatok = peredacha2 - kol
                else:
                    print("Отсутствует необходимое кол-во товара на складе!")
                    break
                print(f"Было на складе {peredacha}: {peredacha2}")
                print(f"Остаток {peredacha} на складе: {ostatok}")
                podr = input("Введите Подразделение 1 или Подразделение 2: ")
                if podr == "Подразделение 1":
                    for kluch in self.podrazdeleniya:
                        if kluch == 'Подразделение 1':
                            self.podrazdeleniya.update({"Подразделение 1":[peredacha, kol]})
                            # self.podrazdelenie1.append(peredacha)
                            # self.podrazdelenie1.append(kol)
                            # print(f"Подразделение 1 список :{self.podrazdelenie1}")
                            return (f"Передано в {kluch} оборудование: {peredacha}, в размере {kol} единиц.")
                elif podr == 'Подразделение 2':
                    for kluch in self.podrazdeleniya:
                        if kluch == 'Подразделение 2':
                            self.podrazdeleniya.update({"Подразделение 2": [peredacha, kol]})
                            # self.podrazdelenie2.append(peredacha)
                            # self.podrazdelenie2.append(kol)
                            # print(f"Подразделение 2 список :{self.podrazdelenie2}")
                            return (f"Передано в {kluch} оборудование: {peredacha}, в размере {kol} единиц.")

class Orgtexnika(Sklad):
    def __init__(self, keys, item, count):
        super().__init__(keys, item, count)
        self.keys = keys
        self.item = item
        self.count = count

class Printer(Orgtexnika):
    def __init__(self, keys, item, count):
        super().__init__(keys, item, count)


class Skaner(Orgtexnika):
    def __init__(self, keys, item, count):
        super().__init__(keys, item, count)


class Kserox(Orgtexnika):
    def __init__(self, keys, item, count):
        super().__init__(keys, item, count)


item1 = Printer("Принтер", "модель 1", 50)
print(item1.передача_в_подразделение())

item2 = Skaner("Сканер", "модель 1", 20)
print(item2.передача_в_подразделение())

item3 = Kserox("Ксерокс", "модель 1", 30)
print(item3.передача_в_подразделение())