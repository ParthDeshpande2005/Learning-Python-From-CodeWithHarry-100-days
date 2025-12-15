# #%% is used to make cells in .py type file
#%%
#data type
a=2 
b="parth" 
c=6.34
d=None
e=complex(5,3)
f=True
print(a,b)
print(a+c)
print(type(a))
print(type(b))
print(type(c))
print(type(d)) 
print(type(e))
print(type(f)) 



#%%
#operators-->
a=10
b=3
print(a+b)  #addition
print(a-b)  #subtraction
print(a*b)  #multiplication
print(a/b)  #normal division operator
print(a**b) #exponential 
print(a%b)  #gives remainder only
print(a//b) #gives the intiger part of division and not the point part



#%%
#typecasting-we decide what is type of variable.
a="1" 
b="2" 
print(a+b)
print(int(a)+int(b))
'''c="parth"
d=2
print(c+d) this will give type error because c 
is string and d is integer.'''
e=1.5
f=24
print(f*e) #here python automatically convert int to float



#%%
#Taking input
a=input("enter your name: ")
print("my name is", a)



# %%
x=int(input("enter first number: "))
y=int(input("enter second number: "))
print("the sum is: ",x+y)



#%%
#is and ==
a=4
b="4"
print(a is b)#checks exact location of object in memory
print(a==b)#checks value
print("")
""" python will create differnt location for same list as the are iterable"""
a1=[1,2,3]
b1=[1,2,3]
print(a1 is b1)
print(a1==b1)
# print("")
'''python wont create different memory location for 
non iterable objects such as none,string,intiger etc'''
a2=3
b2=3
print("\n",a2 is b2,sep="")#we can use \n like this, we use sep="" because without it there will be space left.
print(a2==b2)



# %%
# we use print("") instead of print("\n") as \n is will leave two lines.
#one line of print and one line of \n


#%%
#logical oprator
print(5 and 0) #output=0
print(5 and 6) #output=6 in this case both are true hence it return 2nd operator
print(0 and 6) #output=0
#python allways check first operator before second it return first if it is false(like-0,none,false).
#else it return the second operator.



# %%
