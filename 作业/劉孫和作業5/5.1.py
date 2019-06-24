
# coding: utf-8

# In[ ]:


#EX2
import random 
random.seed(111)
stud_no=[56,43,49,65]
class_avg=[0 for i in range (4)]


for i in range (len(stud_no)):
    sum=0
    for j in range(int(stud_no[i])):
        grade=random.randint(0,100)
        sum+=grade
    class_avg[i]=sum/stud_no[i]
       

print(class_avg)
total=0
for i in range (len(stud_no)):
    total+=class_avg[i]
print(total/4)

