#Link: https://dmoj.ca/problem/ccc13j2
#Made by Vishwas Puri

A = list(input())

letters = ['I','O','S','H','Z','X','N']

count = 0

for i in A:
    if i in letters:
        count+=1

if count == len(A):
    print("YES")
else:
    print("NO")