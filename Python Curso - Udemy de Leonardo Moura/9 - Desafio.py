#9 - Desafio:
#O rapaz está fazendo dois trabalhos, um na terça e outro na quinta
#As respostas podem ser verdadeiro ou falso
#Se ambas forem verdadeiros ele irá ao shopping comprar uma TV de 50 e a familia tomara sorvete
#Se apenas um for verdadeira eles irão ao shopping comprar tv de 32 e a familia tomara sorvete
#Se for falso pras duas ai não tomam sorvete mais ganham saude
trabalho_terca = True
trabalho_quinta = True


tv_50 = trabalho_terca and trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
saude = not sorvete

print("Tv 50' = {}, TV 32' = {}, Sorvete = {}, Saúde = {}".format(tv_50, tv_32, sorvete, saude))
