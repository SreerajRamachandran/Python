current = int(input("enter the current year"))
future = int(input("enter the future year"))
a = []
for i in range(current, future + 1, 2):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        a.append(i)
print(a)
