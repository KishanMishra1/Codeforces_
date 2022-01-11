s=input()
i=0
substr ="WUB"
n= len(s)
while i<n:
    if s[i:i+3] == substr:
        i+=3
    else:
        pos =i
        while s[i:i+3] != substr and i<n :
            i+=1
        print(s[pos:i])

                
        
