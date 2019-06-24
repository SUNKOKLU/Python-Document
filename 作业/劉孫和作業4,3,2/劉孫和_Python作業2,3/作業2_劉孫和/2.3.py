
# coding: utf-8

# In[8]:


import math
a,b,c=input("Input three edge of a triangle:").split()
a,b,c=int(a),int(b),int(c)
if a>b:
    if a>c:
        aa=a
        bb=b
        cc=c
    else:
        aa=c
        bb=a
        cc=b
else: 
    if c>b:
        aa=c
        bb=a
        cc=b
    else:
        aa=b
        bb=a
        cc=c
        
print("longest edge=",aa)

if aa<bb+cc:
    print("Legal triaangle")
    s=(aa+bb+cc)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("area=",area)        
else:
    print("Illegal triaangle")


        
    
        

