n=int(input("enter a number"))
num=n
sum=0
while(num!=0):
    d=num%10
    sum=(sum*10)+d
    num=num//10
if(sum==n):
    print("pallindrome")
else:
    print("not pallindrome")