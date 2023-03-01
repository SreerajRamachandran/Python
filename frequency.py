def fre(n):

    characters = [i for i in n]
    print(characters)
    c = set(characters)
    print(c)
    for i in c:
     if i in characters:
        print(f"{i}={characters.count(i)}")

num = str(input("enter the string"))
fre(num)
