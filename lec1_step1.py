#!/usr/bin/env python
# coding: utf-8

# In[15]:


## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2020 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2022-8-10 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A1_python_intermediate_course
# # @IDE     : Python 3.9.13 (main, Aug  7 2022, 01:33:23)  [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
# # @File    : lec1_step1.py 


# In[7]:


import numpy as np
inData=np.array([1, 2, 3])
NofD=len(inData)
flagD=np.full(NofD,True)
print(flagD)


# In[6]:


inData=np.array([1, 2, 3])
flagD=np.full(len(inData),True)
print(flagD)


# In[36]:


rdat_s=np.floor(np.random.rand(NofD)*NofD)
rdat_s=np.asarray(rdat_s, dtype = int)
print(rdat_s)


# In[35]:


NofD=10
rdat_s=np.random.randint(NofD, size=NofD)
print(rdat_s)


# In[122]:


inData = np.linspace(0, 10, NofD, endpoint=True, dtype=int)
print(inData)
inData = np.linspace(0, 10, NofD, endpoint=False, dtype=int)
print(inData)
# array range →a_range→ arange
inData = np.arange(0, 100, 10, dtype=int)
print(inData)
print(inData[1])
print(inData[[1]])
print(inData[[1,2,3]])
print(inData[rdat_s])


# In[123]:


inData[1]


# In[124]:


inData[[1]]


# In[125]:


inData[[1]]+inData[[2]]


# In[126]:


inData[1]+inData[2]


# In[130]:


inData[[1,2]]+inData[[2,3]]


# In[128]:


inData[1]+inData[[2,3]]


# In[129]:


inData[[1]]+inData[[2,3]]


# In[131]:


inData[[1]]*inData[[2,3]]


# In[90]:


r_a1 = np.random.rand()   
print(r_a1)
r_a2 = np.random.rand(3) 
print(r_a2)
r_a3 = np.random.rand(1, 4)   
print(r_a3)
print(' ')
r_b1 = np.random.randint(1, 5, size=3)
print(r_b1)
r_b2 = np.random.randint(1, 5, size=(1,3))
print(r_b2)
r_b3 = np.random.randint(1, 5, size=(2,3))
print(r_b3)
r_b4 = np.random.randint(1, 5, size=(1,2,3))
print(r_b4)


# In[99]:


c1=np.zeros(6, dtype=int)   
print(c1)
c2=c1.reshape(2,3)   
print(c2)
c2=c1.reshape(1,6)   
print(c2)


# In[137]:


inData = np.arange(0, 10, 1, dtype=int)
print(inData)


# In[138]:


inData[3:]


# In[134]:


inData[-1]


# In[136]:


inData[3:-1]


# In[141]:


inData[-3:-1]


# In[ ]:




