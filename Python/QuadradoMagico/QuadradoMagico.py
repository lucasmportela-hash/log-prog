# Construa um jogo Quadrado Mágico 3X3, no qual o usuário preencherá o
# vetor com números de um a nove (sem repetir números) e a soma de todas
# as linhas, colunas e diagonais será igual a quinze.
# dos valores digitados deverão ser calculadas.
Matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        valor = float(input(f"Digite o valor [{i}][{j}]: "))
        linha.append(valor)
    Matriz.append(linha)