#Link: https://dmoj.ca/problem/ccc13j2
#Made by Vishwas Puri

T = int(input())
C = int(input())
chores = []
for k in range(0,C):
    chores.append(int(input()))

count = 0
chores.sort()

count2 = 0
for i in chores:
    # print(count)
    if count2+i <=T:
        count += 1
        count2 += i

# for j in range(0, count):
#     count2 += chores[j]
# if count2 > T:
#     count -= 1

print(count)