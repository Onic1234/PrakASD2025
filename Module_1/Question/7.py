def faktorPrima(n):
    i = 2
    faktor = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            faktor.append(i)
    if n > 1:
        faktor.append(n)
    return tuple(faktor)

# Contoh penggunaan
print(faktorPrima(10))   
print(faktorPrima(120))
print(faktorPrima(19))  