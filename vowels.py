word=input("enter the words:")
vowels=['a','e','i','o','u']
list=[]
for alphabet in word:
    if alphabet in vowels:
        list.append(alphabet)
        print(list)
    
