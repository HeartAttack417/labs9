#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Goods (товар). В классе должны быть представлены поля: наименование
# товара, дата оформления, цена товара, количество единиц товара, номер накладной, по
# которой товар поступил на склад. Реализовать методы изменения цены товара, изменения
# количества товара (увеличения и уменьшения), вычисления стоимости товара

import math


class Goods:

    def __init__(self):
        self.__coast = 0
        self.__date = 0
        self.__name = 0
        self.__kolich = 0
        self.__number = 0

    def read(self, name, kolich, date, coast, number):
        self.set_name(name)
        self.kolich(kolich)
        self.set_date(date)
        self.coast(coast)
        self.set_number(number)

    def set_name(self, prompt=None):
        self.__name = input() if prompt is None else input(prompt)

    def set_date(self, prompt=None):
        self.__date = input() if prompt is None else input(prompt)

    def coast(self, prompt=None):
        self.__coast = int(input()) if prompt is None else input(prompt)

    def kolich(self, prompt=None):
        self.__kolich = int(input()) if prompt is None else input(prompt)

    def set_number(self, prompt=None):
        self.__number = input() if prompt is None else input(prompt)

    def set_kolich(self, a):
        self.__kolich = int(a)

    def set_coast(self, a):
        self.__coast = int(a)

    def get_info(self):
        return self.__coast, self.__date, self.__name, self.__kolich, self.__number

    def __stiom(self):
        return int(self.__coast) * int(self.__kolich)

    def dispaly(self):
        print("Наименование товара: {}; "
              "Дата оформления - {}; "
              "Цена товара - {};"
              "Количество единиц товара - {}; "
              "Номер накладной - {}."
              "Стоимость всего товара - {}".format(self.__name, self.__date, self.__coast, self.__kolich, self.__number,
                                                   self.__stiom()
                                                   )
              )


if __name__ == '__main__':
    print(((22**2+22+1)%15+1))
    T1 = Goods()
    T1.read("Введите название товара ",
            "Введите количество товара ",
            "Введите дату оформления ",
            "цену товара ",
            "номер накладной "
            )
    T1.dispaly()
    T1.set_kolich(173)
    T1.set_coast(153)
    T1.dispaly()
