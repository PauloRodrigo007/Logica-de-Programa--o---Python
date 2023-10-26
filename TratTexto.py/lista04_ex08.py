'''Nome na vertical em escada. Modifique o programa anterior de forma a 
mostrar o nome em formato de escada.
o F
o FU
o FUL
o FULA
o FULAN
o FULANO'''

nome= input('digite seu nome:\n')
escada=''
for c in nome:
    escada+=c
    print(escada)