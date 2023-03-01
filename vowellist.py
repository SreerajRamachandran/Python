a = ["a", "e", "i", "o", "u"]
n = str(input("enter the word"))
c = [i for i in n]
print(c)
for i in c:
    if i in a:
        print(i)

