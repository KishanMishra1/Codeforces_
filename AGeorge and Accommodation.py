count=0
for _ in range(int(input())):
    a=list(map(int,input().split()))
    if a[0]<=a[1] and a[1]-a[0]>=2:
        count+=1
print(count)
