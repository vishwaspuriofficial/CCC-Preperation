#Link: https://dmoj.ca/problem/ccc12j1
#Made by Vishwas Puri

speed = int(input())
recorded = int(input())

if recorded <= speed:
    print("Congratulations, you are within the speed limit!")
else:
    over = recorded - speed
    if over < 21:
        F = 100
    elif  20 < over < 31:
        F = 270
    else:
        F = 500
    print(f"You are speeding and your fine is ${F}.")