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
# # @File    : lec4_step6_BarStack_Aligned_Stage5.py 


# In[1]:


import numpy as np
#prFill=[90    60    50    50    50    90    40    30    80    40  20 ]/100;
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
tmp=[]
k=0
for i in range(len(prFill)):
#for i in range(5):
#for i in range(5):
    if fillLine[i]:
        remF=1-prFill[i]
        IDrem=np.where((prFill[i+1:len(prFill)]<=remF) & fillLine[i+1:len(prFill)])
        tmp=i
        fID=i
        #j=0
        while IDrem[0].size > 0:
            fID=IDrem[0][0]+fID+1
            tmp=np.append(tmp,fID)
            remF=remF-prFill[fID]
            IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
        LineT.append(tmp)
        fillLine[tmp]=False
        print("k;",k)
        print("LineT;",LineT)
        k=k+1
        print("k;",k)


# In[2]:


#行列の要素内の型が違うことが問題となる
for i in LineT:
    print(type(i))


# In[3]:


#型がintのものを'numpy.ndarray'に変換
f_LineT = [np.array(i) if type(i)==int else i for i in LineT]
print(f_LineT)
[print(type(i)) for i in f_LineT]


# In[3]:


LineT


# In[4]:


#lenLineT=cell2mat(cellfun(@(x) length(x),LineT,'UniformOutput',false));に該当部
lenLineT = [i.size for i in f_LineT]
print(lenLineT)


# In[5]:


#stackBarD=zeros(size(LineT,2),max(lenLineT));に該当部
stackBarD = np.zeros((np.shape(f_LineT)[0],max(lenLineT)))
print(stackBarD)


# In[6]:


len(f_LineT)


# In[7]:


f_LineT[1]
print(prFill)
i = [1, 6]
print(prFill[i])


# In[12]:


#stackBarDにグラフに積み上げるprFillの値を置き換え
for i in range(len(f_LineT)):
    tmp = f_LineT[i]
#     print(prFill[tmp])
    print(lenLineT[i])
    print(stackBarD[i,0:lenLineT[i]])
    stackBarD[i,0:lenLineT[i]] = prFill[tmp] 
    print(stackBarD)


# In[ ]:





# In[11]:


y_data_stack = []
y_data_stack = tuple([np.append(y_data_stack, i)  for i in stackBarD])
print(y_data_stack)


# In[13]:


LineT[0]


# In[98]:


x_label = [i+1 for i in range(len(prFill))]
x_stack_label = ['L'+str(i+1) for i in range(len(stackBarD))]
y_label = np.arange(0, 12, 2)
y_label =[i/10 for i in y_label]
print(x_label)
print(x_stack_label)
print(y_label)


# In[63]:


#matplotlibモジュールの読み込み
import matplotlib.pyplot as plt


# In[97]:


#2つのグラフの表示画面の分割
fig = plt.figure(figsize=(30,13), dpi=50)
init_fig = fig.add_subplot(2 , 1, 1)
stack_fig = fig.add_subplot(2, 1, 2)

#上のグラフの表示設定
#参考；https://www.yutaka-note.com/entry/matplotlib_axis

init_fig.set_xlabel("store ID", size = 25)
init_fig.set_xticks(x_label)
init_fig.set_xticklabels(x_label, size=20)

init_fig.set_ylabel("Action Steps(AS)", size = 25)
init_fig.set_yticks(y_label)
init_fig.set_yticklabels(y_label, size=20)
init_fig.set_ylim(0 , 1)
# init_fig.set_yticks(np.arange(0, 1, 0.2))
# init_fig.title("")
init_fig.grid(True)
#上のグラフの表示
init_fig.bar(x_label, prFill, color = 'w', edgecolor ='black', linewidth = '5')


# In[ ]:


#下のグラフの表示設定
#参考；https://www.yutaka-note.com/entry/matplotlib_axis

stack_fig.set_xlabel("store ID", size = 25)
stack_fig.set_xticks(x_stack_label)
stack_fig.set_xticklabels(x_stack_label, size=20)

stack_fig.set_ylabel("Action Steps(AS)", size = 25)
stack_fig.set_yticks(y_label)
stack_fig.set_yticklabels(y_label, size=20)
stack_fig.set_ylim(0 , 1)
# init_fig.set_yticks(np.arange(0, 1, 0.2))
# init_fig.title("")
stack_fig.grid(True)
#上のグラフの表示
stack_fig.bar(x_label, prFill, color = 'w', edgecolor ='black', linewidth = '5')


# In[26]:


init_fig.bar(x_label, prFill)
# plt.show


# In[ ]:


len(LineT[1])


# In[ ]:


LineT[2].size


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




