```python
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
```


```python
import numpy as np
```


```python
NofD=10
randD=np.random.randint(2, size=(10,10))
randD
```




    array([[0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
           [1, 0, 1, 0, 0, 1, 1, 1, 1, 0],
           [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
           [1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
           [1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
           [1, 1, 0, 0, 0, 1, 1, 0, 0, 0],
           [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
           [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
           [0, 1, 1, 1, 1, 1, 0, 1, 0, 1]])




```python
key=np.where(randD==0)
key
```




    (array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4,
            4, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9]),
     array([0, 1, 6, 7, 1, 3, 4, 9, 1, 5, 6, 7, 8, 1, 3, 6, 7, 8, 9, 1, 3, 7,
            8, 2, 5, 2, 3, 4, 7, 8, 9, 4, 5, 7, 8, 1, 3, 6, 7, 8, 0, 6, 8]))




```python
key[0]
```




    array([0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4,
           4, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 8, 9, 9, 9])




```python
key[1]
```




    array([0, 1, 6, 7, 1, 3, 4, 9, 1, 5, 6, 7, 8, 1, 3, 6, 7, 8, 9, 1, 3, 7,
           8, 2, 5, 2, 3, 4, 7, 8, 9, 4, 5, 7, 8, 1, 3, 6, 7, 8, 0, 6, 8])




```python
randD[key]=3
randD
```




    array([[3, 3, 1, 1, 1, 1, 3, 3, 1, 1],
           [1, 3, 1, 3, 3, 1, 1, 1, 1, 3],
           [1, 3, 1, 1, 1, 3, 3, 3, 3, 1],
           [1, 3, 1, 3, 1, 1, 3, 3, 3, 3],
           [1, 3, 1, 3, 1, 1, 1, 3, 3, 1],
           [1, 1, 3, 1, 1, 3, 1, 1, 1, 1],
           [1, 1, 3, 3, 3, 1, 1, 3, 3, 3],
           [1, 1, 1, 1, 3, 3, 1, 3, 3, 1],
           [1, 3, 1, 3, 1, 1, 3, 3, 3, 1],
           [3, 1, 1, 1, 1, 1, 3, 1, 3, 1]])




```python
NofD=10
rD1=np.random.randint(NofD,size=NofD)
rD2=np.random.randint(2, NofD,size=NofD)
rD=rD2+rD1
mixAry=[np.arange(rD1[i],rD[i]) for i in range(0,len(rD2))]
edgL=[[mixAry[i][0],mixAry[i][-1]] for i in range(0,len(mixAry))]
edgAry=np.array(edgL)
```


```python
mixAry
```




    [array([2, 3, 4, 5, 6, 7, 8]),
     array([2, 3, 4, 5, 6, 7, 8]),
     array([8, 9]),
     array([ 9, 10, 11, 12, 13, 14]),
     array([2, 3, 4, 5]),
     array([ 3,  4,  5,  6,  7,  8,  9, 10, 11]),
     array([5, 6, 7, 8, 9]),
     array([ 9, 10]),
     array([ 8,  9, 10, 11, 12, 13, 14, 15, 16]),
     array([0, 1, 2, 3])]




```python
edgL
```




    [[2, 8],
     [2, 8],
     [8, 9],
     [9, 14],
     [2, 5],
     [3, 11],
     [5, 9],
     [9, 10],
     [8, 16],
     [0, 3]]




```python
edgAry
```




    array([[ 2,  8],
           [ 2,  8],
           [ 8,  9],
           [ 9, 14],
           [ 2,  5],
           [ 3, 11],
           [ 5,  9],
           [ 9, 10],
           [ 8, 16],
           [ 0,  3]])




```python
np.random.randint(0,2, size=(1,3))

```




    array([[0, 1, 0]])




```python
rD1=np.random.randint(NofD,size=(NofD,1))
rD1.tolist()
```




    [[3], [9], [9], [0], [1], [9], [1], [2], [7], [0]]




```python
rD2=np.random.randint(2, NofD,size=NofD)
rD2
```




    array([4, 6, 9, 4, 3, 6, 2, 4, 3, 4])




```python
rD1=np.random.randint(NofD,size=NofD)
rD2=np.random.randint(2, NofD,size=NofD)
rD=rD2+rD1
rD
```




    array([ 9,  8, 15,  9,  5,  8, 12, 17, 10, 17])




```python
mixAry=[np.arange(rD1[i],rD[i]) for i in range(0,len(rD2))]
mixAry
```




    [array([4, 5, 6, 7, 8]),
     array([6, 7]),
     array([ 6,  7,  8,  9, 10, 11, 12, 13, 14]),
     array([6, 7, 8]),
     array([0, 1, 2, 3, 4]),
     array([5, 6, 7]),
     array([ 3,  4,  5,  6,  7,  8,  9, 10, 11]),
     array([ 9, 10, 11, 12, 13, 14, 15, 16]),
     array([6, 7, 8, 9]),
     array([ 9, 10, 11, 12, 13, 14, 15, 16])]




```python
edgAry=[[mixAry[i][0],mixAry[i][-1]] for i in range(0,len(mixAry))]
edgAry
```




    [[4, 8],
     [6, 7],
     [6, 14],
     [6, 8],
     [0, 4],
     [5, 7],
     [3, 11],
     [9, 16],
     [6, 9],
     [9, 16]]




```python

List_new=[item for item in TargetG if item not in ClosedList]
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    /var/folders/mg/w5t8lkhc8xj79f001s7kzpfh0000gp/T/ipykernel_87611/3123364148.py in <module>
    ----> 1 List_new=[item for item in rDL_target if item not in rDL_clist]
    

    NameError: name 'rDL_target' is not defined



```python
list(set(['A','B','C','D']))
```




    ['A', 'B', 'C', 'D']




```python
list(set(['A','B','C','D'])-set(['A']))
```




    ['B', 'C', 'D']




```python
list(set(['S','B','A','D'])-set(['D','B']))
```




    ['S', 'A']


