import random
matris = [[random.randint(1, 100) for _ in range(5)] for _ in range(5)]
print("Əvvəlki matriks:")
for setr in matris:
    print(setr)
for sira in range(len(matris)):
    en_boyuk = max(matris[sira])
    matris[sira][sira] = en_boyuk


print("Ən böyük elementi baş diaqonalda yerləşdirmiş matriks:")
for setr in matris:
    print(setr)
