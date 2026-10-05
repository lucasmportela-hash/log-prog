# Desenvolva um programa que leia os valores de uma matriz 2 × 4 de números
# inteiros. O programa deve contar quantos valores estão abaixo de um limiar, que
# também será informado pelo usuário, estão presentes na estrutura e exibir a
# contagem total, além de imprimir a matriz completa formatada em linhas e colunas.
Matriz = []
Contador = 0
Limiar = int(input("Informe um limiar: "))
for i in range(2):
    Linha = []
    for j in range(4):
        valor = int(input(f"Digite o valor [{i}][{j}]: "))
        if valor < Limiar:
            Contador += 1
        Linha.append(valor)
    Matriz.append(Linha)
for Linha in Matriz:
    print(Linha)
print(f"{Contador} estão abaixo do limiar!")