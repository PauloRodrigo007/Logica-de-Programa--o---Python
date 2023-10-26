'''Num frigorífico existem 90 bois. Cada boi traz preso em seu pescoço um cartão contando seu número de identificação e seu peso.
Fazer um programa que escreva o número e peso do boi mais  gordo e do boi mais magro'''
idgordo=''
idmagro=''
boimagro=9999
boigordo=0
for c in range(3):
    id=(input('insira a identificação do boi:\n'))
    peso=float(input('insira o peso do boi:\n'))
    if peso > boigordo:
        boigordo=peso
        idgordo=id
    if peso<boimagro:
        boimagro=peso
        idmagro=id    
print(f'o boi mais magro pesa {boimagro} e sua id é {idmagro}\no boi mais gordo pesa {boigordo} e sua id é {idgordo}')