#Link: https://dmoj.ca/problem/ccc16j2
#Made by Vishwas Puri

a = []

for i in range(0,4):
    b = list(input().split())
    a.append(b)

sum = []
for j in range(0,4):
    count = 0
    for k in a[j]:
        count+=int(k)
    sum.append(count)

for l in range(0,4):
    count = 0
    for m in a:
        count+=int(m[l])
    sum.append(count)

check = 0
for n in sum:
    if n == sum[0]:
        check+=1

if check == len(sum):
    print("magic")
else:
    print("not magic")