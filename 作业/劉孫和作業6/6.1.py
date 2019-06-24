
# coding: utf-8

# In[ ]:


#59.EX4
import math

xs=[0 for i in range(360)]
ys=[0 for i in range (360)]
x,y,r=1,2,8.5 

for i in range (360):
    xs[i]=x+r*math.cos(i*math.pi/180)
    ys[i]=y+r*math.sin(i*math.pi/180)
    print('(',xs[i],',',ys[i],')',end='')

print()

