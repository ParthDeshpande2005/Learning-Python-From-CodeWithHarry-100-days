#%%
#sets-are unordered collection of data items
#sets are unchangable
s={1,2,3,2,4}
print(s)

info={"parth",18,20.23,False}
print(info)#order kuch bhi print hota hai.

parth={}#->this is empty dictionary
#for making empty set we write
parth1=set()
print(type(parth))
print(type(parth1))

for a in info:
    print(a)



#%%
#sets method
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2)) #used to get union of s1 and s2
print(s1.intersection(s2))#used to get intersection
print(s1.symmetric_difference(s2))#we will get union-intersection
print(s1.difference(s2))#returns the difference of two set
print(s2.difference(s1))

(s1.update(s2))#all extra value of s2 will be added to s1
(s1.intersection_update(s2))#s1 will be updated with intersection value only
(s1.symmetric_difference_update(s2))#update the set with symmetric difference of itself and another set
(s1.difference_update(s2))#removes all element of another set from this set

print(s1.isdisjoint(s2))#return true if two sets have null intersection
print(s1.issuperset(s2))#test whether every element in other is in the set
print(s1.issubset(s2))#test wether every element in set is in other

s1.add(5)#to add single item to set
s1.add(4)

s1.remove(5)#to remove item from set.raise an error if 5 is not in set
s2.discard(10)#to remove item.does not raise an error if item is not in set

removed_item=s1.pop()#removes a random value from set
print(removed_item)

del s1 #used to delete cities
s2.clear()#used to remove all the values form s2



# %%
#Dictionaries -> ordered collection of data items
dic={
    344:"parth",
    56:"shubham",
    12:"abhay",
    1:"ram"
}
print(dic)
print(dic[344])#will give error if not found
print(dic.get(344))
print(dic.get("parth"))#will not give error if not found:will print none.cant find value find only key
print(dic.keys())#gives all the keys
print(dic.values())#gives all the values
print(dic.items())#gives the key,value pair

for key in dic.keys():
    print(dic[key])

for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")



# %%
# Dictionary Methods

dic1={1:90,2:95,3:78,4:100}
dic2={5:60,8:85}

dic1.update(dic2)
dic2.pop(5)#used to pop desired item from dictionary
dic1.popitem()#used to pop last item from dictionary

dic2.clear()#used to clear the dictionary
del dic1[3]#used to delete desired item form dictionary
del dic2 #used to delete the dictionary
