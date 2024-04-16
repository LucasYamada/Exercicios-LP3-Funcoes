def contarPalavras(frase):
    frase_nova = ""

    for palavra in frase:
        if palavra.isalpha() or palavra.isdigit() or palavra == " ":
            frase_nova += palavra
        
    frase_nova = frase_nova.lower()
    frase_nova = frase_nova.split(" ")

    palavras = {}

    for palavra in frase_nova:
        if palavra in palavras.keys():
            palavras[palavra] += 1
        else:
            palavras.update({palavra:1})

    return palavras

print(contarPalavras("O vento sussurra segredos enquanto as folhas dançam ao ritmo da natureza, natureza que inspira, inspira sonhos e desejos."))