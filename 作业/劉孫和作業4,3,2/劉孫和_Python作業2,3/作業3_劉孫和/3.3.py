
# coding: utf-8

# In[4]:


h=int(input("h="))
typ=int(input("type(1:直角三角形, 2: 三角形):"))
if typ==1:
    cnt=1
    for i in range(1,h+1):
        count_blank=h-cnt
        for j in range(0,count_blank):
            print(end="  ")
        for k in range (1,cnt+1):
            print(k,sep='',end='')
        cnt+=1
        print()
        
elif typ==2:
    for i in range(1,h+1):
        for j in range(0, h-i):
            print(end=" ")
        for k in range(1, 2*i-1+1):
            print(k, end='')
        print()
else:
    print("Error!")

