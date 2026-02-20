a=3
u="avi"
p=1234
i=3
c=0
while(True):
    u2=input("enter username")
    if(u==u2):
        while(i!=0):
            n=int(input("enter pin"))
            if(n==p):
                print("login success")
                break
            elif(n!=p and i!=0):
                print(i-1, "attemp left")
                i=i-1
            elif(i==0):
                print("login failed")
        break
    else:
        print("wrong username")








    '''
    u2=input("enter username")
    n=int(input("enter pin"))
    if(n==p and u==u2):
        print("login success")
    elif(n!=p or u!=u2 and i!=0):
        print(i-1, "attemp left")
    elif(i==0):
        print("login failed")
    i=i-1'''



