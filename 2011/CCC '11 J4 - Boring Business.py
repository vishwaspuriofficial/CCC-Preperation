# Link: https://dmoj.ca/problem/ccc11j4
# Made by Vishwas Puri

wellPlan = [[0, -1], [0, -2], [0, -3], [1, -3], [2, -3], [3, -3], [3, -4], [3, -5], [4, -5], [5, -5], [5, -4], [5, -3],
            [6, -3], [7, -3], [7, -4], [7, -5], [7, -6], [7, -7], [6, -7], [5, -7], [4, -7], [3, -7], [2, -7], [1, -7],
            [0, -7], [-1, -7], [-1, -6], [-1, -5]]

while True:
    di, dis = input().split()
    x = 0
    y = 0
    if di == "l":
        x = -1
    elif di == "r":
        x = 1
    elif di == "d":
        y = -1
    elif di == "u":
        y = 1
    else:
        break
    a, b = wellPlan[-1][0] + (x * int(dis)), wellPlan[-1][1] + (y * int(dis))
    print(a, b, end=" ")

    c, d = wellPlan[-1][0], wellPlan[-1][1]
    for i in range(int(dis)):
        c += x
        d += y
        # print([c,d])
        if [c, d] in wellPlan:
            print("DANGER")
            quit()

    print("safe")
    wellPlan.append([a, b])
