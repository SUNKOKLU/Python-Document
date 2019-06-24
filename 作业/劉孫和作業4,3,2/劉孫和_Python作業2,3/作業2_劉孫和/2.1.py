
# coding: utf-8

# In[7]:


itemType=input("Choose Item (A/B/C)? ")
itemAmmount=int(input("How many pieces? "))
discount=0
itemSinglePrice=0

if itemType=="B":
    itemSinglePrice=350
elif itemType=="C":
    itemSinglePrice=400
else :
    itemSinglePrice=200
    
if itemAmmount>=30:
    discount=0.8
elif itemAmmount>=10:
    discount=0.9
else:
    discount=1

print ("total =",itemSinglePrice*itemAmmount*discount)
    
 

