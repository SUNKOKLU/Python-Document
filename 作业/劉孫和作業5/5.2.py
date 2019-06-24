
# coding: utf-8

# In[23]:


m1=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
m2=[[] for i in range (3)]
for i in range (3):
    m2[i]=[0 for j in range (4) ]
    
for i in range (len(m1)):
    for j in range ( len(m1[i])):
        m2[i][j]=m1[i][j]*2

m3=[[] for i in range (4)]
for i in range (4):
    m3[i]=[0 for j in range (3) ]

for i in range (len(m1)):
    for j in range ( len(m1[i])):
        m3[j][i]=m1[i][j]

m4=[[] for i in range (3)]      
for i in range (3):
    m4[i]=[0 for j in range (3) ]      

for i in range (3):
    for j in range (3):
        for k in range (4):
            m4[i][j]+=m1[i][k]*m3[k][j]
    
print ("矩陣相加之後：",m2)
print ("矩陣轉置之後：",m3)
print ("矩陣相乘之後：",m4)

