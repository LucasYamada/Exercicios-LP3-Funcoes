import random

def escolherPalavra():
    palavras = ["cadeira", "computador", "python", "arvore", "teclado","elefante", "banana", "cachorro", "guitarra", "abacaxi"]
    return list(random.choice(palavras))

def mostrarPalavra(letras_certas, letras_usuario):
    for i in range (len(letras_certas)):
        if letras_certas[i] in letras_usuario:
            print(letras_certas[i], end="")
        else:
            print("_", end="")

def forca():
    letras_certas = escolherPalavra()
    tentativas = len(letras_certas) * 2
    letras_usuario = []
    while tentativas > 0:
        tentativas -=1
        mostrarPalavra(letras_certas, letras_usuario)
        print()
        letra = input("Digite uma letra: ")
        print("\n\n")
        if letra in letras_certas and letra not in letras_usuario:
            for i in letras_certas:
                if letra == i:
                    letras_usuario.append(letra)
            if len(letras_certas) != len(letras_usuario):
                print("Essa letra pertence a essa palavra")
                print("Restam ",tentativas," tentativas.\n")
        elif letra in letras_certas and letra in letras_usuario:
            print("Voce ja escolheu essa letra!")
            tentativas += 1
            print("Restam ",tentativas," tentativas.\n")
        else: 
            print("Essa letra nao pertence a essa palavra")
            print("Restam ",tentativas," tentativas.\n")
        if len(letras_certas) == len(letras_usuario):
            print("Parabens, voce venceu!!")
            print("A palavra certa era:")
            mostrarPalavra(letras_certas, letras_usuario)
            break
        
    if len(letras_certas) != len(letras_usuario):
        print("As tentativas acabaram, tente novamente.")

forca()
