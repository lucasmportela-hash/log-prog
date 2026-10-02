import operator
def calcular(ope1, ope2, op):
    return op(ope1, ope2)
operacoes = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul
}
while True:
    operador = input("Escolha uma operação: ")
    if operador == "sair":
        break
    if operador not in operacoes:
        print("Operação inválida!")
        continue
    ope1 = float(input("Operador 1: "))
    ope2 = float(input("Operador 2: "))
    resultado = calcular(ope1, ope2, operacoes[operador])
    print("Resultado:", resultado)