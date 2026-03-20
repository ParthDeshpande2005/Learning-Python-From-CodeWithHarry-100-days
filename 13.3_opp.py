#%%
# Magic/Dunder Method in Python
class Employee():
    def __init__(self,name):
        self.name= name
    
    def __len__(self):
        i=0
        for c in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"The name of the employee is {self.name} str"

    def __repr__(self):
        return f"The name of the employee is {self.name} repr"

    def __call__(self):
        print("hey")

e=Employee("Parth")
print(e.name)
print(str(e))# sirf print(e) bhi karne se str method run hoga.
print(repr(e))
print(len(e))
e()#call method



# %%
# Method Overriding in Python->
class Shape:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def area(self):
        return self.x*self.y

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
        super().__init__(radius,radius)
    def area(self):#overriding the area method here.
        return 3.14*super().area()

rec=Shape(3,5)
print(rec.area())

cir=Circle(5)
print(cir.area())



# %%
#Operator Overloading->
class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i} i + {self.j} j + {self.k} k"

    def __add__(self,x):# add operator "+" ko overload kar rahe hai hum yaha.
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)


v1=Vector(3,5,6)
print(v1)

v2=Vector(1,2,9)
print(v2)

print(v1+v2)
print(type(v1+v2))



# %%
# Single Inheritance

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    
    def make_sound(self):
        print("Sound made by the Animal")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def make_sound(self):
        print("bark!!")

d=Dog("Dog","labra")
d.make_sound()

a=Animal("cat","egpytian")
a.make_sound()



# %%
#Multiple Inheritance-> ek class 2 or more class se inherit hoga.

class Employee:
    def __init__(self,name):
        self.name=name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance=dance

    def show(self):
        print(f"The Dance is {self.dance}")

class DancerEmployee(Employee,Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name

o=DancerEmployee("breakdance","Parth")
print(o.name)
print(o.dance)
o.show()#upar ham ne DancerEmployee(Employee,Dancer)
#likha hai matlab Employee pehle likha hai to Employe ka show method call hoga.
#agr hum pehle Dancer likhte to Dancer ka show method atta
print(DancerEmployee.mro())#method resolution order-> we can know the order of preference of classes



#%%
#Multiplelevel Inheritance->

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Specise: {self.species}")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed: {self.breed}")

class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriver")
        self.color= color
    
    def show_details(self):
        Dog.show_details(self)
        print(f"Color: {self.color}")

o=GoldenRetriver("tommy","Black")
o.show_details()

print("")
z=Dog("tommy","Black")
z.show_details()




# %%
#Hybrid Inhertitance->
class Baseclass:
    pass

class Derived1(Baseclass):
    pass

class Derived2(Baseclass):
    pass

class Deriverd3(Derived1,Derived2):
    pass



#%%
#Hierachical Inheritance->
class Baseclass:
    pass

class D1(Baseclass):
    pass

class D2(Baseclass):
    pass

class D3(D1):
    pass



#%%