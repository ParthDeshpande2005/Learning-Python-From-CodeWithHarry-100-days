s="abcd"
p="d*"

z=len(s)-1
y=len(p)-1

def refun(c,d):
    if(s[c]==p[d] or p[d]=="."):
        if(c==z and d==y):
            return True
        elif(d!=y and c==z):
                if(p[d+1]=="*"):
                    return refun(c,d+1)
                else:
                    return False
        elif(c!=z and d==y):
            if(p[d]=="*"):
                return(c+1,d)
            else:
                return False
        else:
            if(c!=z and d!=y ):
                return refun(c+1,d+1)
            else:
                return False
    elif(p[d]=="*" ): 
        if(s[c]==p[d-1] or p[d-1]=="."):
            if(c==z and d==y):
                return True
            elif(c!=z and d==y):
                return refun(c+1,d)
            elif(d!=y and c==z):
                return refun(c,d+1)
            else:
                return refun(c+1,d)
        else:
            if(d!=y):
                return refun(c,d+1)
            else:
                return False
    else:
        if("*" in p[d:]):
            d=p.index("*",d,len(p))
            return refun(c,d)
        else:
            return False
refun(0,0)

a=refun(c,d)
print(a)

# %%
p="abacdefa"
a=p.index("a",1,len(s))
print(a)