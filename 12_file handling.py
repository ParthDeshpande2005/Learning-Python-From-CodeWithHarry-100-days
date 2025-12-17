#%%
#read a file
f=open('12.1_myfile.txt','r')#(name of file,mode to open file)
print(f) #output=name of file and the mode it is opened in
text=f.read()
print(text)
f.close()

'''
r mode dafault hota hai
r: read mode
w: write mode
a: append mode
rt:read,open as text file
rb:read,open as binary file

'''


#%%
#write in file
f1=open('myfile.txt','w')
f1.write("hello world!")
f1.close()


# %%
#append in file
f2=open('myfile.txt','a')
f2.write("hello using append")
f2.close()


# %%
#using with statement
#with allows us to write the program without closing the file
with open('myfile.txt','r') as f:
    text1=f.read()
    print(text1)


# %%
#readline() method
f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)

# %%
#readline()
f=open('12.1_myfile.txt',"r")
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    print(f"marks of student {i} in Maths is: {m1}")
    print(f"marks of student {i} in SST is: {m2}")
    print(f"marks of student {i} in science is: {m3}")

    
# %%
#writeline() method

f=open('myfile2.txt','w')#this comand can create a new file if that file is not available as we use write
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)#or use f.write(line+'\n') if \n is not included in string
f.close()


# %%
#seek() and tell()
#=>are used to work with file objects and thier positions within a file
with open('12.3_myfile3.txt','r') as f:
    print(type(f))
    f.seek(10) #move to 10th byte in file

    data=f.read(5)#read next 5 line
    print(data)
#seek funcition allows you to move the current position in a file to specific position in file
#the position is specified in byte then you can move forward or backward from current position

    print(f.tell()) #tell() returns the current position within the file



# %%
#truncate()
#this method cant't be used in read'r' mode it must be used in  'w' or 'a' mode

f=open('12.4_myfile4.txt','w')
f.write("hello world")
f.truncate(5) #used to cahnge the size of file.
f.close()

with open('12.4_myfile4.txt','r') as f:
    print(f.read())


