import logging

logging.basicConfig(
    filename="f1.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def countvow(n:str)->str:
    """
    Count the number of vowels in a given string.
    Parameters:
        s (str): Input string
    Returns:
        int: Total number of vowels in the string.
    """
    logging.info("Counting vowels")
    n2=n.lower()
    v=["a","e","e","i","o","u"]
    l=len(n2)
    c=0
    for i in range(l):
        if(n[i] in v):
            c=c+1
    logging.info(f"The count is: {c}")
    return(c)
r=countvow("hi i am avishek")
print(r,countvow.__doc__, sep="\n")

