'''Faça um programa que leia um número indeterminado de números, o programa encerra quando for 
digitado o número 99. O programa deve fornecer ao final o percentual de números pares e ímpares 
digitados.'''

n=float(input('insira um numero:\n'))
contpar=0
contimpar=0
mediaimpar=0
mediapar=0

while n!=99:
    if n % 2 == 0:
        contpar+=1
    else:
        contimpar+=1
    n=float(input('insira um numero:\n'))       
if contpar + contimpar != 0:
    mediapar=contpar/(contpar+contimpar)*100
    mediaimpar=contimpar/(contimpar+contpar)*100

print(f'a media dos pares:{mediapar:.1f}\na media dos impares :{mediaimpar:.1f}')        
