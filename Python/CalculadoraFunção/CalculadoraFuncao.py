import math
def calcular(ope1, ope2, cond):
    if (cond == "+"): 
        resultado = ope1 + ope2
    elif(cond == "-"): 
        resultado = ope1 - ope2
    elif(cond == "*"): 
        resultado = ope1 * ope2
    elif(cond == "/"): 
        resultado = ope1 / ope2
    else:
        print("Operação invalida!")
        return 0
    return resultado
operacao = str (input("Escolha uma operação: "))
while operacao != "sair":
    ope1 = float(input("Operador 1: "))
    ope2 = float(input("Operador 2: "))
    resultado = calcular(ope1, ope2, operacao)
    print(resultado)
    operacao = str (input("Escolha uma operação: "))
