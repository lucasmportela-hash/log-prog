a = float (input ("Informe o valor de a: "))
b = float (input ("Informe o valor de b: "))
c = float (input ("Informe o valor de c: "))

if(a + b > c and a + c > b and b + c > a):
    if (a == b == c):
        print("Equilátero")
    elif(a != b != c):
        print("Escaleno")
    elif(a == b or a == c or b == c):
        print("Isósceles")
else:
        print("Erro")