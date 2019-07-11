#Função de chamada de tela
def chamadaTela():
    print('*' * 60)
    print('\t\t\tRPG GAME')
    print('*' * 60)
    print('Selecione uma opção:\n1 - Novo Jogo\n2 - Load Jogo\n3 - Sair')

#Jogo
chamadaTela()
chamadaMenu = int(input('Qual opção? '))
while chamadaMenu != 3:
    if chamadaMenu == 1:
        print('Opção 1')
    elif chamadaMenu == 2:
        print('Opção 2')
    elif chamadaMenu == 3:
        print('Saindo do jogo')
    else:
        print('Opção inválida')
        chamadaMenu = int(input('Qual opção? '))  

