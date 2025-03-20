import math

def selesaikanABC(a, b, c):
    determinant = b**2 - 4*a*c
    if determinant < 0:
        print("Determinannya negatif. Persamaan tidak mempunyai akar real.")
    else:
        root1 = (-b + math.sqrt(determinant)) / (2*a)
        root2 = (-b - math.sqrt(determinant)) / (2*a)
        return root1, root2

# Example usage:
print(selesaikanABC(1, 2, 3)) 
print(selesaikanABC(1, -3, 2))  