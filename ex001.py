import random

def advinhacao():
    n = random.randint(1,100)
    palpite = 0
    while palpite != n:
        palpite = int(input("Faca um palpite: "))
        if palpite > n:
            print("O palpite esta acima do numero")
        elif palpite < n:
            print("O palpite esta abaixo do numero")
        else:
            print("Parabens voce acertou!!!")
            break