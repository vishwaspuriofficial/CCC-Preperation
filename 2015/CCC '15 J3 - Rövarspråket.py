#Link: https://dmoj.ca/problem/ccc15j3
#Made by Vishwas Puri

import string

word = str(input())
w = ""
alphabets = list(string.ascii_lowercase)
vowels = [0,4,8,14,20]
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in word:
    w+=i
    ind = alphabets.index(i)
    close = ind
    ans = 0
    a = []
    for i in vowels:
        a=True
        if ind in vowels:
            a = False
            pass
        elif ind>i:
            if ind - i < close:
                close = ind - i
                ans = vowels.index(i)
        elif ind<i:
            if i - ind < close:
                close = i-ind
                ans = vowels.index(i)
    if a == True:
        try:
            if vowels[ans]<=ind:
                w+=alphabets[vowels[ans]]
                w+=alphabets[ind+1]
            elif alphabets[vowels[ans]] == alphabets[ind +1]:
                w += alphabets[vowels[ans]]
                w += alphabets[ind + 2]
            else:
                w += alphabets[vowels[ans]]
                w += alphabets[ind +1]
        except IndexError:
            w += alphabets[ind]


print(w)