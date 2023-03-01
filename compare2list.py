a = []
b = []
sum_a = 0
sum_b = 0

list1 = input("Enter the elements of list1 separated by space: ").split()
for i in list1:
    a.append(int(i))
print(a)

list2 = input("Enter the elements of list2 separated by space: ").split()
for i in list2:
    b.append(int(i))
print(b)

c = len(a)
d = len(b)
print(c)
print(d)

if len(a) == len(b):
    print("Lists have the same length.")
else:
    print("Lists have different lengths.")

for i in a:
    sum_a += i
print(sum_a)

for i in b:
    sum_b += i
print(sum_b)

if sum_a == sum_b:
    print("The sum of elements in both lists is the same.")
else:
    print("The sum of elements in both lists is different.")

for i in list2:
    if i in list1:
        print(f"{i} occurred in both lists.")
