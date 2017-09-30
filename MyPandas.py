import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import random as rd
import MyTime

# print(pd.__version__)

# a=np.random.rand(5)
# print(a)
# s=Series(a)
# print(s)
# print(s.index)
# s=Series(np.random.rand(3),index=['a','b','c'],name='my_series')
# print(s)
# print(s.index)
# print(s.name)
# d={'a':1.0,'b':2,'c':3}
# s=Series(d)
# print(s)
# s=Series(d,index=['c','d','a','b'])
# print(s)
# print(Series(2,index=[1,2,3,4]))

# s = Series(np.random.rand(10), index=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'i'])
# print(s)
# print(s['a'])
# print(s[:3])
# print(s[[2, 0, 4]])
# print(s[['b', 'd']])
# print(s[s > 0.5])
# print('e' in s)

# d = {'one': Series([1., 2, 3], index=['a', 'b', 'c']), 'two': Series([1., 2, 3, 4], index=['a', 'b', 'c', 'd'])}
# df = DataFrame(d)
# print(df)
# df=DataFrame(d,index=['r','d','a'],columns=['two','three'])
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
# d={'a':[1,2,3,4.],'b':[5,6,7,3.]}
# df=DataFrame(d,index=[1,2,3,4])
# print(df)
# d=[{'a':1,'b':2},{'b':1,'a':2,'c':3}]
# df=DataFrame(d)
# print(df)
# df=DataFrame()
# print(df)

# a = Series(range(5))
# b = Series(np.linspace(4, 20, 5))
# df = pd.concat([a, b], axis=1)
# print(a, '\n', b, '\n', df)
# df = pd.concat([a, b], axis=0)
# print(a, '\n', b, '\n', df)

# df = DataFrame()
# index = ['a', 'b', 'c', 'd', 'e']
# for i in range(5):
#     tempf = DataFrame([np.linspace(i, 5 * i, 5)], index=[index[i]])
#     print(tempf)
#     df = pd.concat([df, tempf], axis=0)
# print(df)
# print(df[1])
# print(type(df[1]))
# df.columns = ['a1', 'b2', 'c3', 'd4', 'e5']
# print(df)
# print(df['b2'])
# print(type(df['b2']))
# print(df.b2)
# print(df[['a1', 'c3']])
# print(type(df[['a1', 'c3']]))
# print(df['b2']['c'])
# print(df['b2'][2])
# print(df.loc['c'])
# print(df.iloc[2])

pd.set_option('display.width', 200)
# datas = pd.date_range('20150101', periods=5)
# print(datas)
# df = pd.DataFrame(np.random.randn(5, 4), index=datas, columns=list('ABCD'))

a = list()
b = list()
for i in range(7):
    a.append(MyTime.randomDateTimeStr('%Y-%m-%d'))
    b.append(MyTime.randomTimeStr('00:00:00', '23:59:59'))

df2 = pd.DataFrame({'A': a,
                    'B': b,
                    'C': pd.Series(1.6, index=list(range(7, 14))),
                    'D': np.array([4] * 7, dtype='int64'),
                    'E': 'hello world!',
                    'F': np.random.randn(7),
                    'G': np.arange(4., 11., 1)
                    })
print(df2)

# print(df2.head(2))
# print(df2.tail(3))
# print(df2.describe())
# print(df2.sort_index(axis=1, ascending=False).head())
# print(df2.sort_index(axis=0, ascending=False).head())
# print(df2.sort_values(by=['F'], axis=0, ascending=[True]).head())
# print(df2.sort_values(by=['F', 'G'], axis=0, ascending=[True, False]).head())
# print(df2.iloc[1:4][:])
# print(df2[df2.G > df2.G.mean()].head())
# print(df2[df2['G'].isin(['6', '10', '4'])].head())
# pd.set_option('chained_assignment', None)  # 去掉警告
# df2['E'][df2['G'] == 6] = np.nan
# df2['D'][df2['G'] == 6] = np.nan
# df2['C'][df2['G'] == 6] = np.nan
# df2['D'][df2['G'] == 5] = np.nan
# df2['C'][df2['G'] == 5] = np.nan
# df2['C'][df2['G'] == 4] = np.nan
# print(df2.head())
# print(df2.shape)
# print(df2.dropna().shape)
# print(df2.dropna())
# print(df2.dropna(how='any'))
# print(df2.dropna(how='all'))
# print(df2.dropna(axis=0,thresh=2))
# print(df2.dropna(axis=1,thresh=2))
# print(df2.dropna(subset=['E']))
# print(df2.dropna(subset=['G']))
# print(df2.fillna(value='补充值').head())
# print(df2.mean())
# print(df2.mean(0))
# print(df2.mean(1))
# print(df2.sum())
# print(df2.sum(0))
# print(df2.sum(1))
# print(df2['G'].value_counts().head())
# def pow(x):
#     return x * x
#
#
# df2['G'] = df2['G'].apply(pow)
# print(df2)

# dat1 = df2[['C', 'F', 'G']].head()
# dat2 = df2[['C', 'F', 'G']].iloc[2]
# dat3 = df2[['C', 'F', 'G']].loc[10]
# print(dat1)
# dat = dat1.append(dat2, ignore_index=True)
# dat = dat.append(dat3, ignore_index=True)
# print(dat)

# dat1 = df2[['B','C','F']]
# dat2 = df2[['B','C','G']]
# dat = dat1.merge(dat2,on=['B','C']) # 等价于 dat = df2[['B','C','F','G']]
# print(dat1.head())
# print(dat2.head())
# print(dat.head())

# df_grp = df2.groupby('A')
# grp_mean = df_grp.mean()
# print(grp_mean)

# print(df2.drop_duplicates(subset='A', keep='last'))

dat = df2[df2['F']>0].set_index('G')['F']
dat.plot(title='xxx')

# https://uqer.io/community/share/5514bb11f9f06c12790415b2
# isin()函数可方便地过滤DataFrame中的数据
