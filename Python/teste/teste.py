def conta_numeros(n):
    p = 1
    for num in range(n+1):
        if num%2 == 0:
            p += 1
    return p