
#%%
#list are mutable
list1=[3, 5, 6,"parth",True] 
#     [0][1][2]  [3]   [4]  list index
print(list1)
print(*list1) #used to print without[] and ,
print(list1[:])
print(type(list1))
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

print(len(list1))

print(list1[-3])
print(list1[0:5:2])#3rd argument jump hai.

if 7 in list1:
    print("yes")
else:
    print("false")

#same thing applies for string as well
if "pa" in "parth":
    print("yes")

#list comprehension
list2=[i*2 for i in range(5) if i%2==0] 
print(list2)

#list methods
l=[10,32,13,4,15]
l1=[10,32,13,4,15]
print(l)
l.append(7)#adds 7 in end of list
print(l)

l.sort()#assending order
print(l)
l.sort(reverse=True)#decending order
print(l)

l.reverse()#reverse kar dega
print(l1.index(32))#gives index of first occurance
print(l1.count(32))#used to count number of occurance in list
l.insert(1,977)#insert 977 at index 1
print(l)

#imp!to make copy allways use this copy function or original list get changed 
m=l.copy()

p=[900,100,200]
l1.extend(p)
print(l1)

k=p+l1 #create new list which joined with p and l1
print(k)



#%%
#tuples->immutable
tup=(1,2,3,3,3,4,5)
print(type(tup),tup)
nottup=(1)
print(type(nottup),nottup)
istup=(1,) #use comma to define as tuple
print(type(istup),istup)

print(len(tup))
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[-1])
print(tup[-2])
#indexing in tuple are same as list.
if 5 in tup:
    print("5 is in tuple.")

tup2=tup[1:4] #new tupple is made
print(tup2)

#we can't make changes to tuple so we change tuple to a list then do changes and change then temp list to tuple again
countries=("spain","italy","India","england")
temp=list(countries)
temp.append("russia")
temp.pop(3)
temp[2]="finland"
countries=tuple(temp)
print(countries)
#however we can join two tupples to make new.

print(tup.count(3))

print(tup.index(3,2,6))#find the index of 3 in [2,6] range



#%%
#list inside of a list indexing
a=[[1,2,3],[2,5,6],'parth',35]
print(a[1][1])
print(a[0][0])
print(a[2])
print(a[0][2])
print(a[0])


# %%
#map,filter and reduce take arguments as(function,itertable)
#iterable object can be any list,tupple,or any other iterable object
# Map
def cube(x):
    return x*x*x

l=[1,2,3,4,5,6]
newl=[]
for i in l:
    newl.append(cube(i))
print(newl)

                  #or

#using map function
newl2=list(map(cube,l))
print(newl2)
#using lambda
newl2=list(map(lambda x:x*x*x,l))
#list is used to convert to list or we will get map object.



# %%
#Filter
l=[23,5,1,8,12]
newl=list(filter(lambda x:x>10,l))#x greater than 10 return hoga.
print(newl)



# %%
# Reduce
#reduce ko import karna padta hai
from functools import reduce
numbers=[12,4,3,5,13,18,1]
sum=reduce(lambda x,y:x+y,numbers)
print(sum)

