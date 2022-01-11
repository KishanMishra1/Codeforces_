import string
n=int(input())
s=input() 
alphabet = set(string.ascii_lowercase)

if set(s.lower())>=alphabet:
    print("YES")
else:
    print("NO")
