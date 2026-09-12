RendaMensal = float (input("Informe sua renda mensal: "))
score = int (input("Informe seu score: "))
RestricoesEntrada = str (input("Possui restrições (Verdadeiro/Falso): ")).lower() 
if RestricoesEntrada == "verdadeiro":
    Restricoes = True
else:
    Restricoes = False
if (score >= 700 and RendaMensal > 4000 and Restricoes == False):
    print("APROVADO")
elif (RendaMensal >= 2500 and Restricoes == False and score >= 500) or (RendaMensal >6000):
    print("APROVADO")
else:
    print("REPROVADO")
