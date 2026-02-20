import logging

logging.basicConfig(
    filename="f3.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)

def seclarge(n:list)->list:
    """
    gives the second largest number in the list.
    Parameters:
        n (list): Input List
    Returns:
        int: The Second largest string.
    """
    l=len(n)
    for i in range(l):
        for j in range(l):
            if(n[i]<=n[j]):
                n[i], n[j] = n[j], n[i]
    logging.info(f"the second largest no. is{n[l-2]}")
    

s=[2,5,7,2,2,5,3,6,2,8,2,2]
f=seclarge(s)
print(f,seclarge.__doc__)    