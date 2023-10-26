''' Faça um programa que fique lendo valores até encontrar o valor zero, com cada valor lido faça a 
soma dos 10 valores subsequentes e mostre a soma e a média desses valores.'''


soma=0
n=int(input('insira um numero:\n'))
while n != 0:
    for n in range(n+1,n+11):
        soma += n
    print(f'a soma dos 10 consecutivos é {soma}\nE sua media é {soma/10}')  
    n=int(input('insira um numero:\n'))    
      