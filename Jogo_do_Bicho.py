from random import choice

print('=' * 50)
print('Jogo do Bicho'.center(50))
print('=' * 50)

cartela = {'Avestruz': (1, 2, 3, 4),
           'Águia': (5, 6, 7, 8),
           'Burro': (9, 10, 11, 12),
           'Borboleta': (13, 14, 15, 16),
           'Cachorro': (16, 18, 19, 20),
           'Cabra': (21, 22, 23, 24),
           'Carneiro': (25, 26, 27, 28),
           'Camelo': (29, 30, 31, 32),
           'Cobra': (33, 34, 35, 36),
           'Coelho': (37, 38, 39, 40),
           'Cavalo': (41, 42, 43, 44),
           'Elefante': (45, 46, 47, 48),
           'Galo': (49, 50, 51, 52),
           'Gato': (53, 54, 55, 56),
           'Jacaré': (57, 58, 59, 60),
           'Leão': (61, 62, 63, 64),
           'Macaco': (65, 66, 67, 68),
           'Porco': (69, 70, 71, 72),
           'Pavão': (73, 74, 75, 76),
           'Peru': (77, 78, 79, 80),
           'Touro': (81, 82, 83, 84),
           'Tigre': (85, 86, 87, 88),
           'Urso': (89, 90, 91, 92),
           'Veado': (93, 94, 95, 96),
           'Vaca': (97, 98, 99, 0),
           }

animal_escolhido = ''
while animal_escolhido not in cartela:
    animal_escolhido = str(input("Digite o nome do animal que você escolheu: ")).strip().title()
    if animal_escolhido not in cartela:
        print("Tente de novo!")
    else:
        print(f"Parabéns! Você escolheu: \033[1m{animal_escolhido}\033[0m")

numero_escolhido = ''
print(f"Você pode escolher entre os seguinte números: {cartela[animal_escolhido]}")
while numero_escolhido not in cartela[animal_escolhido]:
    numero_escolhido = int(input("Digite o número do animal que você escolheu: "))
    if numero_escolhido not in cartela[animal_escolhido]:
        print("Tente de novo!")
    else:
        print(f"Parabéns! Você escolheu o número: \033[1m{numero_escolhido}\033[0m")

deck_animal = list(cartela.keys())
animal_sorteado = choice(deck_animal)
print(f"O animal sorteado foi: \033[1m{animal_sorteado}\033[0m")

deck_numero = list(cartela[animal_sorteado])
numero_sorteado = choice(deck_numero)
print(f"O número sorteado foi: \033[1m{numero_sorteado}\033[0m")

if animal_escolhido == animal_sorteado and numero_escolhido == numero_sorteado:
    print("\033[1mParabéns! Você ganhou!\033[0m")
else:
    print("Não foi dessa vez. Tente de novo!")
