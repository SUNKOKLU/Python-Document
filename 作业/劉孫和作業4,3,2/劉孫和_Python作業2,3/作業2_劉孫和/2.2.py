
# coding: utf-8

# In[2]:


h,m,s=input("input time: ").split()
hh,mm,ss=int(h),int(m),int(s)
ad_s=int (input("advanced time(secs):"))
sec=ad_s%60
partA=ad_s/60

hour=0
mins=0
st=""

if partA>=60:
    mins=partA%60
    hour=partA/60
else :
    mins=partA
    
time_h=int(hh+hour)
time_m=int(mm+mins)
time_s=int(ss+sec)

if time_h>24:
    time_h=int(time_h%24)

if time_h<=12:
    st="AM"
else:
    time_h=time_h-12
    st="PM"

print(st,time_h,time_m,time_s)

