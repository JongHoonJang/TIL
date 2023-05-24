N = input()
word = ['M','O','B', 'I', 'S']
res = 'NO'
for i in N:
    if i in word:
        word.remove(i)
if len(word) == 0:
    res = 'YES'
print(res)