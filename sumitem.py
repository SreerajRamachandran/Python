def sum(lst):
    if not lst:  # base case
        return 0
    else:
        return lst[0] + sum(lst[1:])  # recursive case


n = int(input("Enter the number of elements in the list: "))
x = []
for i in range(1, n):
    element = int(input(f"Enter element {i}: "))
    print(element)
    x.append(element)

print(sum(x))
