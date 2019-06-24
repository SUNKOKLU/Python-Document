
# coding: utf-8

# In[3]:


a=[1,3,5,7,9,11]
size=len(a)
half=size//2

for i in range (half):
    tmp=a[i]
    a[i]=a[size-i-1]
    a[size-i-1]=tmp

print (a)

