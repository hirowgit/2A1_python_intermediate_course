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
# # @File    : lec2_step1.py 


# In[512]:


import numpy as np
import matplotlib.pyplot as plt


# In[163]:


allData = np.loadtxt('allData200.csv', delimiter=',', dtype='int64')
allData


# In[158]:


a = np.array([[1,2,4],[3,2,1]])
np.sort(a, axis=None)


# In[160]:


np.sort(a, axis=0) 


# In[394]:


allData_sample=allData[0:20,:]
np.sort(allData_sample,axis=0) 


# In[170]:


data = np.array([[3, 0, 0, .24],
                 [4, 1, 1, .41],
                 [2, 1, 1, .63],
                 [1, 1, 3, .38]]) #imagine rows of a spreadsheet
#now do sortrows(data,[3,-4])
ix = np.lexsort((data[:, 3][::-1], data[:, 2])) 
#this yields [0, 2, 1, 3]

#note that lexsort sorts first from the last row, so sort keys are in reverse order

data[ix]


# In[177]:


sample_2d = np.array([[50,4, 89], [5, 150, 20], [110, 8, 1]])
print(sample_2d)
print(' ')

col_id = 1
print(sample_2d[:, col_id])
print(' ')
print(np.argsort(a_2d[:, col_id]))


# In[178]:


sorted_by_col = sample_2d[np.argsort(sample_2d[:, col_id])]
print(sorted_by_col)


# In[460]:


allData_sample


# In[461]:


sorted_data=np.sort(allData_sample, axis=0) 
sorted_data


# In[462]:


diffData=np.diff(sorted_data,axis=0)
diffData


# In[464]:





# In[465]:


key=np.where(np.transpose(diffData)>0)
key


# In[466]:


kj=key[0]
kj


# In[467]:


ki=key[1]
ki


# In[468]:


bodyK=np.where(np.diff(kj)>0)
bodyK


# In[403]:


sizeD=np.shape(allData_sample)
sizeD


# In[469]:


# n0=np.array([0],dtype=int)
np.concatenate([bodyK, bodyK],axis=1)


# In[234]:


np.array([0])


# In[237]:


bodyK


# In[247]:


bodyK


# In[277]:


a1 = np.ones((1,3), int)
a2 = np.ones((1,3), int)
np.concatenate([a1, a2],axis=1)


# In[270]:


a1 = np.ones((1,3), int)


# In[299]:


[0,list(bodyK), len(kj)]


# In[266]:


np.shape(bodyK)


# In[281]:


len(kj)


# In[284]:


len(kj)*np.ones((1,1), int)


# In[285]:


[[ len(kj)]]


# In[294]:


bodyK


# In[296]:


list(bodyK)


# In[302]:


arr_1d=list(bodyK)
bodyK.tolist()


# In[303]:


bodyK


# In[307]:


bodyK


# In[308]:


kj


# In[313]:


kj[bodyK]


# In[314]:


ab=np.concatenate([[[0]], bodyK],axis=1)


# In[315]:


kj[ab]


# In[496]:


bodyK2=bodyK+np.array([[1]])
sect_id=np.insert(bodyK2, 0,0)
sect_id=np.append(sect_id, len(kj))
sect_id


# In[497]:


kj


# In[498]:


ki


# In[339]:


kj[sect_id]


# In[363]:


kj[sect_id[0]:sect_id[1]]


# In[368]:


sect_id[1]


# In[499]:


g2=np.arange(sect_id[0],sect_id[1])
g2


# In[347]:


kj[sect_id[1]:sect_id[2]]


# In[367]:


kj[g2]


# In[350]:


sect_id


# In[501]:


setN=sizeD[0]
NofD=sizeD[1]


# In[500]:


sect_eg=np.vstack([sect_id[0:-1],sect_id[1:]])
sect_eg


# In[502]:


sect_egT=np.transpose(sect_eg)
sect_egT


# In[492]:


[sect_egT[i]  for i in range(0,5)]


# In[439]:


sect_egT[0][1]


# In[440]:


len(sect_egT)


# In[503]:


[kj[sect_egT[i][0]:sect_egT[i][1]]  for i in range(0,len(sect_egT))]


# In[518]:


sect_range=[ki[sect_egT[i][0]:sect_egT[i][1]]  for i in range(0,len(sect_egT))]
sect_range


# In[505]:


[np.diff(np.hstack([-1,d,setN-1])) for d in sect_range]


# In[508]:


[np.diff(np.hstack([-1,d,setN-1]))/setN for d in sect_range]


# In[519]:


NofE_data=[np.diff(np.hstack([-1,ki[sect_egT[i][0]:sect_egT[i][1]],setN-1]))   for i in range(0,len(sect_egT))]
NofE_data


# In[520]:


NofE_data_p=[np.diff(np.hstack([-1,ki[sect_egT[i][0]:sect_egT[i][1]],setN-1]))/setN   for i in range(0,len(sect_egT))]
NofE_data_p


# In[521]:


NofE_data_p[1]


# In[524]:


x=np.arange(0,NofD)
y=NofE_data_p[3]
plt.plot(x,y)
plt.show()


# In[ ]:





# In[517]:


np.arange(0,NofD)


# In[454]:


sorted_data


# In[ ]:


sect_range=[ki[sect_egT[i][0]:sect_egT[i][1]]  for i in range(0,len(sect_egT))]
sect_range


# In[373]:


g3[0]


# In[325]:


sect_id[0:-1]


# In[333]:


kj[sect_id[0:-1]]


# In[327]:


bodyK


# In[331]:


bodyK-np.array([[1]])


# In[388]:


setN


# In[ ]:




