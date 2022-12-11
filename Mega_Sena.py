from random import randint
from random import uniform

jogo_jogador = list()
jogo_loteria = list()
lista_jogador = list()
lista_loteria = list()
stop = True
contagem_jogos = 0
premio = ()

print('-=' * 30)
print('Jogo da Mega Sena'.center(60))
print('Cada Aposta Custa: R$ 4.50'.center(60))
print('A Probabilidade de Acerto é de 1 em 50,063,860'.center(60))
print('Os prêmios vão de R$ 348,732.75 até R$ 317,853,788.54'.center(60))
print('-=' * 30)
print('Boa Sorte!'.center(60))
quantidade_jogos = int(input('Digite a quantidade de jogos: '))
print('-=' * 30)

valor_da_aposta = quantidade_jogos * 4.5
print(f"O valor da primeira aposta foi de: R$ {valor_da_aposta:,.2f}")
print('-=' * 30)

while contagem_jogos < quantidade_jogos:
    for numero in range(0, 6):
        while True:
            numero_sorteado = randint(1, 60)
            if numero_sorteado not in jogo_jogador:
                jogo_jogador.append(numero_sorteado)
                break
    jogo_jogador.sort()
    if jogo_jogador not in lista_jogador:
        lista_jogador.append(jogo_jogador[:])
        jogo_jogador.clear()
        contagem_jogos += 1
    else:
        jogo_jogador.clear()

for jogo in range(0, len(lista_jogador)):
    print(f"O {jogo + 1}º jogo escolhido foi: {lista_jogador[jogo]}")

print('-=' * 30)
print('Começando o Sorteio'.center(60))
print('Aguarde até que o seu número seja sorteado. '.center(60))
print('Essa etapa pode demorar um pouco.'.center(60))
print('-=' * 30)

while stop:
    for numero in range(0, 6):
        while True:
            sorteio_loteria = randint(1, 60)
            if sorteio_loteria not in jogo_loteria:
                jogo_loteria.append(sorteio_loteria)
                break
    jogo_loteria.sort()
    lista_loteria.append(jogo_loteria[:])
    for numero in range(0, len(lista_jogador)):
        if lista_jogador[numero] == jogo_loteria:
            print("Parabéns! Você Ganhou!".center(60))
            print(f"O jogo sorteado foi: {jogo_loteria}\nE você jogou: {lista_jogador[numero]}")
            stop = False
            premio = uniform(348732.75, 317853788.54)
    jogo_loteria.clear()

custo_total = (len(lista_loteria)) * valor_da_aposta
lucro_ou_prejuizo = premio - custo_total

print('-=' * 30)
print('Resumo do Sorteio'.center(60))
print(f"Foram sorteados \033[1m{len(lista_loteria):,.0f}\033[0m jogos até você ganhar o prêmio.")
print(f"O custo com jogos até você ganhar o prêmio foi de: R$ \033[1m{custo_total:,.2f}\033[0m")
print(f"O seu prêmio foi de: R$ \033[1m{premio:,.2f}\033[0m")
print(f"O seu saldo foi de: R$ \033[1m{lucro_ou_prejuizo:,.2f}\033[0m")
print('-=' * 30)
