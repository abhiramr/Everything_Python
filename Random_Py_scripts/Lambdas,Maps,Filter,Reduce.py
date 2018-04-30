
# coding: utf-8

# In[1]:

f = lambda x,y : x*y


# In[2]:

f(3,3
 )


# In[14]:

fahrenheit = lambda T : ((float(9)/5)*T + 32)


# In[15]:

centigrade = lambda T : ((float(5)/9)*(T-32))


# In[6]:

temp = (36.5, 37,27,21)


# In[29]:

F = map(fahrenheit,temp)


# In[33]:

C = map(centigrade,F)


# In[35]:

F


# In[11]:

print(C)


# In[22]:

C


# In[23]:

F


# In[31]:

list(F)


# In[34]:

list(C)


# In[36]:

Celsius = [39.2, 36.5, 37.3, 37.8]


# In[65]:

Fahrenheit = map(lambda x: (float(9)/5)*x + 32, Celsius)


# In[54]:

list(Fahrenheit)


# In[61]:

list(Fahrenheit)


# In[66]:

C = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)


# In[67]:

list(C)


# In[68]:

arr1 = [4,3,6,8]


# In[69]:

arr2 = [3,4,6,8]


# In[73]:

add = map(lambda a,b: a+b,arr1,arr2)


# In[74]:

list(add)


# In[75]:

arr3 = [4,7,9,3]


# In[76]:

add = map(lambda a,b,c: a+b+c,arr1,arr2,arr3)


# In[77]:

list(add)


# In[78]:

fib = [0,1,1,2,3,5,8,13,21,34,55]


# In[82]:

res = filter(lambda x : (x%2==0),fib)

res
# In[83]:

list(res)


# In[84]:

red_ex = [1,2,3,4,5,6]


# In[89]:

red_val = reduce(lambda x,y: x*y , red_ex)


# In[86]:

#reduce is no longer supported in Python 3.x


# In[87]:

import functools


# In[88]:

from functools import reduce


# In[90]:

red_val


# In[ ]:



