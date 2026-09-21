# Construa uma página onde o usuário digitará o nome e a média de cinco
# alunos e o programa só aceitará a média do aluno caso ela esteja entre zero
# e dez.
Notas = []
Nomes = []
for i in range(3):
    Nome = str(input(f"Digite o seu nome aluno {i + 1}: "))
    Nota = float(input(f"Digite a sua média: "))
    if (Nota >= 0 and Nota <= 10):
        Nomes.append(Nome)
        Notas.append(Nota)
    else:
        print("Media Invalida!")
        i -= 1
print(Nomes)
print(Notas)

