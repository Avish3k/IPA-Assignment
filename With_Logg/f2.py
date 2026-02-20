import logging

logging.basicConfig(
    filename="f2.log",
    level=logging.INFO,
    format="%(asctime)s -%(levelname)s -%(message)s"
)
def freq(s:str)->str:
    """
    Count the frequency of each char.
    Parameters:
        s (str): Input string
    Returns:
        int,str: Returns frequency of a character.
    """
    c=0
    s2=s.lower()
    l=[]
    for i in range(len(s2)):
        if(s2[i] not in l):
            l.append(s2[i])
    ln=len(l)
    for i in range(ln):
        for j in range(len(s2)):
            if(l[i] == s2[j]):
                c=c+1
            else:
                c=c+0
        logging.info(f"the frequency of {l[i]} is {c} ")
        c=0
s="22225336992454322"
f=freq(s)
print(f,freq.__doc__)