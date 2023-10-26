'''- Elabore um programa  que permita receber uma frase via teclado e exibir no vídeo 
a quantidade de letras “a” existentes na frase e  a frase recebida invertida'''

frase=input('insira uma frase:\n')

print(frase.lower().count('a'))

print(frase[::-1])
