
# coding: utf-8

# In[11]:


import random


def weight_choice(weight):
    t = random.randint(0, int(sum(weight))- 1)
    float(t)
    for i, val in enumerate(weight):
        t -= val
        if t < 0:
            return i
        
        

a= [2,3,4,5,6,7,8,9,10,11,12]
weight=[3.33,3.33,3.33,16,16,16,16,16,3.33,3.33,3.33]
times=[0 for i in range (12)]

for i in range (5000):
    point=a[weight_choice(weight)]   
    for i in range (12):
        if (point==i+1):
            times[i]+=1
            
title=['P'+str(i) for i in range (1,13)]
print (list(zip(title,times)))


