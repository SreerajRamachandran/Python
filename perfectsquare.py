
a = []
j = 32
i = int(input("initial range"))
f = int(input("final range"))
for i in range(f + 1):
    if j ** 2 == i:
        if i % 2 == 0:
            a.append(i)
        j += 1
print(a)
