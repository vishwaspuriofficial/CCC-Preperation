#Link: https://dmoj.ca/problem/ccc18j3
#Made by Vishwas Puri

def sum(lst):
    count = 0
    for i in lst:
        count +=i
    return count

city = [0]
cities = list(input().split())

for i in cities:
    city.append(int(i))

for i in range(1,len(city)+1):
    for j in range(1,len(city)+1):
        print(abs(sum(city[0:j])-sum(city[0:i])),end=" ")
    print("")