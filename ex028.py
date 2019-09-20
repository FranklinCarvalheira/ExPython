from random import randint
from time import sleep
comp = randint(0, 5) #Gera um número aleatório
n = int(input('Qual o número o computador pensou entre 0 e 5? '))
print('PROCESSANDO...')
sleep(3)
if n == comp:
    print('Venceu')
else:
    print('Perdeu')
    print('Pensei em {}'.format(comp))
