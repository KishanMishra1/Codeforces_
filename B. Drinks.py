n=float(input())
l=list(map(int,input().split()))
s=0.0
for i in l:
    s+=float(i)/n
print("{:.12f}".format(s))
 
