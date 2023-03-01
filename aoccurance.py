words = str(input("enter the words"))
char = "a"
b=[i for i in words]
for i in b:
    if i == char:
        print(f"{i}={b.count(i)}")