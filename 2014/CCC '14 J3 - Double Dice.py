#Link: https://dmoj.ca/problem/ccc14j3
#Made by Vishwas Puri

rounds = int(input())

A = 100
D = 100

for i in range(0,rounds):
    a,d = map(int, input().split())
    if a>d:
        D-=a
    elif d>a:
        A-=d
print(A)
print(D)
