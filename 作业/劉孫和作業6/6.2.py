
# coding: utf-8

# In[1]:


import math 
def gcdAll(listData):
    number=listData[0]
    for i in range (1,len(listData)):
        number=math.gcd(number,listData[i])
    return number
        

data=[2*3*3*5*7*7,3*5*7*11*13,2*2*3*5*5*7*7,100*9*25*49]
GCD=gcdAll(data)
print ("GCDALL=",GCD)

