#Link: https://dmoj.ca/problem/ccc15j2
#Made by Vishwas Puri

happy = 0
sad = 0

a = list(input())
for i in range(0,len(a)):
    if a[i] == ":":
        if a[i+1] == "-":
            if a[i+2] == ")":
                happy += 1
            elif a[i+2] == "(":
                sad+=1

if happy==0 and sad==0:
    print("none")
elif happy==sad:
    print("unsure")
elif happy>sad:
    print("happy")
else:
    print("sad")