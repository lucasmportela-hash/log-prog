cargo = str (input("Informe o seu cargo: ")).lower()
horario = int (input("Informe o horário atual: "))
chave = input("Informe a chave de emergência: (1-Sim/0-Não): ") == "1"
if ((cargo == "supervisor" or cargo == "operador") and (horario >= 8 and horario <=17) or (chave)):
    print("Acesso Permitido")
else :
    print("Acesso Bloqueado")