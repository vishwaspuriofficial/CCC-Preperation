#Link: https://dmoj.ca/problem/ccc12j1
#Made by Vishwas Puri

depths = []
d = []
for i in range(4):
    a = int(input())
    depths.append(a)
    d.append(a)

if depths.count(depths[0]) == 4:
    print("Fish At Constant Depth")
elif sorted(d) == depths:
    print("Fish Rising")
elif d.sort(reverse=True) == depths:
    print("Fish Diving")
else:
    print("No Fish")
