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
# # @File    : lec4_step4_BarStack_Aligned_Stage3.py 

```


```python
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
        
        

```

    0
    [0]
    1
    1
    [0, array([1, 6])]
    2
    2
    [0, array([1, 6]), array([2, 3])]
    3



```python

```


```python
prFill[0:1:len(prFill)]
```




    array([], dtype=float64)




```python
i=4
```


```python
remF=1-prFill[i]
IDrem=np.where((prFill[i+1:len(prFill)]<=remF) & fillLine[i+1:len(prFill)])
tmp=i
fID=i
```


```python
remF
```




    0.5




```python
IDrem
```




    (array([2, 4, 5]),)




```python
IDrem[0][0]
```




    2




```python
fID
```




    4




```python
IDrem[0][0]+fID+1
```




    7




```python
j
```




    0




```python
i
```




    4




```python

```


```python
fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)

```

    7
    [4 7]



```python
prFill[IDrem[j][0]+i]
```




    0.4




```python
IDrem[j][0]
```




    2




```python
prFill[fID]
remF=remF-prFill[fID]
IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
print(IDrem)
```

    (array([2]),)



```python
fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)

```

    10
    [ 4  7 10]



```python
prFill[fID]
remF=remF-prFill[fID]
IDrem=np.where((prFill[fID+1:len(prFill)]<=remF) & fillLine[fID+1:len(prFill)])
print(IDrem)
```

    0.0
    (array([], dtype=int64),)



```python
fID=IDrem[0][0]+fID+1
```


```python
prFill[1:-1]
```




    array([0.6, 0.5, 0.5, 0.5, 0.9, 0.4, 0.3, 0.8, 0.4])




```python
len(prFill[fID+1:len(prFill)])
```




    7




```python
 fillLine[fID+1:len(prFill)]
```




    array([ True,  True, False,  True,  True,  True,  True])




```python
prFill[fID+1:-1]
```




    array([0.5, 0.9, 0.4, 0.3, 0.8, 0.4])




```python
i=4
```


```python
remF=1-prFill[i]
print(remF)
```

    0.5



```python
prFill[i+1:-1]
```




    array([0.9, 0.4, 0.3, 0.8, 0.4])




```python
fillLine[fID+1:-1]
```




    array([ True,  True, False,  True,  True,  True])




```python

```


```python
prFill
```




    array([0.9, 0.6, 0.5, 0.5, 0.5, 0.9, 0.4, 0.3, 0.8, 0.4, 0.2])




```python
fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)
remF=remF-prFill[IDrem[j][0]+i]
print(remF)
IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
print(IDrem)
```

    7
    [4 7]
    0.09999999999999998
    (array([], dtype=int64),)



```python
remF=1-prFill[i]
IDrem=np.where((prFill[i+1:-1]<=remF) & fillLine[i+1:-1])
print(IDrem)
tmp=i
fID=i
j=0
```

    (array([2, 4]),)



```python
fID=IDrem[0][0]+fID+1
print(fID)
```

    5



```python
tmp=np.append(tmp,fID)
remF=remF-prFill[IDrem[j][0]+i]
```


```python
remF

```




    0.0




```python
remF
```




    0.5




```python
fillLine
```




    array([False, False, False, False,  True,  True, False,  True,  True,
            True,  True])




```python
prFill[i+1:-1]
```




    array([0.5, 0.9, 0.4, 0.3, 0.8, 0.4])




```python
print(IDrem[0].size)
```

    3



```python
fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)

```

    4
    [3 4]



```python
print(remF)
print(IDrem[j][0])
print(i)
print(prFill[IDrem[j][0]+i])
```

    0.5
    0
    3
    0.5



```python
prFill[IDrem[j][0]+i]

```




    0.5




```python
j
```




    0




```python
remF=remF-prFill[IDrem[j][0]+i]
print(remF)
IDrem=np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
print(IDrem)
print(IDrem[0].size)
LineT.append(tmp)
print(LineT)
```

    0.0
    (array([], dtype=int64),)
    0
    [0, array([1, 6]), array([2, 3]), array([3, 4])]



```python
np.where((prFill[fID+1:-1]<=remF) & fillLine[fID+1:-1])
```




    (array([0, 3, 5]),)




```python

```


```python
prFill[fID+1:-1]
```




    array([0.9, 0.4, 0.3, 0.8, 0.4])




```python
fID=IDrem[0][0]+fID+1
print(fID)
tmp=np.append(tmp,fID)
print(tmp)
```

    4
    [3 4]



```python
prFill[IDrem[j][0]+i]
```




    0.5




```python
remF=remF-prFill[IDrem[j][0]+i]
print(remF)
```

    -0.5



```python
prFill[IDrem[j][0]+i]
```




    0




```python
IDrem
```




    (array([], dtype=int64),)




```python

```
