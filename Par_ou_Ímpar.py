from random import randint

contagem = 0

print('=' * 30)
print('Par ou Ímpar'.center(30))
print('=' * 30)

while True:
    jogador = int(input('Digite um número de 1 a 10: '))
    computador = randint(1, 10)
    soma = jogador + computador
    resto = soma % 2

    if resto == 0:
        print('O resultado é \033[1;33mPAR\033[0m')
    else:
        print('O resultado é \033[1;31mIMPAR\033[0m')
    print(f'O Jogador escolheu o número {jogador}\nO Computador sorteou o número {computador}\nE a soma dá {soma}')

    if jogador % 2 == 0 and resto == 0:
        contagem = contagem + 1
        print(f'\033[1;34mParabéns você venceu!\n\033[0m\033[0mDepois de tentativas {contagem}')
        break
    elif jogador % 2 != 0 and resto != 0:
        contagem = contagem + 1
        print(f'\033[1;34mParabéns você venceu!\n\033[0m\033[0mDepois de tentativas {contagem}')
        break
    elif jogador % 2 == 0 and resto != 0:
        contagem = contagem + 1
        print(f'\033[1;31mTente outra vez!\033[0m')
        print('=' * 30)
    elif jogador % 2 != 0 and resto == 0:
        contagem = contagem + 1
        print(f'\033[1;31mTente outra vez!\033[0m')
        print('=' * 30)
