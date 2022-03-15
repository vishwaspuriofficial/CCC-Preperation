#Link: https://dmoj.ca/problem/ccc11j2
#Made by Vishwas Puri

seq = [int(input()),int(input())]
a = seq[0] - seq[1]
while a>=0:
    seq.append(a)
    a = seq[-2]-seq[-1]

print(len(seq))
