import logging

logging.basicConfig(
    filename="SBI.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("The code for oops")
class SBI:
    """
    This code is for banking applications
    class : SBI
    def parameters: name:str acn:str bal:int
    return: bank: name,branch,ifsc,rating,  -> individual: name,account-number,balance
    """
    name="State Bank of india"
    branch="Gandhinagar"
    ifsc="SBIN0014542"
    brate=4 
    def acc(self,name,acn,bal,pin):
        self.name=name
        self.acn=acn
        self.bal=bal
        self.pin=pin
    def display(self):
        print(SBI.name,SBI.branch,self.name,self.acn,self.bal)

    def withdraw(self,pin,withd): 
        if pin != self.pin:
            print("Wrong PIN")
        elif withd > self.bal:
            print("Insufficient Balance")
        else:
            self.bal -= withd
            print("Withdraw Successful")
            print("Current Balance:", self.bal)
            
    def dep(self,depo):
        if(depo>0):
            self.bal+=depo
            print("current balance is",self.bal)
b1=SBI()
for i in range(1):
    n=input("enter name")
    a=input("enter ac no.")
    b=int(input("enter balance"))
    p=int(input("enter pin"))
    b1.acc(n,a,b,p)

while(True):
    print("enter 1 for display, enter 2 for  withdraw, 3 for deposit, 4 exit")
    c=int(input())
    if(c==1):
        b1.display()
    elif(c==2):
        p=int(input("enter pin"))
        n=int(input("enter number for withdraw"))
        b1.withdraw(p,n)
    elif(c==3):
        n=int(input("enter amount"))
        b1.dep(n)
    elif(c==4):
        print("Thank you")
        break
    else:
        print("wrong choice")

    

'''b1=SBI()
b2=SBI()
b3=SBI()
b4=SBI()

b1.acc("Avishek","40216342067",35000,1234)
b2.acc("Nitesh","49078654567",39000,1234)
b3.acc("Biprarshi","46456723689",25000,1234)
b4.acc("Santanu","49812745629",55000,1234)

logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b1.name,b1.acn,b1.bal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b2.name,b2.acn,b2.bal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b3.name,b3.acn,b3.bal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.name,b4.acn,b4.bal)
print(__doc__)'''