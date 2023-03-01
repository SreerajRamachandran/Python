n = (input("enter the string"))
print(n)
a = "ing"
b = "ly"
p = n[:-3]
print(p)
if len(n)<3 or n[-3:]!=a:
    print(n+a)
else:
    print(n+b)