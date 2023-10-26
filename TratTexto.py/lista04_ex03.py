'''. Elabore um programa que receba o nome de um aluno e verificar se ele 
existe o sobrenome “SILVA”'''

nome=input('insira seu nome:\n')
if 'silva' in nome.lower():
    print(f'o nome contem sobrenome silva')
else:
    print('o nome nao contem sobrenome silva!!')   
     
