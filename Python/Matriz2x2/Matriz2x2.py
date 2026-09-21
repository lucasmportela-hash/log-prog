# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.
Matriz = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = float(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    Matriz.append(linha)
    soma = 0 
for i in range(2):
    for j in range(2):
        soma += Matriz[i][j]
media = soma / 4
print(f"Soma: {soma}")
print(f"Média: {media}")