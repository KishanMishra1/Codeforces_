def check(n):
    count=0
    k=[4,7,47,74,477,474,744,447,774,747]
    for i in range(0,len(k)):
        if n%k[i]==0:
            count=1
    return count
 
num=int(input())
if (check(num)!=0):
    print("YES")
else:
    print("NO")
