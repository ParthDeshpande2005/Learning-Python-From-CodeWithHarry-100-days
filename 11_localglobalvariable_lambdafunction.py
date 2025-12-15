#%%
#local and global variables
x=10

def my_function():
    global x
    x=5 #this will change the value of global variable x
    y=5 #local variable
    #local variable can't be accessed outside the function

print(x) #will print old value of x
my_function()
print(x) #will print the new value of x
#print(y)-> y can't be accessed outside of my_function


#%%
#lambda function
def double(x):
    return x*2
#this can be writen as :
double=lambda x:x*2
cube=lambda x:x**3
avg=lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
#we can also use a function in side a function
def appl(fx,value):
    return 6+fx(value)

print(appl(cube,2))
       #or
print(appl(lambda x:x**3,2))



