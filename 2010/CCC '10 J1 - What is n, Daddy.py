#Link: https://dmoj.ca/problem/ccc10j1
#Made by Vishwas Puri

a = int(input())

options = []
b = 0
while b<6:
    c = [b, a - b]
    print(c, options, c[::-1])
    if c not in options or c[::-1] not in options:
        options.append(c)
        b+=1
    else:
        break

print(options)
print(len(options))
