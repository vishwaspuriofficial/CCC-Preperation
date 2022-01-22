#Link: https://dmoj.ca/problem/ccc19j1
#Made by Vishwas Puri

A3 = int(input())
A2 = int(input())
A1 = int(input())
B3 = int(input())
B2 = int(input())
B1 = int(input())

A = (3*A3)+(2*A2)+A1
B = (3*B3)+(2*B2)+B1

if A>B:
    print("A")
elif B>A:
    print("B")
else:
    print("T")
















