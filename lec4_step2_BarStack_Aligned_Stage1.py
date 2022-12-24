#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2020 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2020-11-30 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A1_python_intermediate_course
# # @IDE     : Python 3.9.14 (main, Sep  6 2022, 23:29:09) [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
# # @File    : lec4_step2_BarStack_Aligned_Stage1.py 


# In[1]:


import numpy as np
#prFill=[90    60    50    50    50    90    40    30    80    40  20 ]/100;
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
k=1
for i in range(len(prFill)):
    print(i)
    print(prFill[i])
  


# In[ ]:





# In[1]:


1


# In[9]:


import numpy as np
#prFill=[90    60    50    50    50    90    40    30    80    40  20 ]/100;
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
k=0
for i in range(len(prFill)):
    if fillLine[i]:
        remF=1-prFill[i]
        IDrem=np.where((prFill[i+1:-1]<=remF) & fillLine[i+1:-1])
        tmp=i
        fID=i
        j=0
        while IDrem[0].size > 0:
            fID=IDrem[0][0]+fID
            tmp=np.append(tmp,fID)
            remF=remF-prFill[IDrem[j][0]+i]
            IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
        LineT.append(tmp)
        fillLine[tmp]=False
        print(k)
        k=k+1
        
        


# In[ ]:





# In[ ]:





# In[ ]:





# In[118]:


prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
k=1


# In[119]:


i=0
fillLine[i]


# In[20]:


remF=1-prFill[i]
print(remF)
IDrem=np.where((prFill[i+1:-1]<=remF) & fillLine[i+1:-1])
print(IDrem)
tmp=i
fID=i
j=0
i


# In[15]:


i=0
print(remF)
print(prFill[1:-1])
np.where(prFill[i+1:-1]<=remF)
IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
print(IDrem)
print(len(IDrem))
if IDrem:
    print('IDrem is NOT empty')
else:
    print('IDrem is empty')
np.array(IDrem)
print(IDrem[0])


# In[2]:


if IDrem[0]:
    print('IDrem is NOT empty')
else:
    print('IDrem is empty')
print(IDrem[0])


# In[116]:


LineT


# In[117]:


k


# In[131]:


np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])


# In[130]:


fID


# In[128]:


IDrem[0][0]


# In[132]:


prFill[fID+1:-1]


# In[133]:


fillLine[fID+1:-1]


# In[134]:


np.where((prFill[fID+1:-1]<=remF) )


# In[135]:


remF


# In[136]:


IDrem[j]


# In[137]:


IDrem[j][0]


# In[139]:


LineT


# In[ ]:





# In[ ]:




