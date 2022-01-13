a=input()
b=input()
s=""
for i in range(len(a)):
    if (a[i]=='0' and b[i]=='1') or (a[i]=='1' and b[i]=='0'):
        s+='1'
    else:
        s+='0'
print(s)
