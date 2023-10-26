'''Elabore um programa que receba 50  frases via teclado e ao final exiba a maior frase digitada'''
maiorfra=''
tam=0
for c in range(4):
    frase=input('digite uma frase:\n')
if len(frase) > tam:
    tam= len(frase)
    maiorfra = frase

print(f'a maior frase é {maiorfra}')        
        
    
   