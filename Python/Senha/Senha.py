senha = 0 
tentativa = 4
while (senha < 10000 and senha < 1000):
    senha = int (input("Informe uma senha: "))
while (tentativa != 1):
    resposta = int (input("Digite a senha "))
    if (resposta == senha):
        print("Acesso concedido")
    else:
        print(f"Acesso negado: {tentativa} restante")
        tentativa = tentativa - 1