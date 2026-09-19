faturamentototal = 0.0
cliente = 1
produto = 0.0
while (cliente != 0):
    total = 0.0
    while (produto != -1):
        total = total + produto
        produto = float (input("Informe o valor do produto: "))
    produto = 0.0
    if (total > 200):
         total = total * 0.9
    elif (total > 100):
            total = total * 0.95
    faturamentototal = total + faturamentototal
    parcelas = int (input("Quantas parcelas serão? "))
    if (parcelas == 1):
         print (total)
    else:
        total = total / parcelas
        for i in range(parcelas, 0, -1):
            print(f"{i} parcela de {total:.2f}")
    cliente = float (input("Novo cliente? "))
print(f"Faturamento total de: {faturamentototal:.2f}") 