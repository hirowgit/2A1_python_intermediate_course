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
# # @File    : lec4_step4_BarStack_Aligned_Stage3.py 


# In[1]:


import numpy as np
#prFill=[90    60    50    50    50    90    40    30    80    40  20 ]/100;
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
k=0
#for i in range(len(prFill)):
#for i in range(5):
for i in range(4):
    if fillLine[i]:
        remF=1-prFill[i]
        IDrem=np.where((prFill[i+1:len(prFill)]<=remF) & fillLine[i+1:len(prFill)])
        tmp=i
        fID=i
        j=0
        while IDrem[0].size > 0:
            fID=IDrem[0][0]+fID+1
            tmp=np.append(tmp,fID)
            remF=remF-prFill[fID]
            IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
        LineT.append(tmp)
        fillLine[tmp]=False
        print(k)
        print(LineT)
        k=k+1
        print(k)
        
        


# In[ ]:





# In[181]:


prFill[0:1:len(prFill)]


# In[230]:


i=4


# In[231]:


remF=1-prFill[i]
IDrem=np.where((prFill[i+1:len(prFill)]<=remF) & fillLine[i+1:len(prFill)])
tmp=i
fID=i


# In[197]:


remF


# In[198]:


IDrem


# In[200]:


IDrem[0][0]


# In[201]:


fID


# In[220]:


IDrem[0][0]+fID+1


# In[214]:


j


# In[215]:


i


# In[ ]:





# In[232]:


fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)


# In[233]:


prFill[IDrem[j][0]+i]


# In[216]:


IDrem[j][0]


# In[234]:


prFill[fID]
remF=remF-prFill[fID]
IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
print(IDrem)


# In[235]:


fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)


# In[221]:


prFill[fID]
remF=remF-prFill[fID]
IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
print(IDrem)


# In[191]:


fID=IDrem[0][0]+fID+1


# In[172]:


prFill[1:-1]


# In[174]:


len(prFill[fID+1:len(prFill)])


# In[176]:


fillLine[fID+1:len(prFill)]


# In[171]:


prFill[fID+1:-1]


# In[152]:


i=4


# In[158]:


remF=1-prFill[i]
print(remF)


# In[159]:


prFill[i+1:-1]


# In[160]:


fillLine[fID+1:-1]


# In[ ]:





# In[154]:


prFill


# In[149]:


fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)
remF=remF-prFill[IDrem[j][0]+i]
print(remF)
IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
print(IDrem)


# In[146]:


remF=1-prFill[i]
IDrem=np.where((prFill[i+1:-1]<=remF) & fillLine[i+1:-1])
print(IDrem)
tmp=i
fID=i
j=0


# In[131]:


fID=IDrem[0][0]+fID+1
print(fID)


# In[133]:


tmp=np.append(tmp,fID)
remF=remF-prFill[IDrem[j][0]+i]


# In[134]:


remF


# In[118]:


remF


# In[112]:


fillLine


# In[119]:


prFill[i+1:-1]


# In[100]:


print(IDrem[0].size)


# In[101]:


fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)


# In[103]:


print(remF)
print(IDrem[j][0])
print(i)
print(prFill[IDrem[j][0]+i])


# In[105]:


prFill[IDrem[j][0]+i]


# In[107]:


j


# In[95]:


remF=remF-prFill[IDrem[j][0]+i]
print(remF)
IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
print(IDrem)
print(IDrem[0].size)
LineT.append(tmp)
print(LineT)


# In[62]:


np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])


# In[ ]:





# In[97]:


prFill[fID+1:-1]


# In[57]:


fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)


# In[49]:


prFill[IDrem[j][0]+i]


# In[51]:


remF=remF-prFill[IDrem[j][0]+i]
print(remF)


# In[43]:


prFill[IDrem[j][0]+i]


# In[44]:


IDrem


# In[ ]:




