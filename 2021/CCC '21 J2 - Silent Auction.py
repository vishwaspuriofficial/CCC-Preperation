#Link: https://dmoj.ca/problem/ccc21j2
#Made by Vishwas Puri

N = int(input())
winner = ""
bidHigh = 0

for i in range(0,N):
    name = input()
    bid = int(input())
    if bid > bidHigh:
        bidHigh= bid
        winner = name

print(winner)















