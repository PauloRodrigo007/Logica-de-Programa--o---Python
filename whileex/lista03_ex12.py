'''Escrever um programa que leia o número de matrícula dos vendedores de uma empresa, seu salário
fixo e o total de vendas de cada vendedor. Cada vendedor recebe um salário fixo, mais uma
comissão proporcional às vendas por ele efetuadas. A comissão é de 3% sobre o total de vendas até 
1.000 e 5 % sobre o que ultrapassa este valor. Escrever o número do vendedor, o total de suas 
vendas, seu salário fixo e seu salário total. OBS: A leitura deve ser encerrada quando ler a matrícula 
do vendedor com número igual a 99.'''
comissao=0
sal_novo=0
matricula=input('matricula:\n')
while matricula != '99':
    salario_fixo=float(input('Salario fixo:\n'))
    total_vendas=float(input('total de vendas:\n'))
    if total_vendas <= 1000:
        comissao= total_vendas*0.03
        sal_novo=salario_fixo + comissao
    else:
        comissao = (1000 * 0.03) + ((total_vendas - 1000) * 0.05)
        sal_novo=salario_fixo+comissao
    print(f'matricula: {matricula}')
    print(f'total vendas: {total_vendas:.2f}')
    print(f'Salario fixo: {salario_fixo:.2f}')
    print(f'comissão: {comissao:.2f}')
    print(f'Salario novo: {sal_novo:.2f}')    
    matricula=input('matricula:\n')