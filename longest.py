wordlist = input("Enter a list of words separated by spaces: ").split()

a= 0

for i in wordlist:
    if len(i) > a:
        b=i
        a = len(i)

print(f"The length of the longest word in the list is  \t\n{b}:{a}")
