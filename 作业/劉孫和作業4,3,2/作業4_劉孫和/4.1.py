
# coding: utf-8

# In[2]:


a=[1,2,3,4,5,6,7,8]
size=len(a)
half=size//2

for i in range (half):
    tmp=a[i]
    a[i]=a[half+i]
    a[half+i]=tmp
print (a)

