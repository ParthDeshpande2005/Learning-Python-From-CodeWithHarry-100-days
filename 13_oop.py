#%%
class student:
    name="parth"
    rollno=23
    branch="SCOPE"
    def info(self):
        print(f"{self.name} is a student from {self.branch}")
#self parameter are reference to current instance of the class
a=student()
b=student()
b.name="ram" 
b.branch="SAI"
print(a.name,a.branch)

a.info()
b.info()



# %%
#constructor->used to initalize values.__init__ is a constructor
class person:
    def __init__(self,name,o):#n,o are arugument we need to give when we call the class
        print("hey I am a person")
        self.name=name
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a=person("harry","developer")#self automatically pass hota hai baki do hame karna padte hai
b=person("parth","HR")
a.info()
b.info()



# %%
#Decorators->used to modify function

def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("thanks for using this function")
    return mfx  
    
@greet
def hello():
    print("hello world")
hello() 
                #or for taking arguments

def greet1(fx):
    def mfx(*args,**kwargs):#*args,**kwargs->way to take argument as tuple and dictionary respectively
        print("Good morning")
        fx(*args,**kwargs)
        print("thanks for using this function")
    return mfx 

def add(a,b):
    print(a+b)
greet1(add)(1,2) #as we dont use @before add



# %%
#Getters and Setters
class Myclass:
    def __init__(self,value):
        self._value=value

    def show(self):
        print(f"Value is {self._value}")
    
    #getter
    @property
    def ten_value(self):
        return 10*self._value

    #setter
    @ten_value.setter
    def ten_value(self,new_value):
        self._value=new_value/10

obj=Myclass(10)
obj.ten_value=67
print(obj.ten_value)
obj.show()



#%%
#Inheretence
class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")

#programmer is a inhereted class of employee
class Programmer(Employee):
    def showlanguage(self):
        print("the default language is python")


e1=Employee("Parth Deshpande",21)
e1.showdetails()
e2=Programmer("Harry",22)
e2.showdetails()

e2.showlanguage()



# %%
#Access Modifiers
"""Type of access specifiers- 
1)public->can we accessed from outside the class
2)private->can be accessed within the class
3)protected->can be accessed within the class and subclass(child class)"""

#1)public
class Employee:
    def __init__(self):
        self.name="Parth"#public representation

a=Employee()
print(a.name)


#2)private 
class student:
    def __init__(self,name):
        self.__name=name #we use double underscore(__) for private

a=student("parth")
#we can access private by->
#we use indirect access
print(a._student__name)#we can access private by (variable._class__name)
#(a.__name) will give error->as cant be accessed directly
print(a.__dir__())#gives all the method we can use in class student


#3)protected
#single underscore(_) is used for protected class.
#it can be accessed directly unlike private.
class father:
    def __init__(self):
        self._name="Abhay"
    def _funname(self):
        return "hello"
class child(father):
    pass

a=father()
print(a._name)
print(a._funname())

b=child()
print(b._name)
print(b._funname())


# %%

# %%
