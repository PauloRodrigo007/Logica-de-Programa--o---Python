'''Faça um programa que lê uma string e imprima “É um Palíndromo” caso a 
string seja um palíndromo e “Não é palíndromo” caso não seja. A entrada 
não tem acentos e que todas as letras são minúsculas. Exemplos de 
palíndromo: “ovo”, “reviver”, “mega bobagem”, “anotaram a data da 
maratona”'''

nome=input('insira uma palavra:\n')
nome_invert=nome.lower().strip().replace(' ', '')
if nome_invert==nome_invert[::-1]:
    print("é um palindromo")
else:
    print('essa palavra nao é um palindromo')    