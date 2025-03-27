def binSeAll(arr, target):
    """
    Melakukan binary search pada array yang sudah terurut.Mengembalikan semua index elemen yang ditemukan dalam bentuk list.Jika elemen tidak ditemukan, mengembalikan list kosong.
    """
    low = 0
    high = len(arr) - 1
    result = []

    # Binary search to find one occurrence of the target
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            # Expand to the left and right to find all occurrences
            left = mid
            while left >= 0 and arr[left] == target:
                result.append(left)
                left -= 1
            right = mid + 1
            while right < len(arr) and arr[right] == target:
                result.append(right)
                right += 1
            result.sort()  # Ensure the indexes are sorted
            return result
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return []  # Return an empty list if the target is not found
# Contoh penggunaan
arr = [2, 3, 5, 6, 6, 6, 8, 9, 9, 10, 11, 12, 13, 13, 14]
target = 6
result = binSeAll(arr, target)
if result:
    print(f"Elemen {target} ditemukan pada index {result}.")
else:
    print(f"Elemen {target} tidak ditemukan.")
target = 7
result = binSeAll(arr, target)
if result:
    print(f"Elemen {target} ditemukan pada index {result}.")
else:
    print(f"Elemen {target} tidak ditemukan.")