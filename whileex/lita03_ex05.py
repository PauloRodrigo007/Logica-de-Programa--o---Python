'''Uma pesquisa sobre algumas características físicas da população de uma determinada região
coletou os seguintes dados referentes a cada habitante para serem analisados:
• Sexo (“M” - Masculino, “F” - Feminino)
• Cor dos Olhos (“A”-Azul,”V”-Verde, “C’-Castanho)
• Idade em anos
Para cada habitante foi digitada uma linha com esses dados e a última linha, que não corresponde a 
ninguém conterá o valor de idade igual a -1. Fazer um programa que determine e imprima:
a) A maior idade dos habitantes;
b) A porcentagem de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos inclusive e
que tenham olhos verdes;'''

maiorid=0
contm=0
cont=0
sexo=input('insira seu sexo:(F/M)\n')
cor_olhos = input('qual cor dos olhos você tem?azul,verde,castanho\n')
idade = int(input('qual é sua idade?'))
while idade != -1:
    sexo=input('insira seu sexo:(F/M)\n')
    cor_olhos = input('qual cor dos olhos você tem?azul,verde,castanho\n')
    idade = int(input('qual é sua idade?\n'))   
    if idade>maiorid:
        maiorid=idade
    if sexo.upper()== 'F':
        contm+=1
        if idade >=18 and idade<=35:
            if cor_olhos.upper()== 'V':
                cont+=1

print(f'a maior idade é {maiorid}\nA porcentagem das mulheres entre 18 e 35 anos de olhos verdes é {(cont/contm)*100:.2f}')