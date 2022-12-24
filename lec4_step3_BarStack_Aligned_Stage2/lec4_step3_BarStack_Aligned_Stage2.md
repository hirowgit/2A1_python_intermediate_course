```python
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
# # @File    : lec4_step3_BarStack_Aligned_Stage2.py 

```


```python
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
            fID=IDrem[0][0]+fID+1
            tmp=np.append(tmp,fID)
            remF=remF-prFill[IDrem[j][0]+i]
            IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
        LineT.append(tmp)
        fillLine[tmp]=False
        print(k)
        k=k+1
        
        

```

    0
    1
    2
    3
    4
    5
    6
    7



```python
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
fillLine=np.full(len(prFill),True)
LineT=[]
k=0
```


```python
i=1
```


```python
remF=1-prFill[i]
print(remF)
print(prFill)
IDrem=np.where((prFill[i+1:-1]<=remF) & fillLine[i+1:-1])
print(IDrem)
tmp=i
fID=i
j=0
print(IDrem)
IDrem[0].size
```

    0.8
    [0.9 0.6 0.5 0.5 0.5 0.9 0.4 0.3 0.8 0.4 0.2]
    (array([], dtype=int64),)
    (array([], dtype=int64),)





    0




```python
print(IDrem[0][0])
fID=IDrem[0][0]+fID
print(fID)
```

    4
    5



```python
print(LineT)
```

    [0, array([1, 6]), array([2, 3]), array([4, 7]), 5, 8, 9, 10]



```python

```
