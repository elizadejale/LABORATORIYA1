import random

# Ədədi massiv yaratmaq
lst = [random.randint(0, 101) for _ in range(10)]
print("lst =", lst)

# Faylı yaratmaq və ədədləri daxil etmək
with open('file.txt', 'w') as f:
    s = str(len(lst))
    f.write(s + '\n')
    for i in lst:
        s = str(i)
        f.write(s + ' ')

# Faylı oxumaq və elementləri 2 dəfə artırmaq
with open('file.txt', 'r') as f:
    s = f.readline()
    lst2 = []
    for line in f:
        # strs vektorunun yaradılması
        strs = line.split(' ')
        print('strs=', strs)
        for s in strs:
            if s != '':
                lst2 = lst2 + [int(s)]

# Hər bir elementi 2 dəfə artırmaq
lst2_doubled = [x * 2 for x in lst2]
print('Doubled:', lst2_doubled)

# Yeni fayla yazmaq və elementlərin cəmini hesablayaraq yazmaq
with open('file_doubled.txt', 'w') as f_doubled:
    s = str(len(lst2_doubled))
    f_doubled.write(s + '\n')
    for i in lst2_doubled:
        s = str(i)
        f_doubled.write(s + ' ')

    # Elementlərin cəmini hesablayaraq yeni fayla yazmaq
    cem = sum(lst2_doubled)
    s = str(cem)
    f_doubled.write('\nCem:' + s)

# Faylı oxumaq və en axırdakı elementlərin cəmini əldə etmək
with open('file_doubled.txt', 'r') as f_doubled:
    len_doubled = int(f_doubled.readline())
    elements_doubled = [int(x) for x in f_doubled.readline().split() if x]
    cem_doubled = int(f_doubled.readline().split(':')[-1])

print("En axırdakı elementlərin cəmi:", cem_doubled)
