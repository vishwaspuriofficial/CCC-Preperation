#Link: https://dmoj.ca/problem/ccc12j3
#Made by Vishwas Puri

K = int(input())

code = str(input())

encoded = ""

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(code)):
    S = 3*(i+1)+K
    pos = alphabets.index(code[i])
    letter = pos - S
    if letter < 0:
        letter+=26
    encoded += alphabets[letter]

print(encoded)