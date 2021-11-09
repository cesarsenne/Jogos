from random import randint
from time import sleep

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input('Digite uma opção: '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!')
sleep(0.5)

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('O computador escolheu {}.'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))

if computador == 0:  # Pedra
    if jogador == 0:  # Pedra
        print('\033[1;30mEmpate')
    elif jogador == 1:  # Papel
        print('\033[1;34mJogador Vence!')
    elif jogador == 2:  # Tesoura
        print('\033[1;31mComputador Vence')
elif computador == 1:  # Papel
    if jogador == 0:  # Pedra
        print('\033[1;31mComputador Vence')
    elif jogador == 1:  # Papel
        print('\033[1;30mEmpate')
    elif jogador == 2:  # Tesoura
        print('\033[1;34mJogador Vence!')
elif computador == 2:  # Tesoura
    if jogador == 0:  # Pedra
        print('\033[1;34mJogador Vence!')
    elif jogador == 1:  # Papel
        print('\033[1;31mComputador Vence')
    elif jogador == 2:  # Tesoura
        print('\033[1;30mEmpate')
