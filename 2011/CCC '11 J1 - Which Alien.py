#Link: https://dmoj.ca/problem/ccc11j1
#Made by Vishwas Puri

a = int(input())
e = int(input())

if a>3 and e<5:
    print("TroyMartian")
if a<7 and e>2:
    print("VladSaturnian")
if a<3 and e<4:
    print("GraemeMercurian")
