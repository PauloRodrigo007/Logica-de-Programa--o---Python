'''Elabore um programa que receba 5 placas de automóvel no formato 
“LLLNLNN” onde: “L” são letras e “N” são números, calcule e exiba para cada 
uma das placas recebidas a soma dos valores que estão nas posições “N”'''
soma=0
somageral=0
p1=int
p2=int
p3=int
for c in range(5):
    placa=input('insira a placa no veiculo:\n') 
    p1=int(placa[3])
    p2=int(placa[5])
    p3=int(placa[6])
    soma=p1+p2+p3
    somageral+=soma
print(f'a soma dos n placa é {somageral}')    

