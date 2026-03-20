
#%%
#Time Module
import time
#time.time()->
def usingfor():
    for i in range(50000):
        print(i)

def usingwhile():
    i=0
    while i<50000:
        i=i+1
        print(i)

init=time.time()
usingfor()
t1=time.time()-init
init=time.time()
usingwhile()
print(time.time()-init)#time taken for while loop.
print(t1) #time taken for for loop



# %%
#time.sleep()

import time
print(4)
time.sleep(3)
print("This is printed after 3 sec")



#%%
#time.strftime()-> function formats a time value as a string,based on a specific format.

import time
t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S" ,t)
print(formatted_time)



# %%
#command line utility 
#is ko padha padega
#concpt samaz lo bas
#import argparse use hota hai.



#%%
#Walrus Operator->assigns values to variable as part of a larger expression.

a=True
print(a:=False)


numbers=[1,2,3,4,5]
while(n:=len(numbers))>0:#har bar n chota hoga
    print(numbers.pop())


#normal way
# foods=list()
# while True:
#     food=input("What food do you like?: ")
#     if food == "quit":
#         break
#     foods.append(food)


#using walrus operator
foods=list()
while(food:=input("what food do you like?: ")) !="quit":
    foods.append(food)



# %%
# Shutil Module

# shutil.copy("src","dist") to copy file
# shutil.copytree("src","dist") to copy folder
# shutil.move("src","dist") to move the file
# os.remove(path) to delete the folder



#%%