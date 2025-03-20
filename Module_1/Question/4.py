def rerata(b):
    total = sum(b)
    n = len(b)
    hasil = total / n
    return hasil

def variance(x):
    mean = rerata(x)
    total_squared_diff = sum((xi - mean) ** 2 for xi in x)
    var = total_squared_diff / len(x)
    return var

def stdev(x):
    var = variance(x)
    std_dev = var ** 0.5
    return std_dev


print(rerata([1, 2, 3, 4, 5]))  
g = [3, 4, 5, 4, 3, 4, 5, 2, 2, 10, 11, 23]
print(rerata(g))  
print(variance(g)) 
print(stdev(g)) 