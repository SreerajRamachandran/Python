n = int(input("enter number of integers"))
list1 = []
for i in range(1, n + 1):
    list1.append(i)

for i in list1:
    if i % 2 == 0:
        list1.remove(i)
print(list1)
