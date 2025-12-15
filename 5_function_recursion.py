#%%
def calculateGmean(a,b):
    mean=(a*b)/(a+b)
    return mean #using return statement
#if nothing is return none is returned.
#if multiple return are used the first one is considered

def isgreater(a,b):
    if(a>b):
        print(a,"is greater than",b)
    elif(b>a):
        print(b,"is greater than",a)
    else:
        print(a,"is equal to",b)

def islesser(a,b):
    pass
#pass is used to skip the part without any error

a=7
b=8
a=calculateGmean(a,b)
print(a)
isgreater(a,b)
islesser(a,b)#pass hojayega so no output



#%%
#using default arguments
def defaultarg(a=2,b=3):
    pass

defaultarg()#will take default value of a and b.
defaultarg(a=3,b=9)#will take new value of a and b
defaultarg(5)#only new value of a will be taken and default of b
defaultarg(b=3)#a=default and b=new value


#variable-length arguments
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:",sum/len(numbers))

average(4,5,2,7,8)

#can also be used to take string inputs:
def add(*string):
    sum2=0
    for i in string:
        sum2=sum2+1
    print(sum2)

add("parth","abhay","deshpande")

#dictionry argument
def name(**name):# **is used to take dictionary inputs.
    pass



#%%
#Recursion factorial code
#my code 
def factorial(n):
    if(n<0):
        a="invalid number"
    if(n>0):
        a=n*factorial(n-1)
    if(n==0):
        a=1
    return a

answer=factorial(5)
print(answer)

#harry code better hai kyu ki har bar 0 ko check nahi karega
def fac(k):
    if(k==0 or k==1):#here there is no need to write k==0 as that condition will never be checked.
        return 1
    else:
        return k * fac(k-1)
print(fac(4))



# %%
#fibonacci code
def fibonacci(n):
        if(n==0):
            return 0
        if(n==1):
            return 1   
        else:
            return(fibonacci(n-1)+fibonacci(n-2))

def fn(n):
    for i in range(n):
        print(fibonacci(i))
fn(7)



# %%
#Enumerate Function
"""The enumerate() function in Python is used to iterate over a sequence while keeping 
track of the index of each item. It returns an iterator that produces index-value pairs."""
fruits=["apple","bannana","mango"]
for index,fruit in enumerate(fruits):
    print(index, fruit)

fruits=["apple","bannana","mango"]
for v in enumerate(fruits,start=1):#start is used to start from a desired value
    print(v)#output will be tupple



# %%
a=[]
for i in range(2):
    a.append(int(input()))
print(a)



# %%
