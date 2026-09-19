import time
senha = 0 
tentativa = 3
while (senha < 10000 and senha < 1000):
    senha = int (input("Informe uma senha: "))

while (tentativa != 0):
    resposta = int (input("Digite a senha: "))
    if (resposta == senha):
        print("Acesso concedido")
        break   
    else:
        tentativa = tentativa - 1
        print(f"Acesso negado: {tentativa} restante")
        if (tentativa == 0):
            print("Conta bloqueada")
print("Sistema inicializando em:")
for i in range(5, 0, -1):
    print(i)
    time.sleep(1)
print("Sistema inicializado :D")
