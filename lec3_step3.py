#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2020 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2022-8-20 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A1_python_intermediate_course
# # @IDE     : Python 3.9.13 (main, Aug  7 2022, 01:33:23) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
# # @File    : lec3_step3.py 


# In[2]:


import numpy as np


# In[12]:


NofD=10
randD=np.random.randint(2, size=(10,10))
randD


# In[15]:


key=np.where(randD==0)
key


# In[16]:


key[0]


# In[17]:


key[1]


# In[19]:


randD[key]=3
randD


# In[84]:


NofD=10
rD1=np.random.randint(NofD,size=NofD)
rD2=np.random.randint(2, NofD,size=NofD)
rD=rD2+rD1
mixAry=[np.arange(rD1[i],rD[i]) for i in range(0,len(rD2))]
edgL=[[mixAry[i][0],mixAry[i][-1]] for i in range(0,len(mixAry))]
edgAry=np.array(edgL)


# In[85]:


mixAry


# In[86]:


edgL


# In[87]:


edgAry


# In[29]:


np.random.randint(0,2, size=(1,3))


# In[35]:


rD1=np.random.randint(NofD,size=(NofD,1))
rD1.tolist()


# In[36]:


rD2=np.random.randint(2, NofD,size=NofD)
rD2


# In[38]:


rD1=np.random.randint(NofD,size=NofD)
rD2=np.random.randint(2, NofD,size=NofD)
rD=rD2+rD1
rD


# In[47]:


mixAry=[np.arange(rD1[i],rD[i]) for i in range(0,len(rD2))]
mixAry


# In[52]:


edgAry=[[mixAry[i][0],mixAry[i][-1]] for i in range(0,len(mixAry))]
edgAry


# In[89]:



List_new=[item for item in TargetG if item not in ClosedList]


# In[90]:


list(set(['A','B','C','D']))


# In[91]:


list(set(['A','B','C','D'])-set(['A']))


# In[95]:


list(set(['S','B','A','D'])-set(['D','B']))

