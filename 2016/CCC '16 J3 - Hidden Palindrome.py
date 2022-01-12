#Link: https://dmoj.ca/problem/ccc16j3
#Made by Vishwas Puri

word = input()
count = []
for i in range(0,len(word)):
    for j in range(1,len(word)+1):
        a = word[i:j]
        aRev = a[::-1]
        if a == aRev:
            count.append(len(a))

print(max(count))
