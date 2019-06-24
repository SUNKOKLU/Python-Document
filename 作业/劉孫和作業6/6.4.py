
# coding: utf-8

# In[3]:


mothDays=[0,31,28,31,30,31,30,31,31,30,31,30,31]
LmothDays=[0,31,29,31,30,31,30,31,31,30,31,30,31]
def isLeapYear (year):
    if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
        return True 
    return False

def iThDays(y,m,d):
    days=d
    if isLeapYear(y)==True:
        for i in range (m):
            days+=LmothDays[i]
    else:
        for i in range (m):
            days+=mothDays[i]
    return days

def trans(de):
    d1=de%100
    de=de//100
    m1=de%100
    y1=de//100
    return y1,m1,d1

def diffInDays(date1,date2):
    y1,m1,d1=trans(date1)
    y2,m2,d2=trans(date2)
   
    number=iThDays(y1,m1,d1)+iThDays(y2,m2,d2)
    for i in range (y1+1,y2):
        if isLeapYear(i):
            number+=366
        else:
            number+=365
    return number
            
diff=diffInDays(19980707,20080430)
print("diff days=",diff)

