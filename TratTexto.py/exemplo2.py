x = 'abc_123_XYZ'

print(x.lower())#minusculo
print(x.upper())#maiusculo
print(x.title())#1 letra maisucula tudo no inicio das palavras
print(x.find('123'))#retorna em qual casa esta o texto indicado,caso nao tenha retorna -1
print(x.replace('_','*'))#substitue _ por *
print(x.isalpha())#pergunta se texto tem somente letra
print(x.isnumeric())# pergunta se texto tem somente numero
print(x.split('_'))#onde tiver _ ele separa texto
print(x.count('z'))#conta quantas vezes o caractere aparece no texto