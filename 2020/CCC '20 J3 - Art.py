#Link: https://dmoj.ca/problem/ccc20j3
#Made by Vishwas Puri

N = int(input())
x = []
y = []
for i in range(0,N):
    X, Y = map(int, input().split(","))
    x.append(X)
    y.append(Y)

print(f"{min(x)-1},{min(y)-1}")
print(f"{max(x)+1},{max(y)+1}")














