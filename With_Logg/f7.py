import logging

logging.basicConfig(
    filename="f7.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)

def miss(l:list)-> list:
    """
    This is a code to find missing number of a consecutive list
    parameters: l-> list
    return type: m-> integer
    """
    logging.info("Finding missing number")
    n=len(l)+1
    d=n*(n+1)//2
    n=n-1
    sum=0
    for i in range(n):
        sum+=l[i]
    m=d-sum
    logging.info(f"Missing number is :{m}")
    return(m)
f=miss([1,2,3,5,6,7])
print(f,__doc__)

