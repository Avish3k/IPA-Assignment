class person():
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def display(self):
      print(self.name,self.age, end = " ")

class stu(person):
  def __init__(self,name,age,roll):
    super().__init__(name,age)
    self.roll=roll
  def display(self):
    super().display()
    print(self.roll, end = " ")

class academic():
  def __init__(self,course=None,cgpa=None):
    self.course=course
    self.cgpa=cgpa
  def display(self):
    print(self.course,self.cgpa, end = " ")

class sports():
  def __init__(self,sname=None,level=None):
    self.sname=sname
    self.level=level
  def display(self):
    print(self.sname,self.level,end=" ")

class allrounder(stu,academic,sports):
    def __init__(self,name,age,roll,is_academic=False,is_sports=False,course=None,cgpa=None,sname=None,level=None):
        super().__init__(name,age,roll)
        self.is_academic=is_academic
        self.is_sports=is_sports
        if self.is_academic:
            academic.__init__(self,course,cgpa)
        if self.is_sports:
            sports.__init__(self,sname,level)
        if self.is_academic and self.is_sports:
            academic.__init__(self,course,cgpa)
            sports.__init__(self,sname,level)

    def display(self):
        super().display()
        if self.is_academic==True and self.is_sports==False:
            print(self.course,self.cgpa,end = " ")
        elif self.is_sports==True and self.is_academic==False:
            print(self.sname,self.level,end = " ")
        elif self.is_academic and self.is_sports:
            print(self.course,self.cgpa,end = " ")
            print(self.sname,self.level,end = " ")



    

nr=int(input("enter no of students"))
for i in range(0,nr):
    print("1 for academics, 2 for sports, 3 for allrounder, 4 for exit: ")
    ch=int(input())
    if(ch==1):
        n=input("enter name: ")
        a=int(input("enter age: "))
        r=int(input("enter roll: "))
        b=True
        cr=input("enter course: ")
        cg=int(input("enter cgpa: "))
        s1=allrounder(n,a,r,is_academic=b,course=cr,cgpa=cg)
        s1.display()
    elif(ch==2):
        n=input("enter name: ")
        a=int(input("enter age: "))
        r=int(input("enter roll: "))
        b=True
        sn=input("enter sports name: ")
        l=input("enter sports level: ")
        s1=allrounder(n,a,r,is_sports=b,sname=sn,level=l)
        s1.display()
    elif(ch==3):
        n=input("enter name: ")
        a=int(input("enter age: "))
        r=int(input("enter roll: "))
        b=True
        b2=True
        cr=input("enter course: ")
        cg=float(input("enter cgpa: "))
        sn=input("enter sports name: ")
        l=input("enter sports level")
        s1=allrounder(n,a,r,b,b2,cr,cg,sn,l)
        s1.display()
    elif(ch==4):
       print("Thank You")
       break
    else:
        print("Wrong choice")
       
    
   
'''s1=allrounder("Avi",22,9,True,True,"MCA",8.40,"Cricket","State")
s1.display()
print("\n")
s2=allrounder("Avi",22,9,is_academic=True,course="MCA",cgpa=8.40)
s2.display()
print("\n")
s3=allrounder("Avi",22,9,is_sports=True,sname="Cricket",level="State")
s3.display()
print("\n")
'''
