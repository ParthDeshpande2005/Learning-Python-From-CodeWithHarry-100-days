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
#Class Methods 

class Employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod#->ye method class pe apply hoga naki instance pe
    #without @classmethod ye method instance pe apply hoga
    def changecompany(anything, newcompany):#yaha anithing ke jagha self bhi aa skta hai
        anything.company=newcompany

e1=Employee()
e1.name="Parth"
e1.show()
e1.changecompany("Infinty")
e1.show()
print(Employee.company)

#standard-->
# @classmethod
# def changecompany(cls, newcompany):
#     cls.company = newcompany



# %%
#Class Method as Alternative Constructors

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    #is class method mai string input leke hum instance ka name aur salary return kar rahe hai

#used when the input is some other form like string
string="Parth-7777777"
e1=employee.fromStr(string)
print(e1.name)
print(e1.salary)



# %%

# dir
x=[1,3,2]
print(dir(x))#list ke sare method print hoge
print(x.__add__)

#__dict__
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
p=Person("John",30)
print(p.__dict__)

#help() Method
print(help(Person))



# %%

#Super Keyword
#jab hame child class mai parent class ka method call karna hota hai tab hum super keyword ka use karte hai

class ParentClass:
    def parent_method(self):
        print("This is the parent Method1")

class ChildClass(ParentClass):
    # def parent_method(self):
    #     print("Parth")
    #     super().parent_method()
    def chil_method(self):
        print("This is the child method")
        super().parent_method()

child_obj=ChildClass()
child_obj.chil_method()
child_obj.parent_method()#agar child class mai is nam ka method hoga to parent class wale ko call karega


#constructor ko call karna super ke use se
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang

parth=Programmer("parth","23bce","python")
print(parth.name)
print(parth.id)
print(parth.lang)



# %%
