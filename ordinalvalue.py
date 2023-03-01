word = str(input("enter the word"))
ordinal_value = []
for i in word:
    ordinal_value.append(ord(i))
print(list(set(ordinal_value)))