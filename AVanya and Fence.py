n,h=map(int,input().split())
a=list(map(int,input().split()))
k=1
res=0
for i in range(n):
    if a[i]%h==0:
        res+=a[i]//h
    else:
        res+=(a[i]//h)+1
print(res)
