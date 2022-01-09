#Link: https://dmoj.ca/problem/ccc17j3
#Made by Vishwas Puri

a,b = map(int, input().split())

c,d = map(int, input().split())

t = int(input())


dis = abs(a - c) + abs(b - d)
if (dis <= t and not((t - dis) % 2)):
    print("Y")
else:
    print("N")

