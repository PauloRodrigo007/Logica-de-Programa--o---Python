'''Faça um programa que leia o nome e a idade de 15 pessoas e apresente:
a. Maior idade
b. Nome da pessoa mais nova
c. Média das idades'''
maiorid=0
menorid=999
somaid=0
nomemenorpess=''
for c in range(4):
    nome=input('insira seu nome:\n')
    idade=int(input('insira sua idade:\n'))
    somaid+=idade
    media=somaid/4
    if idade>maiorid:
        maiorid=idade
    if  idade<menorid:
        menorid=idade
        nomemenorpess=nome   


        
print(f'A maior idade é {maiorid}\nnome da pessoa mais nova:{nomemenorpess}\na media das idades é:{media:.2f}')        
