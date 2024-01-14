import random


VALID_OPTIONS = ['piedra', 'papel', 'tijera']

computer = random.choice(VALID_OPTIONS)
human = input('¿piedra, papel o tijera? Escoje una opción: ').lower()

if human in VALID_OPTIONS:

    if computer == human:
        print(f'Empate -> El computador sacó {computer} y el humano sacó {human}')

    elif (human == 'piedra' and computer == 'papel') or (human == 'papel' and computer == 'tijera') or (human == 'tijera' and computer == 'piedra'):
        print(f'Ganó la computadora -> El computador sacó {computer} y el humano sacó {human}')

    else:
        print(f'Gana el humano -> El computador sacó {computer} y el humano sacó {human}')

else:
    print(f'La opción {human} no es válida')
