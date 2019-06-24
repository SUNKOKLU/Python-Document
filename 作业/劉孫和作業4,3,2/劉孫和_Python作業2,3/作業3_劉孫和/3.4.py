
# coding: utf-8

# In[20]:


import math
def isPrime(x):
    for i in range (2, math.ceil( math.sqrt(x)+1.0 ) ):
        if x% i== 0:
            return False 
    return True

def findPrimes(n):
    print("primes in [2,",n,"]:",sep='',end='')
    
    for x in range (2 , n+1):
        if isPrime(x):
            print(x , end=',')
            
    print ()
    
n=int(input("n="))
findPrimes(n)

