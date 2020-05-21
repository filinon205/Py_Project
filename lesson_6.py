# # задание 1
# import time
# import os
# class TrafficLight:
#     def __init__(self, color):
#         self.__color = color
#     def running(self):
#         print("Запуск")
#         while True:
#             for i in self:
#                 if i == "Красный свет":
#                     print("\033[31m\033[41m {}".format("Красный свет"))
#                     print("\n" * 50)
#                     time.sleep(7)
#                     print("\033[0m")
#                     print("\n" * 50)
#                 elif i == "Желтый свет":
#                     print("\033[33m\033[43m {}".format("Желтый свет"))
#                     print("\n" * 50)
#                     time.sleep(2)
#                     print("\033[0m")
#                     print("\n" * 50)
#                 elif i == "Зеленый свет":
#                     print("\033[32m\033[42m {}".format("Желтый свет"))
#                     print("\n" * 50)
#                     time.sleep(7)
#                     print("\033[0m")
#                     print("\n" * 50)
#                 elif i == "Желтый свет":
#                     print("\033[33m\033[43m {}".format("Желтый свет"))
#                     print("\n" * 50)
#                     time.sleep(2)
#                     print("\033[0m")
#                     print("\n" * 50)
#
# svetofor = TrafficLight
# svetofor.running(["Красный свет", "Желтый свет", "Зеленый свет", "Желтый свет"])

# # Задание 2
# class Road:
#     itog = None
#
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def massa(self):
#         self.__mass = int(input("Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см: "))
#         self.__tall = int(input("Введите толщину асфальта в см: "))
#         return self.__length * self.__width * self.__mass * self.__tall
#
#
# a = Road(20, 5000)
# print(f"Масса асфальта составит {a.massa() / 1000} тонн.")

# # Задание 3
# class Worker:
#     __income = {}
#
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#
#
# class Position(Worker):
#     def __init__(self, name, surname, position):
#         super().__init__(name, surname, position)
#
#     def get_full_name(self):
#         return self.surname + " " + self.name
#
#     def get_total_income(self):
#         new_dict = {"wage": int(input("Введите оклад ")),
#                     "bonus": float(input("Введите процент премирования в виде вещественного числа "))}
#         self._Worker__income.update(new_dict)
#         wage = self._Worker__income.get("wage")
#         bonus = self._Worker__income.get("bonus")
#         salary = wage + (wage * bonus)
#         return salary
#
#
# worker1 = Position("Петр", "Петрович", "Аналитик")
# worker2 = Position("Василий", "Зайцев", "Аналитик")
# print("Полное имя: ", worker1.get_full_name())
# print("Зарплата: ", worker1.get_total_income())
# print("Полное имя: ", worker2.get_full_name())
# print("Зарплата: ", worker2.get_total_income())

# Задание 4
import random
class Car:

    showspeed = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self. is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")
        return ""

    def stop(self):
        print("Машина остановилась")
        return ""
    def turn_direction(self):
        direction = ['Прямо', 'Налево', 'Направо', 'Назад']
        print(f"Машина поехала: {random.choice(direction)}")
        return ""

    def show_speed(self):
        self.showspeed = random.randrange(0, 180)
        print(f"Текущая скорость: {self.showspeed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        self.showspeed = random.randrange(0, 180)
        if self.showspeed > 60:
            previshenie = self.showspeed - 60
            print(f"Текущая скорость: { self.showspeed}, скорость превышена на: {previshenie} км/ч")
        else:
            print(f"Текущая скорость: { self.showspeed}")
        if self.is_police == True:
            print("Полицейская машина")
        else:
            print("Не относится к полиции")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        # self.showspeed == random.randrange(0, 180)
        # print("Текущая скорость", self.showspeed)
        if self.is_police == True:
            print("Полицейская машина")
        else:
            print("Не относится к полиции")

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        self.showspeed = random.randrange(0, 180)
        if self.showspeed > 60:
            previshenie = self.showspeed - 40
            print(f"Текущая скорость: {self.showspeed}, скорость превышена на: {previshenie} км/ч")
        else:
            print(f"Текущая скорость: {self.showspeed}")
        if self.is_police == True:
            print("Полицейская машина")
        else:
            print("Не относится к полиции")
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police == True:
            print("Полицейская машина")
        else:
            print("Не относится к полиции")
        # self.showspeed = random.randrange(0, 180)
        # print("Текущая скорость", self.showspeed)

car1 = TownCar(75, "Red", "BMW", 0)
print(f"\033[31m {car1.go()} \033[0m {car1.turn_direction()} {car1.show_speed()} {car1.stop()} ", end="")

car2 = SportCar(90, "Black", "Lexus", 0)
print(f"\033[31m {car2.go()} \033[0m {car2.turn_direction()} {car2.show_speed()} {car2.stop()} ", end="")

car3 = WorkCar(50, "Green", "Kamaz", 0)
print(f"\033[31m {car3.go()} \033[0m {car3.turn_direction()} {car3.show_speed()} {car3.stop()} ", end="")

car4 = PoliceCar(80, "Blue", "Lada", 1)
print(f"\033[31m {car4.go()} \033[0m {car4.turn_direction()} {car4.show_speed()} {car4.stop()} ", end="")
