import logging
'''
logging.basicConfig(
    filename="SBI2.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("The code for oops")
'''

class SBI:
    #"""
    #This code is for banking applications
    #class : SBI
    #def parameters: name:str acn:str bal:int
    #return: bank: name,branch,ifsc,rating,  -> individual: name,account-number,balance
    #"""
    name="State Bank of india"
    branch="Gandhinagar"
    ifsc="SBIN0014542"
    brate=4 
    def __init__(self,name,acn,bal):
        self.name=name
        self.acn=acn
        self.bal=bal
    def display(self):
        print(self.name,self.acn,self.bal)
    @classmethod
    def changebr(cls,br):
        cls.branch=br

b1=SBI("Avishek","40216376916",35000)
b2=SBI("Nitesh","49078654567",39000)
b3=SBI("Biprarshi","46456723689",25000)
b4=SBI("Santanu","49812745629",55000)

'''print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b1.cname,b1.cacn,b1.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b2.cname,b2.cacn,b2.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b3.cname,b3.cacn,b3.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.cname,b4.cacn,b4.cbal)'''
#b4.display()
SBI.changebr("Asansol")
b4.display()
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.name,b4.acn,b4.bal)

'''logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b1.cname,b1.cacn,b1.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b2.cname,b2.cacn,b2.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b3.cname,b3.cacn,b3.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.cname,b4.cacn,b4.cbal)
print(__doc__)'''