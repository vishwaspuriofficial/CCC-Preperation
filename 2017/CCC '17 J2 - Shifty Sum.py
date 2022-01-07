#Link: https://dmoj.ca/problem/ccc17j2
#Made by Vishwas Puri

# n = int(input())
# k = int(input())
# cnt = n
# for i in range(0,k):
#     n = n * 10
#     cnt += n
#
# print(cnt)

N = str(input())
k = int(input())

count = 0
for i in range(0,k+1):
    num = N+(i*"0")
    count += int(num)

print(count)


