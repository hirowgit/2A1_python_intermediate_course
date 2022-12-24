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
# # @File    : lec3_step4.py 

```


```python
import numpy as np
import os
```


```python
datafol='ShippingData'
MasterF='ORDER_20201208_newClassNum_corr.csv'
Line_F='LOC_LINE.csv'
ProductivityF='PRODUCTIVITY.csv'
os.path.join(datafol, MasterF)
```




    'ShippingData/ORDER_20201208_newClassNum_corr.csv'




```python
pwd
```




    '/Users/hiro/Documents/github/2A1_python_intermediate_course'




```python
L_Info=np.loadtxt(os.path.join(datafol,Line_F), delimiter=',', dtype='int64')
# Mdat=np.loadtxt(fuos.path.joinllfile(datafol,MasterF))
# Prod_Info=np.loadtxt(os.path.join(datafol,ProductivityF))
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    /var/folders/mg/w5t8lkhc8xj79f001s7kzpfh0000gp/T/ipykernel_23638/3928839866.py in <module>
    ----> 1 L_Info=np.loadtxt(os.path.join(datafol,Line_F), delimiter=',', dtype='int64')
          2 # Mdat=np.loadtxt(fuos.path.joinllfile(datafol,MasterF))
          3 # Prod_Info=np.loadtxt(os.path.join(datafol,ProductivityF))


    /usr/local/lib/python3.9/site-packages/numpy/lib/npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin, encoding, max_rows, like)
       1065             fname = os_fspath(fname)
       1066         if _is_string_like(fname):
    -> 1067             fh = np.lib._datasource.open(fname, 'rt', encoding=encoding)
       1068             fencoding = getattr(fh, 'encoding', 'latin1')
       1069             fh = iter(fh)


    /usr/local/lib/python3.9/site-packages/numpy/lib/_datasource.py in open(path, mode, destpath, encoding, newline)
        191 
        192     ds = DataSource(destpath)
    --> 193     return ds.open(path, mode, encoding=encoding, newline=newline)
        194 
        195 


    /usr/local/lib/python3.9/site-packages/numpy/lib/_datasource.py in open(self, path, mode, encoding, newline)
        531                                       encoding=encoding, newline=newline)
        532         else:
    --> 533             raise IOError("%s not found." % path)
        534 
        535 


    OSError: ShippingData/LOC_LINE.csv not found.



```python

allData = np.loadtxt('ORDER_20201208.csv', delimiter=',', dtype='int64')
```


    ---------------------------------------------------------------------------

    OSError                                   Traceback (most recent call last)

    /var/folders/mg/w5t8lkhc8xj79f001s7kzpfh0000gp/T/ipykernel_23638/317202758.py in <module>
    ----> 1 allData = np.loadtxt('ORDER_20201208.csv', delimiter=',', dtype='int64')
    

    /usr/local/lib/python3.9/site-packages/numpy/lib/npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin, encoding, max_rows, like)
       1065             fname = os_fspath(fname)
       1066         if _is_string_like(fname):
    -> 1067             fh = np.lib._datasource.open(fname, 'rt', encoding=encoding)
       1068             fencoding = getattr(fh, 'encoding', 'latin1')
       1069             fh = iter(fh)


    /usr/local/lib/python3.9/site-packages/numpy/lib/_datasource.py in open(path, mode, destpath, encoding, newline)
        191 
        192     ds = DataSource(destpath)
    --> 193     return ds.open(path, mode, encoding=encoding, newline=newline)
        194 
        195 


    /usr/local/lib/python3.9/site-packages/numpy/lib/_datasource.py in open(self, path, mode, encoding, newline)
        531                                       encoding=encoding, newline=newline)
        532         else:
    --> 533             raise IOError("%s not found." % path)
        534 
        535 


    OSError: ORDER_20201208.csv not found.



```python

```
