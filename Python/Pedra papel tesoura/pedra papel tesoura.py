jogador1 = str (input("Jogador um informe a sua jogada: "))
jogador2 = str (input("Jogador dois informe a sua jogada: "))

if(jogador1 == "pedra" and jogador2 == "pedra"):
    print("Empate!")
elif(jogador1 == "papel" and jogador2 == "papel"):
    print("Empate!")
elif(jogador1 == "tesoura" and jogador2 == "tesoura"):
    print("Empate!")
    
elif(jogador1 == "tesoura" and jogador2 == "papel"):
    print(f"{jogador1} ganhou de {jogador2}")
elif(jogador1 == "tesoura" and jogador2 == "pedra"):
     print(f"{jogador2} ganhou de {jogador1}")
elif(jogador1 == "pedra" and jogador2 == "tesoura"):
    print(f"{jogador1} ganhou de {jogador2}")
elif(jogador1 == "pedra" and jogador2 == "papel"):
    print(f"{jogador2} ganhou de {jogador1}")
elif(jogador1 == "papel" and jogador2 == "tesoura"):
    print(f"{jogador2} ganhou de {jogador1}")
elif(jogador1 == "papel" and jogador2 == "pedra"):
    print(f"{jogador1} ganhou de {jogador2}")
else:
    print("jogada invalida")