''' Faça um programa que leia 20 números inteiros e apresente:
a. Média dos ímpares
b. Maior número par
c. Diferença do maior menos o menor número'''
npar=0
soma=0
maiorn=0
menorn=999999
contimp=0
for c in range(8):
    n=int(input('insira um numero: '))
    if n % 2 == 0:
        if n > npar:
            npar = n
    else: 
        soma+=n
        contimp+= 1  
    if n>maiorn:
        maiorn=n
    if n<menorn:
        menorn=n
        
print(f'a media dos impares é {soma/contimp:.2f}\no maior numero par é {maiorn}\ndiferenca entre maior e menor é {maiorn-menorn}')        
            



