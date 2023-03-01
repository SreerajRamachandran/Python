n = int(input("enter the limit of integers"))
a = []
b = []
for i in range(96, n+1):
    a.append(i)

for i in a:
    if i > 100:
        b.append("over")
    else:
        b.append(i)
print(b)
