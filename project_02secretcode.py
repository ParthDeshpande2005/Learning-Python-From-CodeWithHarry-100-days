import random
import string
n=[]
def encoding(code):
    for i in range(len(code)):
        if(len(code[i])<3):
            output=code[i][::-1]
            n.append(output)
        else:
            k=code[i][0]
            temp=code[i]+k
            temp1=temp[1:]
            random1=''.join(random.choices(string.ascii_letters,k=3))
            random2=''.join(random.choices(string.ascii_letters,k=3))
            output=random1+temp1+random2
            n.append(output)
    print("Encoded message is: ",*n) #using *n method

def decoding(code):
    for i in range(len(code)):
        if(len(code[i])<3):
            output=code[i][::-1]
            n.append(output)
        else:
            temp=code[i][3:-3]
            temp1=temp[:-1]
            k=temp[len(temp)-1]
            output=k+temp1
            n.append(output)
    print("Decoded message is: "," ".join(n)) #using join method

code=(input("Enter the string: "))
task=int(input("enter 0:Encoding or 1:Decoding: "))
code1=code.split(" ")
if(task==0):
    encoding(code1)
if(task==1):
    decoding(code1)
