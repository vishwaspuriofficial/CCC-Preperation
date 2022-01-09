#Link: https://dmoj.ca/problem/ccc16j1
#Made by Vishwas Puri

count = 0
for i in range(0,6):
    a = input()
    if a == "W":
        count+=1

if 0<count<3:
    print(1)
elif 2<count<5:
    print(2)
elif 4<count<7:
    print(3)
else:
    print(-1)

