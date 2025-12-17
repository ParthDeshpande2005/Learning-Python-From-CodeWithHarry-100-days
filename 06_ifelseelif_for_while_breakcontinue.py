#%%
#if else elif
#<,>,<=,>=,==,!= (condition statement)
a=int(input("enter your age: "))
if (a>18):
    print("you can drive")                        #-|
elif a==18 :#can be used without brackets also    # |->or use (a>=18)
    print("you can drive")                        #-|
else:
    print("you cannot drive")
print("thank you")#out of the loop



#%%
#nested if else->we can use if else staement in if else
b=int(input("enter your age: "))
if(b>=18):
    print("you can drive.")
    if(b==18):
        print("must have a driving licence.")
else:
    print("you cant drive.")
print("thank you")



#%%
#short hand if else->hard to read and understand,good for small if else
'''
if condition:
    result=value_if_true
else:
    result=value_if_false
'''
#result=value_if_true if condition else value_if_false

a=30000
b=26584
print("A") if a>b else print("=") if a==b else print("B")
'''
if a>b:
    print(A)
else:
    if a==b:
        print(=)
    else:
        print(B)
'''

c=9 if a>b else 0
print(c)



# %%
#match case
x=int(input("enter x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is 4")
    case _ if x>=90:
        print("x is greater or equal to 90")
    case _:
        print("value of x is:",x)



# %%
#For
for i in range(2,8):  #->8is not included
    print(i)

for i in range (3):
    print(i)

for i in range(0,8,2):#->third parameter is step used to skip the numbers.
    print(i)

name="Parth"
for i in name:
    print(i)
    if(i=="P"):
        print("first letter")

colour=["red","black","yellow"]
for i in colour:
    print(i)



#%%
#using for and while with else
for i in range(5):
    print(i)
else:
    print("done")#else execute hoga kyu ki for loop complete hoga

for i in []:
    print(i)
else:
    print("no value for i")#else execute hoga kyuki for loop chalu nahi hoga

for i in range(6):
    print(i)
    if i==4:
        break
else:
    print("sorry no i")#else execute nahi hoga kyu ki for loop break hoga

i=0
while i<7:
    print(i)
    i=i+1
    if i==4:
        break
else:
    print("while ka else")#else execute nahi hoga kyu ki while loop break hoga

#else gets printed if loops complete or does not get started.



# %%
#while loop
i=0
while(i<=3):
    print(i)
    i=i+1

print("")

#we can use else with while once while condition is false we enter else statement
count=5
while(count>0):
    print(count)
    count=count-1
else:print("inside else")



#%%
#do while loop
i=0
while True:
    print(i)
    i=i+10
    if(i%100==0):
        break



# %%
for i in range(1,12):
    if(i==5):
        print("skip")
        continue
    print("5 X",i,"=",5*(i+1))
    if(i==10):
        break



# %%
