#Link: https://dmoj.ca/problem/ccc12j3
#Made by Vishwas Puri

output = [['*', 'x', '*'],[' ', 'x', 'x'],['*', ' ', '*']]

scale = int(input())

for i in output:
    out = ""
    for j in i:
        out+=scale*j
    out+="\n"
    print(out*scale,end="")