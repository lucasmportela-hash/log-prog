Lista = []
for i in range (10):
    Aluno = input(f"Digite o nome do aluno: {i}")
    Nota = float(input("Digite a média do aluno: "))
    Lista.append([Aluno, Nota])
for AlunoNota in Lista:
    if (Aluno[1] >= 6):
        print(AlunoNota[0])