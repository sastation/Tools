#!/usr/bin/env python
# coding: utf-8

'''
pandas 模块练习
'''

from pandas import Series, DataFrame
import pandas as pd 
import numpy as np

# 生成列表
## 从随机数中生成列表
di = {k:np.random.randn(10) for k in ["a", "b", "c", "d"]}
df = pd.DataFrame(di)

## 从 csv 文件中生成列表
f_csv = './test.csv'
df = pd.read_csv(f_csv)

## 从 excel 中读取列表
f_xls = ExcelFile('test.xlsx')
f_xls.parse('sheet1', index_col=None, na_values=['NA'])

# 转换
df.to_dict(outtype='dict') # outtype = [dict|list|series|records]

# 查询
df.head()
df.tail()
df.index
df.columns
df.values
df.describe() #decribe方法可以计算各个列的基本描述统计值。包含计数，平均数，标准差，最大值，最小值及4分位差。

# 行列转换
df.T

# 排序
df.sort_index(axis=1, ascending=False)
df.sort(columns=['a', 'b'], ascending=[0,1])

cols = df.columns
## df.loc 只可以通过行列标签进行查询
for idx in df.index:
    for col in cols:
        print df.loc[idx, col],
    print

## df.iloc 只可以通过行列编号进行查询
for i in range(0, len(df)):
    for j in range(0, len(cols)):
        print df.iloc[i, j],
    print 

## df.ix 可以通过行列标签，也可以通过行列编号进行查询
for idx in df.index:
    for col in cols:
        print df.ix[idx, col],
    print 

# 遍历
## Iterate over DataFrame rows as namedtuples, with index value as first element of the tuple.
for row in df.itertuples():
###for row in df.itertuples(index=False, name=None):
    ### print row
    ### print row.a, row.b, row.c, row.d
    for i in row:
        print i

## Iterate over DataFrame rows as (index, Series) pairs.
for idx, row in df.iterrows():
    print idx
    print row['a'], row['b'], row['c'], row['d']
    
## Iterate over (column name, Series) pairs
for col, list in df.iteritems():
    print col
    for val in list:
        print val,
    print

# 筛选
