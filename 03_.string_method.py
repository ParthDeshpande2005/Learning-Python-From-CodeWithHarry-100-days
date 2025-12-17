#%%
#strings
a="parth" 
print(len(a))
b='deshpande' #<--also a string using ''
word="he said,\"I want to eat an apple.\" "#use of escape sequence characters by using back slash
                 #or          
word1='he said,"I want to eat an apple."'#using '' to define string
print(word)
print(word1)

#for multiline string
word2='''hello
again'''
     #or
word3="""hello
hello"""

print(word2)#hello and again gets printed in different line same output for word3

print(a[0])
print(a[2])
#print(a[5])<--indexerror as nothing on five index

print("lets use for loop: ")
for character in a:
    print(character)



#%%
#string slicing
name="Parth Deshpande" 
print(len(name))
print(name[0:5]) #<--does not print 5th index
print(name[:])
print(name[1:])
print(name[:5])
print(name[3:12])
print(name[-1])
#negative slicing
print(name[0:-4]) #-->print(name[0:len(name)-4])
print(name[-5:-2]) #-->print(name[len(name)-5:len(name)-2])



#%%
#strings are immutable
a="!!Parth!!! PARTH!!!"
print(len(a))
print(a)
print(a.upper()) #we create a new string
print(a.lower()) #no change can be done to original string
print(a.rstrip("!")) #rstrip is used to remove trailing character.
                     #only remove trailing character from behind and not from leading.
print(a.replace("Parth","Ram"))
#split is important to make list of a string
print(a.split(" ")) #makes list after each space
print(a.capitalize()) #used to capitlaize
print(a.count("!")) #for counting 
print(a.center(50))#used to move titel towards center
                   #add space such that last letter moves to 50.

#endswith--> gives true and flase according to question
b="Hello Guys welcome to India"
print(b.endswith("a"))
print(b.endswith("lo",2,5)) #<-taking range to check endswith

print(b.find("hello")) #will find the first apperence of Hello
#find will give output as -1 if string is not found.
print(b.index("to")) #index will give error of string is not found

c="Parth00"
print(c.isalnum())#check if the string only consist of a-z,A-Z,0-9
print(c.isalpha())#only check for A-Z,a-z
print(b.isalpha())#space is also consider false

#islower() <--to check all character are in lower.
#isupper() <--to check all character are in upper.
#isprintable() <--to check all character are printable
    #example of non printable character \n
#isspace() <--if string contain only space(may be given by spacebar or tab)
#istitle() <--to check first letter of each word is capital.
#startswith() <--to check if string starts with the desirable alphabet
#swapcase() <--convert uppercase to lower and lower to upper
#title() <--convert first letter of word to capital.



    


# %%
