#Link: https://dmoj.ca/problem/ccc14j2
#Made by Vishwas Puri

V = int(input())
a = list(input())

A = 0
B = 0

for i in a:
    if i == "A":
        A+=1
    elif i == "B":
        B+=1

if A==B:
    print("Tie")
elif A>B:
    print("A")
else:
    print("B")