#%%
a=(input("enter the number:"))
print(f"Multiplication table of {a} is:")

try:
    for i in range(1,11):
        print(f"{int(a)}X{i}={int(a)*i}")   

except:#prints below text when ever error occurs
    print("Invalid input")
print("some imp lines of code")


b=(input("enter the number:"))
print(f"Multiplication table of {b} is:")

try:
    for i in range(1,11):
        print(f"{int(b)}X{i}={int(b)*i}")
except Exception as e:#stores the exception in e
    print(e)#prints the exception
print("some imp lines of code")



# %%
#handling specific error

try:
    num=int(input("enter a number"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("value error occured")
except IndexError:
    print("Index error occured")



# %%
#Finally Clause
def func1():
    try:
        l=[1,2,3,4,5]
        i=int(input("Enter the value of index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    #even if we return still finally will get executed
    #finally har bar excute hoga error aye ya na aye
    finally:
        print("I am always executed")
    print("I am not always executed")#this line is dead code as there is return statement used in above part
x=func1()
print(x)



# %%
#Raise custom error->
a=int((input("enter a number between 5 and 9: ")))

if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")
#we can raise custom error using raise keyword



# %%
#Raise custom error Quick quiz->
a=(input("enter quit: "))
try:
    int(a)!=int
except ValueError:
    if(a=="quit"):
        print("exit the program")
    if(a!="quit"):
        raise ValueError("invalid input")
    
else:
    if(int(a)<5 or int(a)>9):
        raise ValueError("value should be between 5 and 9") 


