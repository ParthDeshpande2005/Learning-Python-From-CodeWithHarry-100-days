#%%
#fstring

#method 1
letter="hey my name is {0} and I am from {1}."#number inside{} shows where the input will be placed,not giving number will simply put input in serial order.    
country="India" 
name="Parth"
print(letter.format(name,country))

#method 2
print(f"hey my name is {name} and I am from {country}.")
print(f"we use f-string like this: hey my name is {{name}} and I am from {{country}}")
#double {{}} use karne se single {} print hoga
price=49.909991
txt=f"For only {price:.2f} dollars!" #.2f convert decimal to 2 decimal places
print(txt)

print(type(f"{2*30}")) #automatically string bana dega



#%%
#docstring->used right after defining function,method,class or module.
def square(n):
    '''takes in a number n,return the square of n'''
    #above line is not a comment its docstring
    #docstring are used right after def above the body of function,class,module
    print(n**2)
square(5)
print(square.__doc__)



# %%
import this
#poem of python

