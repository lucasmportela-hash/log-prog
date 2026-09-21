import random
num = random.randint(1, 100)
print(num)
tentativa = int(input("Adivinhe o número: "))
if (tentativa == num):
    print("Acertou!")
else:
    print("Errou!")     