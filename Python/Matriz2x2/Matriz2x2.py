# Construa uma matriz 2X2 e, como saída desse programa, a média e a soma
# dos valores digitados deverão ser calculadas.
Matriz = []
soma = 0
contador = 0
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    Matriz.append(linha)
for linha in range (len(Matriz)):
    for coluna in range (len(Matriz[linha])):
        soma += Matriz[linha][coluna]
        contador += 1
media = soma/contador
print(f"Média: {media} \nSoma: {soma}")
