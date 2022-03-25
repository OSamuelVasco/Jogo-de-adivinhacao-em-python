from random import randint
from time import sleep
computador = randint(0, 5) #computador escolhe um número entre 0 e 5
print('-=' *28)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-='*28)
jogador = int(input('Em que número eu pensei? ')) #resposta do usuário
print('E agora...')
sleep(1.5)
if jogador == computador: #verifica se a resposta do usuário foi igual a do computador
    print('\033[1;33mPARABÉNS!\033[m Você conseguiu me vencer!')
else:
    print('\033[1;34mGANHEI!\033[m Eu pensei no número {} e não no {}'.format(computador, jogador))
