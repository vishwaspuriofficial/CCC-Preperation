#Link: https://dmoj.ca/problem/ccc19j1
#Made by Vishwas Puri

count = 0
n1 = int(input())
if n1==8 or n1==9:
    count+=1
n2 = int(input())
n3 = int(input())
if n3==n2:
    count+=1
n4 = int(input())
if n4==8 or n4==9:
    count+=1

if count==3:
    print("ignore")
else:
    print("answer")
















