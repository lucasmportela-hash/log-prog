
rodada = 0
tentativa = 0 
pontos = 100

while (rodada != 3):
    import random
    num = random.randint(1, 50)
    while (tentativa != 5):
        print (num)
        palpite = int (input("Adivinhe um número entre 1 e 50: "))
        if (palpite > num):
            print("Palpite maior que o número")
            tentativa = tentativa + 1
            pontos = pontos - 25
        elif(palpite < num):
            print("Palpite menor que o número")
            tentativa = tentativa + 1
            pontos = pontos - 25
        else:
            print("Palpite certo")
            tentativa = 5
    rodada = rodada + 1
print(pontos)

#Encerrar a rodada caso o jogador acerte, somando
#pontos: 100 pontos na 1a tentativa, 75 na 2a, 50 na 3a, 25
#na 4a e 10 na 5a.
#● Indicar fim de tentativas na rodada com 0 pontos ganhos
#se esgotar as 5 chances.

#■ No final das 3 rodadas, avalie a pontuação total com if/elif/else e
#imprima a classificação: "Excelente" (acima de 200), "Bom"
#(entre 100 e 200) ou "Tente Novamente" (abaixo de 100).