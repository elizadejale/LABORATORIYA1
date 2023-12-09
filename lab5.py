import random

lst = []
for i in range(10):
    number = random.randint(0, 50)
    lst = lst + [number]
print("lst=", lst)

with open('file.txt', 'w') as f:
    s = str(len(lst))
    f.write(s + '\n') 

    for i in range(5):
        s = str(lst[i])
        f.write(s + '\n')  
    sum_of_first_5 = sum(lst[:5])
    f.write(f"Sum of the first 5 numbers: {sum_of_first_5}\n")  

with open('file.txt', 'r') as f:
    s = f.readline().strip()
    lst_size = int(s)

    lst2 = []
    for _ in range(5):
        line = f.readline().strip()
        lst2.append(int(line))

    sum_line = f.readline().strip()
    sum_of_first_5_from_file = int(sum_line.split(":")[1].strip())

print("Read from file:")
print("Size of lst:", lst_size)
print("First 5 numbers:", lst2)
print("Sum of the first 5 numbers:", sum_of_first_5_from_file)