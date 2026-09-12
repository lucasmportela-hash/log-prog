cargo = str (input("Informe o seu cargo: ")).lower()
horario = int (input("Informe o horário atual: "))
chave = str (input("Informe a chave de emergência: (Sim/Não) ")).lower()

if (chave == "sim"):
    acesso = True
else:
    acesso = False  

if ((cargo == "supervisor" or cargo == "operador") and (horario >= 8 and horario <=17) or (acesso == True)):
    print("Acesso Permitido")
else :
    print("Acesso Bloqueado")
