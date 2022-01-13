n=int(input())
k=[]
for i in range(n):
    if i%2==0:
        k.append("I hate")
    else:
        k.append("I love")
    if i!=n-1:
        k.append("that")
    else:
        k.append("it")
print(" ".join(k))
