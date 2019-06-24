
# coding: utf-8

# In[1]:


def NonRecursiveGcd(x,y):
 
    while(y):
        x , y = y , x % y
    return x

a,b,c=input ("Input three numbers: ").split()
a,b,c=int(a),int(b),int(c)
x1=NonRecursiveGcd(a,b)
print("gcd=",NonRecursiveGcd(x1,c))

