#%%
#Static Methods-method jo class se associated hota hai
#is method mai self use nahi hota

class math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n
    
    @staticmethod
    def add(a,b):
        return a+b
    
a=math(5)
print(a.num)
a.addtonum(6)
print(a.num)


#static method ko class ya instance ka nam use kar ke call kar skte hai.
print(a.add(7,3))
print(math.add(7,3))



#%%
#Instance Variables vs Class Variables

class Employee:
    companyName="Apple"#-|->Clas Variables
    noofemployee=0     #-|
    def __init__(self,name):
        self.name=name       #-|
        self.raise_amount=0.2#-|->Instance variables
        Employee.noofemployee +=1
    def showdetails(self):
        print(f"the name of the employee is {self.name} and the raise amount in {self.noofemployee} sized {self.companyName} is {self.raise_amount}.")


emp1=Employee("Parth")
emp1.raise_amount=0.3
emp1.companyName="Infinity"#Parth ko ek instance variable diya hai 
emp1.showdetails()#is mai instance variable show hoga kyu ki uska preference high hai class variable se.


emp2=Employee("Harry")
emp2.showdetails()

print(Employee.companyName)



# %%
