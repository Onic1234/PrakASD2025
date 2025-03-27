def binSe(arr, target):
    """
    Melakukan binary search pada array yang sudah terurut.
    Mengembalikan index elemen jika ditemukan, atau False jika tidak ditemukan.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Mengembalikan index elemen yang ditemukan
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False  # Mengembalikan False jika elemen tidak ditemukan

# Contoh penggunaan
arr = [10, 20, 30, 40, 50]
target = 30
result = binSe(arr, target)
if result is not False:
    print(f"Elemen {target} ditemukan pada index {result}.")
else:
    print(f"Elemen {target} tidak ditemukan.")

target = 25
result = binSe(arr, target)
if result is not False:
    print(f"Elemen {target} ditemukan pada index {result}.")
else:
    print(f"Elemen {target} tidak ditemukan.")