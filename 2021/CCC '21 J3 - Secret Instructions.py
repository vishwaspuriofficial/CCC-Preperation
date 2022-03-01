#Link: https://dmoj.ca/problem/ccc21j2
#Made by Vishwas Puri
#Link:https://dmoj.ca/problem/ccc21j3

previous = ""
while True:
    line = input().strip()
    if line == "99999":
        break
    dir = int(line[0]) +int(line[1])
    if dir%2 != 0:
        dir = "right"
    elif dir%2 == 0:
        dir = "left"
    else:
        dir = previous

    print(dir,line[2:])
    previous = dir
