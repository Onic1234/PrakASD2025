def jumlahHurufVokal(s):
    vowels = 'aiueoAIUEO'
    total_letters = 0
    vowel_count = 0
    for char in s:
        if char.isalpha():
            total_letters += 1
            if char in vowels:
                vowel_count += 1
    return (total_letters, vowel_count)

def jumlahHurufKonsonan(s):
    vowels = 'aiueoAIUEO'
    total_letters = 0
    consonant_count = 0
    for char in s:
        if char.isalpha():
            total_letters += 1
            if char not in vowels:
                consonant_count += 1
    return (total_letters, consonant_count)

k = jumlahHurufVokal('Surakarta') 
print(k)

v = jumlahHurufKonsonan('Surakarta') 
print(v)