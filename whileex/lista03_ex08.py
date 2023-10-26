'''Fazer um programa que: Leia um número indeterminado de linhas contendo cada uma a idade de 
um indivíduo. A última linha que não entrará nos cálculos contém o valor da idade igual à zero.
Calcule e imprima a idade média deste grupo de indivíduos.'''
idtotal=0
media=0
cont=0
id=float(input('insira sua idade:\n'))
while id != 0:
    idtotal+=id
    cont+=1
    id=float(input('insira sua idade:\n'))
    media=idtotal/cont
print(f'cont:{cont}\nidtotal:{idtotal}')    
print ('A idade media do grupo é',media)
