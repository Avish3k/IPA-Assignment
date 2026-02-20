import logging
logging.basicConfig(
    filename="f4.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)
def sortasc(l:list) -> list:
    """
    checks if list is in ascending order
    parameters: l: List
    return type: str messages
    """
    logging.info("checking if sorted in ascending order")
    ln=len(l)
    c=0
    for i in range(ln-1):
        if(l[i]<=l[i+1]):
            c=c+1
        else:
            c=c+0
    if(c==ln-1):
        logging.info("It is in ascending order")
    else:
        logging.info("It is in descending order")
f=sortasc([1,2,3,4,1])
print(f,__doc__)