''' Tem-se um conjunto de dados contendo altura e sexo (“M” ou “F”) de 50 pessoas, fazer um 
programa que calcule e escreva:
a) a maior e a menor altura do grupo
b) média de altura das mulheres
c) o número de homens'''


maioralt=0
menoralt=99999
media=0
conthomen=0
medaltmulh=0
for c in range(5):
    altura= float(input('insira a altura:\n'))
    sexo=input('insira o sexo:(M/F)\n')
    if sexo.upper() == 'M':
        conthomen+=1
    else:
        medaltmulh+=altura
    if altura > maioralt:
        maioralt=altura
    if altura < menoralt:
        menoralt=altura
    print(f'maior altura:{maioralt}')
    print(f'menor altura:{menoralt}')
    print(f'média de altura das mulheres:{medaltmulh/(5)}')
    print(f'quantidade de homens:{conthomen}')
    
