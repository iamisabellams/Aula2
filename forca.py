def forca():
    
    palavra = "carrossel"
    descobertas = ["*" for _ in palavra]
    tentativas = 11

    exibir=print("Você iniciou o jogo da FORCA! Você tem:", (tentativas), "tentativas")
    while "*" in descobertas and tentativas > 0:
        letra = input("Digite uma letra: ")

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    descobertas[i] = letra
            print(" ".join(descobertas))
        else:
            tentativas -= 1
            print(" ".join(descobertas))
            print("Tentativas restantes:", tentativas)

    if "*" not in descobertas:
        print("Você acertou a palavra!")
    else:
        print("\n\tVocê perdeu ! A palavra era:\n  \n\tDragão\n ")

forca()