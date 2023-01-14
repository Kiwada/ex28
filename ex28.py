#ex28
from random import randint
computador = randint(0,5)#randomiza o pc
#print('Pensei no número {}.'.format(computador)) faz o cpu pensar
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar ... ')
print('-=-'* 20)
jogador = int(input('Em que número eu pensei ?')) # jogador tenta adivinhar
if jogador == computador:
    print('Parabéns Acertou')
elif jogador > 6 :
    print ('Comando Invalido')
else:
    print('You Die , eu pensei no Número {} e não no {}'.format(computador , jogador))
