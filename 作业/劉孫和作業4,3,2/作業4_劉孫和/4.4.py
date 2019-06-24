
# coding: utf-8

# In[1]:


score=[88,45,63,74,88,36,57,45,88,100,95]
query=int (input('Input a score:'))

if query in score:
    times=score.count(query)
    start=0
    end=len(score)
    for i in range (times):
        index=score.index(query,start,end)
        print('[',index,']',query)
        start=index+1
    

