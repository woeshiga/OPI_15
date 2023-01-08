#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(func):
    def wrapper(*args):
        print(f'Площадь круга равна = {func(*args):1.2f}')
    return wrapper


@decorator
def s_circle(r):
    import math

    return math.pi * r**2


if __name__ == '__main__':
    s_circle(int(input('enter r: ')))
