
# coding: utf-8

# In[8]:


import math

def quadratic(a,b,c):
    p=b*b-4*a*c
    if p>=0 and a!=0:#一元二次方程有解的条件
        x1=(-b+math.sqrt(p))/(2*a)
        x2=(-b-math.sqrt(p))/(2*a)
        return x1,x2
    elif  p>0 and a==0:#a=0的情况下为一元一次方程
    	x1=x2=-c/b
    	return x1
    elif p<0:
         m=-b/(2*a)     
         n=math.sqrt(-p)/(2*a) 
         x1=str(m)+"+"+str(n)+"i"
         x2=str(m)+"-"+str(n)+"i"
         return x1, x2
    else:
        return ("Error!")
 
a,b,c=input("a,b,c=").split()
a,b,c=float(a),float(b),float(c)

print(quadratic(a,b,c))

