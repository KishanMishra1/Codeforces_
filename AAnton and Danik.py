n=int(input())
l=input()
if l.count('A') > l.count('D'):
    print("Anton") 
elif l.count('A')==l.count('D'):
    print("Friendship")
else: 
    print("Danik")
