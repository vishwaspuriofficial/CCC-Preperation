#Link: https://dmoj.ca/problem/ccc20j2
#Made by Vishwas Puri

# P = int(input())
# N = int(input())
# R = int(input())
#
# infected = [N]
#
# count = 0
# while sum(infected) < P+1:
#     count += 1
#     infected.append(infected[-1]*R)
#
# print(count)

#Link: https://dmoj.ca/problem/ccc20j2
#Made by Vishwas Puri

P = int(input())
N = int(input())
R = int(input())

a = N
count = 0
while N < P+1:
    count += 1
    b = a*R
    N+=a*R
    a = b

print(count)

