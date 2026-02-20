import logging

logging.basicConfig(
    filename="f5.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)

def strev(n:str) -> str :
    """
    This is a code to return the reverse of a string
    parameters: n string
    return type: messages and string value of n2
    """
    n2=""
    l=len(n)
    l2=[]
    for i in range(-1,-l-1,-1):
        l2.append(n[i])
    n2="".join(l2)
    logging.info(f"reversed string is: {n2}")
    return(n2)

f=strev("Avishek")
print(f,__doc__)

