''' Escrever um programa que lê 10 valores, um de cada vez, e conta quantos deles estão no intervalo 
fechado entre 10 e 20 e quantos deles estão fora do intervalo, no final escreva estes resultados.'''

contdentro=0
contfora=0
for c in range(10):
    n=int(input('insira um numero:\n'))
    if n >=10 and n<=20:
        contdentro+=1
    else:
        contfora+=1
print(f'A qtd de numeros dentro do intervalo é {contdentro}\ne a qtd fora do intervalo é {contfora}\n(intervalo 10 e 20)')            