def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


n1 = int(input("enter the number1"))
n2 = int(input("enter the number2"))
result = gcd(n1, n2)
print(result)
