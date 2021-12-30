#Link: https://dmoj.ca/problem/ccc14j1
#Made by Vishwas Puri

s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1+s2+s3 == 180:
    if s1==60 and s2==60 and s3==60:
        print("Equilateral")
    elif s1==s2 or s2==s3 or s1==s3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
