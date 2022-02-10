# Link: https://dmoj.ca/problem/ccc20j4
# Made by Vishwas Puri

T = str(input())
S = str(input())

x = False
for i in range(len(S)):
    if S[i:]+S[:i] in T:
        x=True
        break

if x == False:
    print("no")
else:
    print("yes")