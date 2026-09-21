import random
import math
rodada = 0
pontosTotais = 0
while (rodada != 3):
    tentativa = 0 
    pontos = 0
    num = random.randint(1, 50)
    while (tentativa != 5):
        print (num)
        print (f"Rodada: {rodada+1}")
        tentativa += 1
        print (f"Tentativa: {tentativa}")
        palpite = int (input("Adivinhe um número entre 1 e 50: "))
        if (palpite > num):
            print("Palpite maior que o número")
        elif(palpite < num):
            print("Palpite menor que o número")
        else:
            print("Palpite certo")
            pontos = (125 - 25 * tentativa) + 10 * math.floor(tentativa / 5)
            break
    pontosTotais = pontosTotais + pontos
    rodada += 1
if (pontosTotais > 200):
    print(f"Excelente pontuação de: {pontosTotais}")
elif (pontosTotais >= 100):
    print(f"Bom pontuação de: {pontosTotais}")
elif (pontosTotais <100):
    print(f"Tente novamente :( {pontosTotais}")

