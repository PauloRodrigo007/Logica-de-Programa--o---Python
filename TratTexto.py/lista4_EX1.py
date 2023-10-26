'''Elabore um programa que receba 5 frases e no final exiba o total de letras 
“A” existentes em todas as frases digitadas.'''
conta=0

for c in range(5):
    frase=input('insira uma frase:\n')
    frase.lower()
    if frase.count('a') >= 1 :
        conta +=frase.count('a')
print (f'o total de letra A nas frases são {conta}')
     
    
    


