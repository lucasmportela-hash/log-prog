import random
rodada = 1
tentativa = 0 
pontos = 100
pontosTotais = 0 
while (rodada != 4):
    num = random.randint(1, 50)
    while (tentativa != 5):
        print (num)
        print (f"Rodada: {rodada}")
        tentativa = tentativa + 1
        print (f"Tentativa: {tentativa}")
        palpite = int (input("Adivinhe um número entre 1 e 50: "))
        if (palpite > num):
            print("Palpite maior que o número")
            pontos = 0
        elif(palpite < num):
            print("Palpite menor que o número")
            pontos = 0
        else:
            print("Palpite certo")
            if (tentativa == 1):
                pontos = 100
            elif (tentativa == 2):
                pontos = 75
            elif (tentativa == 3):
                pontos = 50
            elif (tentativa == 4):
                pontos = 25
            elif (tentativa == 5):
                pontos = 10
            tentativa = 5
    tentativa = 0 
    pontosTotais = pontosTotais + pontos
    rodada = rodada + 1

if (pontosTotais > 200):
    print(f"Excelente pontuação de: {pontosTotais}")
elif (pontosTotais >= 100):
    print(f"Bom pontuação de: {pontosTotais}")
elif (pontosTotais <100):
    print("Tente novamente :( ")

