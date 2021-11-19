#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Напишите функцию, которая считывает с клавиатуры числа и перемножает их до тех пор, пока не будет введен 0.
# Функция должна возвращать полученное произведение. Вызовите функцию и выведите на экран результат ее работы.

def calc():
    count = 1
    res = 1
    while True:
        number = int(input(f"Введите число номер {count}: "))
        if number == 0:
            break
        res *= number
        count += 1
    return res


print(calc())
