'''A Cidade de São Paulo precisará acrescentar um algarismo 9 na frente de 
cada um dos 3 números de celulares informados via teclado no formato 
011NNNN-NNNN. Elabore um programa que receba os números originais e 
para cada um escreva o número com a modificação sugerida, ou seja, 
0119NNNN-NNNN.'''

n=input('insira seu numero:\n')
novon='011 9'+n[0:4]+'-'+n[4:]
print(novon)