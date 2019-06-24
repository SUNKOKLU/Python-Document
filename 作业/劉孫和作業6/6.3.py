
# coding: utf-8

# In[2]:


import math
def Cnk1(n,k):
    return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

def Cnk2(n,k):
    part=1
    for i in range (n-k+1,n+1):
        part*=i
    return part/math.factorial(k)

print (Cnk1(10,3)," ", Cnk2(20,15))

