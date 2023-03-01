def factors(n):
    a = []
    for i in range(1, n):
        if n % i == 0:
            print(i)
            a.append(i)
    return a


num = int(input("enter  the number"))
print(f"factors of{num}are",factors(num))
