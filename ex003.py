def vogaisConsoantes(frase):
    frase = frase.lower()

    letras = {
        "a": "vogal",
        "e": "vogal",
        "i": "vogal",
        "o": "vogal",
        "u": "vogal",
        "q": "consoante",
        "w": "consoante",
        "r": "consoante",
        "t": "consoante",
        "y": "consoante",
        "p": "consoante",
        "s": "consoante",
        "d": "consoante",
        "f": "consoante",
        "g": "consoante",
        "h": "consoante",
        "j": "consoante",
        "k": "consoante",
        "l": "consoante",
        "z": "consoante",
        "x": "consoante",
        "c": "consoante",
        "v": "consoante",
        "b": "consoante",
        "n": "consoante",
        "m": "consoante"
    }

    vogais = 0
    consoantes = 0

    for i in frase:
        if i in letras:
            if letras[i] == "vogal":
                vogais = vogais +1
            else:
                consoantes = consoantes +1

    return vogais, consoantes