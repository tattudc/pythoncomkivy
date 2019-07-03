#!/usr/local/bin/python
# --*-- conding: utf-8 --*--
import math

def circulo(raio):
    print("Área do circulo", math.pi * float(raio)**2)

if __name__ == '__main__':   
    raio = input('Digite um raio ')
    circulo(raio)

