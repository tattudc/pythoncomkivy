#!/usr/local/bin/python
# --*-- conding: utf-8 --*--
import math

def circulo(raio):
    return math.pi * float(raio)**2

if __name__ == '__main__':   
    raio = input('Digite um raio ')
    area = circulo(raio)
    print(area)

