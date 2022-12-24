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
# # @File    : lec3_step2.py 
```


```python
import numpy as np
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
print(prFill)
```

    [0.9 0.6 0.5 0.5 0.5 0.9 0.4 0.3 0.8 0.4 0.2]



```python
a=[10,20,30]
print(a)
for d in a:
    print(d/10)
for i in range(len(a)):
    print(a[i]/10)
```

    [10, 20, 30]
    1.0
    2.0
    3.0
    1.0
    2.0
    3.0



```python
import numpy as np
#prFill=[90    60    50    50    50    90    40    30    80    40  20 ]/100;
prFill=np.array([90, 60, 50, 50, 50, 90, 40, 30, 80, 40, 20])
prFill=prFill/100
print(prFill)
```

    [0.9 0.6 0.5 0.5 0.5 0.9 0.4 0.3 0.8 0.4 0.2]



```python
# fillLine=boolean(ones(1,size(prFill,2)));
# を1行で書く方法
fillLine=np.full(len(prFill),True)
print(fillLine)
```

    [ True  True  True  True  True  True  True  True  True  True  True]



```python
# fillLine=boolean(ones(1,size(prFill,2)));
# を1行で書く方法
NofD=len(prFill)
fillLine=np.full(NofD,True)
print(fillLine)
```

    [ True  True  True  True  True  True  True  True  True  True  True]



```python
# fillLine=boolean(ones(1,size(prFill,2)));
# を1行で書く方法 :これは階層構造になるので、x
fillLine=np.full(( 1,len(prFill)),True)
print(fillLine)
```

    [[ True  True  True  True  True  True  True  True  True  True  True]]



```python
# 行で書く方法
fillLine2=np.empty(len(prFill), dtype = bool) 
fillLine2[:]=True  #スライシング機能
print(fillLine2)
```

    [ True  True  True  True  True  True  True  True  True  True  True]



```python
a=np.zeros((2,3))
print(a)
print(len(a))
print(a.size)
print(a.ndim)
print(a.shape)
```

    [[0. 0. 0.]
     [0. 0. 0.]]
    2
    6
    2
    (2, 3)



```python
b=np.argwhere(prFill>0.8)
print(b)
print(b.shape)
```

    [[0]
     [5]]
    (2, 1)



```python
prFill
```




    array([0.9, 0.6, 0.5, 0.5, 0.5, 0.9, 0.4, 0.3, 0.8, 0.4, 0.2])




```python
c=np.where(prFill>0.8)
print(c)
print(np.shape(c))
```

    (array([0, 5]),)
    (1, 2)



```python
np.argwhere((prFill>0.8) & fillLine)
```




    array([[0, 0],
           [0, 5]])




```python
fillLine[5]=False
np.where((prFill>0.8) & fillLine)
```




    (array([0]),)




```python
fillLine
```




    array([ True,  True,  True,  True,  True, False,  True,  True,  True,
            True,  True])




```python
prFill
```




    array([0.9, 0.6, 0.5, 0.5, 0.5, 0.9, 0.4, 0.3, 0.8, 0.4, 0.2])




```python
prFill[(prFill>0.8) ]
```




    array([0.9, 0.9])




```python
np.where((prFill>0.8) & (prFill>=0.8))
```




    (array([0, 5]),)




```python
b=np.where(np.logical_and(prFill>0.8,fillLine))
print(b)
print(len(b))
```

    (array([0, 5]),)
    1



```python
b2=np.unique(b)
print(b2)
```

    [0 5]



```python
b2[0]
```




    0




```python
print(fillLine[3:-1])

```

    [ True  True  True  True  True  True  True]



```python
i=3
np.where((prFill[i+1:-1]>0.8) & fillLine[i+1:-1])

```




    (array([1]),)




```python
i=3
remF=0.5
IDrem=np.where((prFill[i+1:-1]>remF) & fillLine[i+1:-1])
print(IDrem)
```

    (array([1, 4]),)



```python
a=np.empty(0)
print(a)
a.append([0,1])
print(a)
np.append(a,np.array([4])
print(a)
np.append(a,np.array([1,2,3])

```


      File "<ipython-input-134-26a9b3048070>", line 6
        print(a)
        ^
    SyntaxError: invalid syntax




```python
a=[]
print(a)
a.append([0,1])
print(a)
a.append([1,2,3])
print(a)
```

    []
    [[0, 1]]
    [[0, 1], [1, 2, 3]]



```python
gg=[[1,2],[0,1,2],[5]]
print(gg)
print(gg[0])
gg.append([1,2,1,1,3])
print(gg)
```

    [[1, 2], [0, 1, 2], [5]]
    [1, 2]
    [[1, 2], [0, 1, 2], [5], [1, 2, 1, 1, 3]]



```python
np.array([[1,2,3],[4,5,6]])
```




    array([[1, 2, 3],
           [4, 5, 6]])




```python
np.array([[1,2,3],[4,5]])
```

    /var/folders/mg/w5t8lkhc8xj79f001s7kzpfh0000gp/T/ipykernel_46824/4191096310.py:1: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
      np.array([[1,2,3],[4,5]])





    array([list([1, 2, 3]), list([4, 5])], dtype=object)




```python
np.array([['a','a'],['b','b']])
```




    array([['a', 'a'],
           ['b', 'b']], dtype='<U1')




```python
np.array([['a','a'],['b','b','c']])
```

    /var/folders/mg/w5t8lkhc8xj79f001s7kzpfh0000gp/T/ipykernel_46824/3154860643.py:1: VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. If you meant to do this, you must specify 'dtype=object' when creating the ndarray.
      np.array([['a','a'],['b','b','c']])





    array([list(['a', 'a']), list(['b', 'b', 'c'])], dtype=object)




```python
d=[[1,2,3],[4,5]]
print(d)
```

    [[1, 2, 3], [4, 5]]



```python
d[0]
```




    [1, 2, 3]




```python
d[0][2]
```




    3




```python
[['a','a'],['b','b','c']]
```




    [['a', 'a'], ['b', 'b', 'c']]




```python
c=['aa','bbc']
print(c)
```

    ['aa', 'bbc']



```python
c[0]
```




    'aa'




```python
c[1][2]
```




    'c'




```python
import sympy as sym
```


```python
A =sym.MatrixSymbol('a',2,2)
b =sym.MatrixSymbol('b',2,1)
A.as_explicit()
```




$\displaystyle \left[\begin{matrix}a_{0, 0} & a_{0, 1}\\a_{1, 0} & a_{1, 1}\end{matrix}\right]$




```python
b.as_explicit()
```




$\displaystyle \left[\begin{matrix}b_{0, 0}\\b_{1, 0}\end{matrix}\right]$




```python
y=A*b
y.as_explicit()
```




$\displaystyle \left[\begin{matrix}a_{0, 0} b_{0, 0} + a_{0, 1} b_{1, 0}\\a_{1, 0} b_{0, 0} + a_{1, 1} b_{1, 0}\end{matrix}\right]$




```python
sym.init_printing
```




    <function sympy.interactive.printing.init_printing(pretty_print=True, order=None, use_unicode=None, use_latex=None, wrap_line=None, num_columns=None, no_global=False, ip=None, euler=False, forecolor=None, backcolor='Transparent', fontsize='10pt', latex_mode='plain', print_builtin=True, str_printer=None, pretty_printer=None, latex_printer=None, scale=1.0, **settings)>




```python
A=sym.Matrix([[1, 2], [3, 4]])
A
```




$\displaystyle \left[\begin{matrix}1 & 2\\3 & 4\end{matrix}\right]$




```python
b=sym.Matrix([[5], [6]])
b
```




$\displaystyle \left[\begin{matrix}5\\6\end{matrix}\right]$




```python
A*b
```




$\displaystyle \left[\begin{matrix}17\\39\end{matrix}\right]$




```python
sym.MatrixSymbol('a',2,2)*sym.MatrixSymbol('b',2,1)[1]
```




$\displaystyle b_{1, 0} a$




```python

```
