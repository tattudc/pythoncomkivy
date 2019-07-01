PALAVRAS_PROIBIDAS = ['futebol', 'politica', 'religião']
textos = [
    'João gosta de futebol e politica',
    'A praia foi divertida',
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in  PALAVRAS_PROIBIDAS:
            print('Texto possui pelo menos uma palavra proibida', palavra)
            found = True
            break
    if not found:
        print('Texto Autorizado', texto)

