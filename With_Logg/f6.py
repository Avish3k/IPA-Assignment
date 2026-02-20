import logging

logging.basicConfig(
    filename="f6.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)
def remrep(l:list) -> list:
    """
    this code is removing the duplicate numbers while maintaining the order
    parameters: l list 
    return type: l also list
    """
    logging.info("Removing duplicate")
    l2=[]
    for i in range(len(l)):
        if(l[i] not in l2):
            l2.append(l[i])
    l[:]=l2
    return(l)
    logging.info(f"The unique list is: {l}")
f=remrep([1,3,5,3,5,2,5,6,1,4,6,3])
print(f,__doc__)

