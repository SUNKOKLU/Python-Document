
# coding: utf-8

# In[9]:


import random 
from statistics import *
random.seed(111)
m=[random.uniform(-100.0,100.0) for i in range (100)]
pos=[x for x in m if x>=0]
neg=[x for x in m if x<0]

range_up=mean(pos)+2*stdev(pos)
range_down=mean(pos)-2*stdev(pos)
pos=[x for x in pos if x<=range_up and x>=range_down]

range_up=mean(neg)+2*stdev(neg)
range_down=mean(neg)-2*stdev(neg)
neg=[x for x in neg if x<=range_up and  x>=range_down]

print ("the mean of pos list after operation:",mean(pos))
print ("the mean of neg list after operation:",mean(neg))


