#Link: https://dmoj.ca/problem/ccc19j1
#Made by Vishwas Puri

N = int(input())

yesterday = list(input())
today = list(input())
count = 0

for i in range(0,N):
    if yesterday[i] == today[i] and yesterday[i]=="C":
        count+=1
print(count)