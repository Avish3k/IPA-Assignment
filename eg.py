def evod(n):
    num=n
    e=0
    o=0
    while(num!=0):
        d=num%10
        if(d%2==0):
            e+=1
        elif(d%2!=0):
            o+=1
        num=num//10
    print("no of even are",e)
    print("no of odd are",o)
evod(845236)
evod(7856205412)
