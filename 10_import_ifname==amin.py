#%%
#import
import math
math.floor(4.2323)



#%%
#from is used to get desirable function from math
from math import sqrt,pi
result=sqrt(9)*pi
print(result)



#%%
# * is used to import all the function from math
# You can use functions without prefixing with math.
from math import *
print(sqrt(25))



#%%
# 'as' keyword is used to get in short
import math as m
result=m.sqrt(9)*m.pi
print(result)


#%%
import math
print(dir(math))#used to print all the function in math


# %%
from test import *
print(parth)
# welcome()

# %%
import test as T
T.welcome()

# %%
import test
#print(__name__) will get printed which is test
