# Construa um programa que exiba a contagem regressiva de 10 até 0
def regressiva(x):
    if x <= 0:
        print("Acabou")
    else:
        print(x)
        regressiva(x-1)
contagem = regressiva(10)
print (contagem)