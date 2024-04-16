def palindromo(palavra):

    palavra = palavra.lower()
    palavra = palavra.replace(" ","")

    i = 0
    j = len(palavra)-1

    while i < j:
        if palavra[i] != palavra[j]:
            return False
        i += 1
        j -= 1
        
    return True

print(palindromo("A base do teto desaba"))