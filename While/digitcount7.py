n=input("enter number")
s=input("enter number for search")
l=len(n)
c=0
i=0
while(i!=l):
    if(s==n[i]):
        c=c+1
    i=i+1
print(c)