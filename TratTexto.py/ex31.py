'''Ex31- Operação_Frase: Faça um programa que receba uma frase qualquer informada via teclado 
e escreva no vídeo o que se segue:
Os Primeiros 5(cinco) caracteres da frase;
Os últimos 5(cinco) caracteres da frase;
Os primeiros 5(cinco) caracteres da frase invertidos;
A quantidade de caracteres contidos na frase;'''
tex=input('insira uma frase qualquer:\n')
#a
print(tex[0:6])
#b
print(tex[-5:])
#c
print(tex[0:6][::-1])
#d
print(len(tex))