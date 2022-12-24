```python
## Python basics for novice data scientists, supported by Wagatsuma Lab@Kyutech 
#
# The MIT License (MIT): Copyright (c) 2022 Hiroaki Wagatsuma and Wagatsuma Lab@Kyutech
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. */
#
# # @Time    : 2022-8-10 
# # @Author  : Hiroaki Wagatsuma
# # @Site    : https://github.com/hirowgit/2A1_python_intermediate_course
# # @IDE     : Python 3.9.13 (main, Aug  7 2022, 01:33:23)  [Clang 13.1.6 (clang-1316.0.21.2.5)] on darwin
# # @File    : lec3_step1.py 
```


```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
```


```python
allData = np.loadtxt('allData200.csv', delimiter=',', dtype='int64')
allData
```


```python
import pandas as pd

df = pd.read_csv('allData200.csv',delimiter=',', dtype='int64')
print(df)
```

         9   7   3   5  6   2  8   4  1  10
    0    6   4  10   7  9   3  8   5  1   2
    1    4   3   6   2  7   5  9  10  1   8
    2    3   6   7   4  1   8  2   5  9  10
    3    1  10   4   8  7   6  3   5  2   9
    4    7   8   9   2  3   4  5  10  1   6
    ..  ..  ..  ..  .. ..  .. ..  .. ..  ..
    194  6  10   3   7  8   9  4   5  2   1
    195  8   1   5  10  6   4  2   7  9   3
    196  3   4   1  10  5   9  6   2  7   8
    197  6   7   3   2  5  10  1   8  9   4
    198  9   8   5   3  4   1  2  10  7   6
    
    [199 rows x 10 columns]



```python
df_tsv = pd.read_table('part2_Interface_definition_code_data_fullENG.csv', index_col=0)
print(df_tsv)


```

    Empty DataFrame
    Columns: []
    Index: [,1-1,Distribution_line_slot_configuration_data,,6,,6,[LINE.csv], ,No,Item,Type,Number of digits,Type,Number of digits,Remarks, ,1,Line_number,Number,2,Number,2,, ,2,Number_of_upper_slots,Number,2,Number,2,, ,3,Number_of_lower_slots,Number,2,Number,2,, ,,,,,,,, ,,,,,,,, ,1-2,Order_data,,40,,40,[ORDER.csv], ,No,Item,Type,Number of digits,Type,Number of digits,Remarks, ,1,Center_code,Number,2,Number,2,, ,2,Company_code,Number,4,Number,4,, ,3,Division_code,Number,2,Number,2,, ,4,Store_code,Number,3,Number,3,, ,5,Carry-in_regulations,Number,1,Number,1,, ,6,Shipping_priority,Number,2,Number,2,, ,7,Delivery_time_limit,Number,4,Number,4,, ,8,Regular_special_sale,Number,1,Number,1,, ,9,Sorting_classification_code,Number,2,Number,2,, ,10,Product_code,Number,13,Number,13,, ,11,Shipping_packing,Number,1,Number,1,, ,12,Number_of_orders,Number,"4,1",Number,"4,1",, ,13,Total_Action_Step,Number,5,Number,5,, ,,,,,,,, ,,,,,,,, ,1-3,Productivity_data,,8,,8,[PRODUCTIVITY.csv], ,No,Item,Type,Number of digits,Type,Number of digits,, ,1,Work_start_time,Number,4,Number,4,, ,2,Action_step,Number,4,Number,4,, ,,,,,,,, ,,,,,,,, ,,,,,,,, 2. Output file,,,,,,,, ,2-1,Execution_result,,41,,41,[STATUS.csv], ,No,Item,Type,Number of digits,Type,Number of digits,, ,1,Completion_code,Number,1,Number,1,, ,2,Error_message,letter,40,letter,40,, ,,,,,,,, ,,,,,,,, ,2-2,Execution_result,,64,,64,[SETTING.csv], ,No,Item,Type,Number of digits,Type,Number of digits,Remarks, ,1,Sequencing_No,Number,2,Number,2,, ,2,Allocation_line_No,Number,2,Number,2,, ,3,Slot_allocation_No,Number,2,Number,2,, ,4,Center_code,Number,2,Number,2,, ,5,Company_code,Number,4,Number,4,, ,6,Division_code,Number,2,Number,2,, ,7,Store_code,Number,3,Number,3,, ,8,Carry-in_regulations,Number,1,Number,1,, ,9,Regular_special_sale,Number,1,Number,1,, ,10,Sorting_classification_code,Number,2,Number,2,, ,11,Slot_division,Number,1,Number,1,, ,12,Total_number_of_ActionSteps,Number,5,Number,5,, ,13,Total_number_of_balls,Number,5,Number,5,, ,14,Total_number_of_pieces,Number,5,Number,5,, ,15,Total_number_of_bags,Number,5,Number,5,, ,16,Total_halves,Number,5,Number,5,, ,17,Line_ActionStep_number,Number,7,Number,7,, ,18,Line_ActionStep_average_ratio,Number,3,Number,3,, ,19,Assumed_work_time,Number,7,Number,7,]



```python
df_tsv = pd.read_table('part2_Interface_definition_code_data_fullENG.csv')
print(df_tsv)


```

                                     1. Input file,,,,,,,
    0   ,1-1,Distribution_line_slot_configuration_data...
    1   ,No,Item,Type,Number of digits,Type,Number of ...
    2                   ,1,Line_number,Number,2,Number,2,
    3         ,2,Number_of_upper_slots,Number,2,Number,2,
    4         ,3,Number_of_lower_slots,Number,2,Number,2,
    5                                             ,,,,,,,
    6                                             ,,,,,,,
    7                 ,1-2,Order_data,,40,,40,[ORDER.csv]
    8   ,No,Item,Type,Number of digits,Type,Number of ...
    9                   ,1,Center_code,Number,2,Number,2,
    10                 ,2,Company_code,Number,4,Number,4,
    11                ,3,Division_code,Number,2,Number,2,
    12                   ,4,Store_code,Number,3,Number,3,
    13         ,5,Carry-in_regulations,Number,1,Number,1,
    14            ,6,Shipping_priority,Number,2,Number,2,
    15          ,7,Delivery_time_limit,Number,4,Number,4,
    16         ,8,Regular_special_sale,Number,1,Number,1,
    17  ,9,Sorting_classification_code,Number,2,Number,2,
    18              ,10,Product_code,Number,13,Number,13,
    19            ,11,Shipping_packing,Number,1,Number,1,
    20    ,12,Number_of_orders,Number,"4,1",Number,"4,1",
    21           ,13,Total_Action_Step,Number,5,Number,5,
    22                                            ,,,,,,,
    23                                            ,,,,,,,
    24    ,1-3,Productivity_data,,8,,8,[PRODUCTIVITY.csv]
    25  ,No,Item,Type,Number of digits,Type,Number of ...
    26              ,1,Work_start_time,Number,4,Number,4,
    27                  ,2,Action_step,Number,4,Number,4,
    28                                            ,,,,,,,
    29                                            ,,,,,,,
    30                                            ,,,,,,,
    31                              2. Output file,,,,,,,
    32         ,2-1,Execution_result,,41,,41,[STATUS.csv]
    33  ,No,Item,Type,Number of digits,Type,Number of ...
    34              ,1,Completion_code,Number,1,Number,1,
    35              ,2,Error_message,letter,40,letter,40,
    36                                            ,,,,,,,
    37                                            ,,,,,,,
    38        ,2-2,Execution_result,,64,,64,[SETTING.csv]
    39  ,No,Item,Type,Number of digits,Type,Number of ...
    40                ,1,Sequencing_No,Number,2,Number,2,
    41           ,2,Allocation_line_No,Number,2,Number,2,
    42           ,3,Slot_allocation_No,Number,2,Number,2,
    43                  ,4,Center_code,Number,2,Number,2,
    44                 ,5,Company_code,Number,4,Number,4,
    45                ,6,Division_code,Number,2,Number,2,
    46                   ,7,Store_code,Number,3,Number,3,
    47         ,8,Carry-in_regulations,Number,1,Number,1,
    48         ,9,Regular_special_sale,Number,1,Number,1,
    49  ,10,Sorting_classification_code,Number,2,Numbe...
    50               ,11,Slot_division,Number,1,Number,1,
    51  ,12,Total_number_of_ActionSteps,Number,5,Numbe...
    52       ,13,Total_number_of_balls,Number,5,Number,5,
    53      ,14,Total_number_of_pieces,Number,5,Number,5,
    54        ,15,Total_number_of_bags,Number,5,Number,5,
    55                ,16,Total_halves,Number,5,Number,5,
    56      ,17,Line_ActionStep_number,Number,7,Number,7,
    57  ,18,Line_ActionStep_average_ratio,Number,3,Num...
    58           ,19,Assumed_work_time,Number,7,Number,7,



```python
df_tsv = pd.read_csv('part2_Interface_definition_code_data_fullENG.csv')
print(df_tsv)

```

         1. Input file Unnamed: 1                                 Unnamed: 2  \
    0              NaN        1-1  Distribution_line_slot_configuration_data   
    1              NaN         No                                       Item   
    2              NaN          1                                Line_number   
    3              NaN          2                      Number_of_upper_slots   
    4              NaN          3                      Number_of_lower_slots   
    5              NaN        NaN                                        NaN   
    6              NaN        NaN                                        NaN   
    7              NaN        1-2                                 Order_data   
    8              NaN         No                                       Item   
    9              NaN          1                                Center_code   
    10             NaN          2                               Company_code   
    11             NaN          3                              Division_code   
    12             NaN          4                                 Store_code   
    13             NaN          5                       Carry-in_regulations   
    14             NaN          6                          Shipping_priority   
    15             NaN          7                        Delivery_time_limit   
    16             NaN          8                       Regular_special_sale   
    17             NaN          9                Sorting_classification_code   
    18             NaN         10                               Product_code   
    19             NaN         11                           Shipping_packing   
    20             NaN         12                           Number_of_orders   
    21             NaN         13                          Total_Action_Step   
    22             NaN        NaN                                        NaN   
    23             NaN        NaN                                        NaN   
    24             NaN        1-3                          Productivity_data   
    25             NaN         No                                       Item   
    26             NaN          1                            Work_start_time   
    27             NaN          2                                Action_step   
    28             NaN        NaN                                        NaN   
    29             NaN        NaN                                        NaN   
    30             NaN        NaN                                        NaN   
    31  2. Output file        NaN                                        NaN   
    32             NaN        2-1                           Execution_result   
    33             NaN         No                                       Item   
    34             NaN          1                            Completion_code   
    35             NaN          2                              Error_message   
    36             NaN        NaN                                        NaN   
    37             NaN        NaN                                        NaN   
    38             NaN        2-2                           Execution_result   
    39             NaN         No                                       Item   
    40             NaN          1                              Sequencing_No   
    41             NaN          2                         Allocation_line_No   
    42             NaN          3                         Slot_allocation_No   
    43             NaN          4                                Center_code   
    44             NaN          5                               Company_code   
    45             NaN          6                              Division_code   
    46             NaN          7                                 Store_code   
    47             NaN          8                       Carry-in_regulations   
    48             NaN          9                       Regular_special_sale   
    49             NaN         10                Sorting_classification_code   
    50             NaN         11                              Slot_division   
    51             NaN         12                Total_number_of_ActionSteps   
    52             NaN         13                      Total_number_of_balls   
    53             NaN         14                     Total_number_of_pieces   
    54             NaN         15                       Total_number_of_bags   
    55             NaN         16                               Total_halves   
    56             NaN         17                     Line_ActionStep_number   
    57             NaN         18              Line_ActionStep_average_ratio   
    58             NaN         19                          Assumed_work_time   
    
       Unnamed: 3        Unnamed: 4 Unnamed: 5        Unnamed: 6  \
    0         NaN                 6        NaN                 6   
    1        Type  Number of digits       Type  Number of digits   
    2      Number                 2     Number                 2   
    3      Number                 2     Number                 2   
    4      Number                 2     Number                 2   
    5         NaN               NaN        NaN               NaN   
    6         NaN               NaN        NaN               NaN   
    7         NaN                40        NaN                40   
    8        Type  Number of digits       Type  Number of digits   
    9      Number                 2     Number                 2   
    10     Number                 4     Number                 4   
    11     Number                 2     Number                 2   
    12     Number                 3     Number                 3   
    13     Number                 1     Number                 1   
    14     Number                 2     Number                 2   
    15     Number                 4     Number                 4   
    16     Number                 1     Number                 1   
    17     Number                 2     Number                 2   
    18     Number                13     Number                13   
    19     Number                 1     Number                 1   
    20     Number               4,1     Number               4,1   
    21     Number                 5     Number                 5   
    22        NaN               NaN        NaN               NaN   
    23        NaN               NaN        NaN               NaN   
    24        NaN                 8        NaN                 8   
    25       Type  Number of digits       Type  Number of digits   
    26     Number                 4     Number                 4   
    27     Number                 4     Number                 4   
    28        NaN               NaN        NaN               NaN   
    29        NaN               NaN        NaN               NaN   
    30        NaN               NaN        NaN               NaN   
    31        NaN               NaN        NaN               NaN   
    32        NaN                41        NaN                41   
    33       Type  Number of digits       Type  Number of digits   
    34     Number                 1     Number                 1   
    35     letter                40     letter                40   
    36        NaN               NaN        NaN               NaN   
    37        NaN               NaN        NaN               NaN   
    38        NaN                64        NaN                64   
    39       Type  Number of digits       Type  Number of digits   
    40     Number                 2     Number                 2   
    41     Number                 2     Number                 2   
    42     Number                 2     Number                 2   
    43     Number                 2     Number                 2   
    44     Number                 4     Number                 4   
    45     Number                 2     Number                 2   
    46     Number                 3     Number                 3   
    47     Number                 1     Number                 1   
    48     Number                 1     Number                 1   
    49     Number                 2     Number                 2   
    50     Number                 1     Number                 1   
    51     Number                 5     Number                 5   
    52     Number                 5     Number                 5   
    53     Number                 5     Number                 5   
    54     Number                 5     Number                 5   
    55     Number                 5     Number                 5   
    56     Number                 7     Number                 7   
    57     Number                 3     Number                 3   
    58     Number                 7     Number                 7   
    
                Unnamed: 7  
    0           [LINE.csv]  
    1              Remarks  
    2                  NaN  
    3                  NaN  
    4                  NaN  
    5                  NaN  
    6                  NaN  
    7          [ORDER.csv]  
    8              Remarks  
    9                  NaN  
    10                 NaN  
    11                 NaN  
    12                 NaN  
    13                 NaN  
    14                 NaN  
    15                 NaN  
    16                 NaN  
    17                 NaN  
    18                 NaN  
    19                 NaN  
    20                 NaN  
    21                 NaN  
    22                 NaN  
    23                 NaN  
    24  [PRODUCTIVITY.csv]  
    25                 NaN  
    26                 NaN  
    27                 NaN  
    28                 NaN  
    29                 NaN  
    30                 NaN  
    31                 NaN  
    32        [STATUS.csv]  
    33                 NaN  
    34                 NaN  
    35                 NaN  
    36                 NaN  
    37                 NaN  
    38       [SETTING.csv]  
    39             Remarks  
    40                 NaN  
    41                 NaN  
    42                 NaN  
    43                 NaN  
    44                 NaN  
    45                 NaN  
    46                 NaN  
    47                 NaN  
    48                 NaN  
    49                 NaN  
    50                 NaN  
    51                 NaN  
    52                 NaN  
    53                 NaN  
    54                 NaN  
    55                 NaN  
    56                 NaN  
    57                 NaN  
    58                 NaN  



```python

```
