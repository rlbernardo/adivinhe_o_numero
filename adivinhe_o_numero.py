import random
nome = input('Qual o seu nome? ')


def adiv(x):
    num_al = random.randit(1, x)
    adiv = 0
    while adiv != num_al:
        adiv = int(input(f'Escolha um número entre 1 e {x}: '))
        if adiv < num_al:
            print('desculpe, tente de novo. Mais baixo.')
        elif adiv > num_al:
            print('Desculpe, tente novamente. Mais alto')


    print(f'Aí sim {nome}, Parabéns! Você achou o número {num_al}. Foi fácil ou dificil?')