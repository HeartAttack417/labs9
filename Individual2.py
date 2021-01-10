#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Triangle с полями-сторонами. Определить методы изменения сторон,
# вычисления углов, вычисления периметра. Создать производный класс Equilateral
# (равносторонний), имеющий поле площади. Определить метод вычисления площади.

import math


class Triangle:

    def __init__(self, a, b, c, alpha=0, beta=0, gamma=0):
        self.__a = a
        self.__b = b
        self.__c = c

    def set_a(self, a):
        self.__a = a

    def get_a(self):
        return self.__a

    def set_b(self, b):
        self.__b = b

    def get_b(self):
        return self.__b

    def set_c(self, c):
        self.__c = c

    def get_c(self):
        return self.__c

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        for part in parts:
            if part == 0:
                raise ValueError()

        self.set_a(parts[0])
        self.set_b(parts[1])
        self.set_c(parts[2])

    def srav(self):
        if self.__a + self.__b > self.__c and  self.__a + self.__c > self.__b and self.__c + self.__b > self.__a:
            return "Треугольник существует"
        else:
            return "Треугольник с такими сторонами невозможен"

    def __angles(self):
        alpha = math.degrees(math.acos((self.get_b() ** 2 + self.get_c() ** 2 - self.get_a() ** 2)
                                              / (2 * self.get_c() * self.get_b())))
        beta = math.degrees(math.acos((self.get_a() ** 2 + self.get_c() ** 2 - self.get_b() ** 2)
                                             / (2 * self.get_a() * self.get_c())))
        gamma = math.degrees(math.acos((self.get_a() ** 2 + self.get_b() ** 2 - self.get_c() ** 2)
                                              / (2 * self.get_a() * self.get_b())))
        return alpha, beta, gamma

    def get_angles(self):
        return self.__angles()

    def per(self):
        return self.__a + self.__b + self.__c


class Equilateral(Triangle):
    def __init__(self, a=0, b=0, c=0):
        super(Equilateral, self).__init__(a, b, c)

    def read(self, prompt=None):
        Triangle.read(self, prompt)
        return self.get_angles

    def square(self):
        p = (self.get_a() + self.get_b() + self.get_c()) * 0.5
        return math.sqrt(p * (p - self.get_a()) * (p - self.get_b()) * (p - self.get_c()))


if __name__ == '__main__':
    Triagle = Equilateral()
    Triagle.read("Введите стороны прямоугольника ")
    print("Площадь S={} "
          "Углы {} ".format(Triagle.square(), Triagle.get_angles()))
