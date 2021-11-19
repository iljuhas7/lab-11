#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В основной ветке программы вызывается функция cylinder(), которая вычисляет площадь цилиндра.
# В теле cylinder() определена функция circle(), вычисляющая площадь круга по формуле πr2.
# В теле cylinder() у пользователя спрашивается, хочет ли он получить только площадь боковой
# поверхности цилиндра, которая вычисляется по формуле 2πrh, или полную площадь цилиндра.
# В последнем случае к площади боковой поверхности цилиндра должен добавляться удвоенный результат
# вычислений функции circle().


from math import pi


def cylinder(r, h):
    def circle(rc):
        return pi * rc ** 2

    s = 2 * pi * r * h
    if input('Full area? [y/n]: ') == 'y':
        s += 2 * circle(r)

    return s

ra, ha = 1, 1
print('s =', cylinder(ra, ha))