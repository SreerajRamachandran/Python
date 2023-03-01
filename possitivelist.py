n = int(input("enter the limit"))
a = []
for i in range(0, n + 1):
    if i % 2 == 0:
        a.append(i)
print(a)
