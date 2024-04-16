def votacao():
    candidatos = ["Candidato 1","Candidato 2","Candidato 3"]

    votos = [0,0,0]

    votos_validos = 0

    while votos_validos < 20:
        voto = int(input("Digite o numero do candidato: "))
        if voto > 0 and voto < 4:
            votos[voto-1] = votos[voto-1] +1
            votos_validos += 1
        else:
            print("Digite um numero valido!")
            

    print("")

    for i in range(0,len(votos)):
        print(candidatos[i]," tem ",votos[i], " votos.") 

    print("")

    ganhadores = []
    maior = 0

    for i in votos:
        if i >= maior:
            maior = i

    for i in range(0,len(votos)):
        if votos[i] == maior:
            ganhadores.append(i)

    if len(ganhadores) == 1:
        print("O ganhador foi: ",candidatos[ganhadores[0]])
    else:
        print("Houve um empate entre: ",candidatos[ganhadores[0]], " e ", candidatos[ganhadores[1]])
