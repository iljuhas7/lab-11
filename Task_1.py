#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def positive():
    print("Положительное")


def negative():
    print("Отрицательное")


def test():
    a = int(input())
    if a > 0:
        positive()
    elif a < 0:
        negative()


if __name__ == '__main__':
    test()
