#!/usr/local/bin/python
# --*-- conding: utf-8 --*--
import math
import sys

def circulo(raio):
    return math.pi * float(raio)**2

if __name__ == '__main__':
    raio = sys.argv[0]
    area = circulo(raio)
    print(area)

