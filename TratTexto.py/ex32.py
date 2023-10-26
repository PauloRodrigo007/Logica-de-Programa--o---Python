'''Ex32 - Receba um nome com, no mínimo,  10 caracteres via teclado. 
Com ele você deve gerar uma senha no seguinte formato: 
dividir o nome recebido em duas partes 
e concatenar os dois primeiros caracteres da segunda parte, com os caracteres “%%” 
e os três últimos caracteres da primeira parte. Exiba ao final a parte1, a parte 2 e a senha.'''


nome=input('insira um nome:\n')

while len(nome) < 10 :
    print('digite um nome com no minimo 10 caractere')
    nome=input('insira um nome:\n')

divisao= len(nome) // 2 
print(divisao)

parte1=  nome[0:divisao]
print(parte1)

parte2= nome[divisao:]
print(parte2) 

senha= parte2[0:2] + '%%' + parte1[-3:]
print(senha)
    
   