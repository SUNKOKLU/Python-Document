
# coding: utf-8

# In[ ]:


a=[1,3,5,7,9,11]
size=len(a)-1

for i in range (0,size):
    tmp=a[i]
    a[i]=a[size]
    a[size]=tmp
print(a)

