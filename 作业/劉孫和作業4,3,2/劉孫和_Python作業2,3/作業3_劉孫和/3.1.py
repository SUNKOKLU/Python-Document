
# coding: utf-8

# In[3]:


import math
flag="Y" 
while flag.upper()=="Y":
    orignal,rate,num=input("(本金，年利率，期數)=").split()
    orignal,rate,num=float(orignal),float(rate),float(num)
    print("本利和=",orignal*math.pow((1+rate),num))
    flag=input("===continue?(y/n)")
print()

