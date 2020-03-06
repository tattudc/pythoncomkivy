#!/usr/bin/env python3

#LER ARQUIVO E INSERIR EM MATRIZ O LABIRINTO
f = open("lab.txt",'r')
texto = f.readlines()

x = 0

while x < len(texto):
    if texto[x] == "\n":
        local = texto.index(texto[x])
        texto.pop(local)
    else:
        texto[x] = texto[x].split(',')
        x += 1

# Esse for abaixo aqui é só para tirar o "\n" em algumas strings, é opcional.

for i in texto:
    local = texto.index(i) # Local do i em texto
    for b in i:
        local2 = texto[local].index(b) # Local2 do b em i ( local )
        if "\n" in b:
            texto[local][local2] = b.replace("\n",'') # Substitui o valor de acordo com "local" e "local2"

lista1 = texto
print("lista1 =",lista1)

#ACHAR O INICIO DO LABIRINTO
