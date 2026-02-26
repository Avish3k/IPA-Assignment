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
    def acc(self,name,acn,bal):
        self.cname=name
        self.cacn=acn
        self.cbal=bal
    

b1=SBI()
b2=SBI()
b3=SBI()
b4=SBI()

b1.acc("Avishek","40216376916",35000)
b2.acc("Nitesh","49078654567",39000)
b3.acc("Biprarshi","46456723689",25000)
b4.acc("Santanu","49812745629",55000)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b1.cname,b1.cacn,b1.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b2.cname,b2.cacn,b2.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b3.cname,b3.cacn,b3.cbal)
print(SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.cname,b4.cacn,b4.cbal)


logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b1.cname,b1.cacn,b1.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b2.cname,b2.cacn,b2.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b3.cname,b3.cacn,b3.cbal)
logging.info("%s %s %s %s %s %s %s",SBI.name,SBI.branch,SBI.ifsc,SBI.brate,b4.cname,b4.cacn,b4.cbal)
print(__doc__)