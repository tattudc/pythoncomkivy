#Exercicio 18 do site Python Brasil
#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps)
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanhoArq = input("Quantos MB tem seu arquivo? ")
velocidadeNet = input("Qual a velocidade da sua internet? ")
velocidadeReal = (float(velocidadeNet)* 1000)/8
tamanhoReal = float(tamanhoArq) * 1024
taxaTransf = float(tamanhoReal)/float(velocidadeReal)
taxaReal = float(taxaTransf)/60
taxaReal = taxaReal - (float(taxaReal) % 1)
print("Para o download de {}MB na velocidade de {}Mbps ira demorar {:.0f}minutos".format(tamanhoArq, velocidadeNet, taxaReal))