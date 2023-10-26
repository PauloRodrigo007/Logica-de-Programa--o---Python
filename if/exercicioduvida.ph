'''#entrada
segundos = float (input('insira tempo de duraçao em segundos: '))
#processamento
minutos= float (segundos*60) %60
horas= float (segundos*3600)
#saida
print('os segundos sao:',segundos,"\nos minutos sao: ",minutos,'\nashoras sao: ',horas)'''

#entrada
seg=int (input("Entre com o Tempo em segundos: "))
#processamento
horas=int (seg / 3600)
min=int (seg-(horas*3600)) / 60
seg=(seg-(horas*3600)-(min*60))
#saida
print(horas," Horas,",min," Minutos e",seg, " Segundos")