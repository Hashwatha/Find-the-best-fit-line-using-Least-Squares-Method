#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
import matplotlib.pyplot as plt


# In[23]:


#preprocessing Input data

X=np.array(eval(input()))
Y=np.array(eval(input()))


# In[24]:


#mean
X_mean = np.mean(X)
Y_mean = np.mean(Y)
num=0 #for slope
den=0 #for slope


# In[25]:


# to find the sum of (xi-x') & (yi-y') & (xi-x')^2

for i in range(len(X)):
    num +=(X[i] - X_mean) * (Y[i] - Y_mean)
    den +=(X[i]-X_mean)**2


# In[26]:


#calculate slop
m = num/den


# In[27]:


#calculate intercept
b = Y_mean - m * X_mean


# In[28]:


print("Slope : ",m)
print("Y intercrept : ",b)


# In[29]:


#line equation
Y_predicted = m * X + b


# In[31]:


#to plot graph
plt.scatter(X,Y)
plt.plot(X,Y_predicted,color='red')
plt.show()
print("Name:Hashwatha M")
print("Reg No:212223240051")


# In[ ]:




