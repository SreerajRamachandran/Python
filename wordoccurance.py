lines = str(input("enter the line of words"))
words = lines.split()
set = set(words)
count = 0
for i in set:
    if i in words:
        # count+=1
        print(f"{i}={words.count(i)}")
