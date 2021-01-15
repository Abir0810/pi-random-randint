#!/usr/bin/env python
# coding: utf-8

# In[6]:


from math import pi
r=input("radius od orbit (millon km):")
v=input("orbital speed")
r=float(r)
v=float(v)
r=r*1000000
year=2*pi*r/v
year=year/(60*60*24)
print(round(year))


# In[9]:


from math import pi
h=float(input('h='))
r=float(input('r='))
side=2*pi*r*h
circle=2*(pi*r**2)
area=circle+side
print('A=',round(area,2))


# In[10]:


c=input("Letter(a-z):")  
c=ord(c)
a=ord('a')
n=c-a
n=n+1
print("its number is %d" %n)


# In[13]:


from random import random,randint
print("range of interger:")
imin=int(input())
imax=int(input())
n=randint(imin,imax)
print("%d"%n)
print("range of floats:")
fmin=float(input())
fmax=float(input())
n=random()*(fmax-fmin)+fmin
print("%.3f"%n)


# In[ ]:





# In[ ]:




