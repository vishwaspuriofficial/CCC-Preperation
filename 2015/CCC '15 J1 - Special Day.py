#Link: https://dmoj.ca/problem/5
#Made by Vishwas Puri

month = int(input())
date = int(input())

if month < 2:
    print("Before")
elif month == 2:
    if date < 18 :
        print("Before")
    elif date == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")
