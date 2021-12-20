n=int(input())
t=list(map(int,input().split()))
sumf=0
suml=0
count=0
t=sorted(t)
 
for i in t:
    sumf+=i
for i in t[::-1]:
    suml+=i
    count+=1
    if suml >(sumf/2):
        break
print(count)
