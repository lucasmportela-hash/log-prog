# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.
Matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    Matriz.append(linha)
media = soma / 4
print(f"Soma: {soma}")
print(f"Média: {media}")
