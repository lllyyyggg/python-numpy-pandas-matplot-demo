import numpy as np
import pandas as pd

# 通过不同的方式创建数组
# np_array = np.array([1, 2, 3])
# np_array2 = np.arange(4, 7)
# print(np_array)
# print(np_array2)
# print(np_array * np_array2)
# print(np.dot(np_array, np_array2))


# array的一些操作
# X = np.arange(1, 16).reshape(3, 5)
# print(X)
# print('argmin: %s' % np.argmin(X))
# print('argmax: %s' % np.argmax(X))
# print('max: %s' % np.max(X))
# print('median: %s' % np.median(X))
# print('nonezero: {0}'.format(np.nonzero(X)))
# print('clip: \n{0}'.format(np.clip(X, 7, 9)))
# print('cumsum: {0}'.format(np.cumsum(X, axis=0)))

# 堆叠
# a = np.arange(1, 5)
# b = np.arange(5, 9)
# print(a, b)
# print('vstack:\n {0}'.format(np.vstack((a, b))))
# print('hstack: {0}'.format(np.hstack((a, b))))

# 拷贝
# a = np.array([{'name': 'lanyage'}, 2, 3, 4])
# b = a
# b[0]['name'] = 'Leo'


# 分裂
# A = np.arange(12).reshape(3, 4)
# print(A)
# print(np.split(A, 3, axis=0))
# print(np.array_split(A, 3, axis=1))
# print(np.hsplit(A, 2))
# print(np.vsplit(A, 3))


# pandas Serial
# pd_serial = pd.Series([1, 2, 6], index=[3, 2, 1])
# print(pd_serial)

# pandas DataFrame
# pd_dates = pd.date_range(start='20180808', periods=2, normalize=True)
# pd_dataframe = pd.DataFrame(data=np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3), index=pd_dates, columns=np.arange(3))
# print(pd_dataframe)
# pandas DataFrame的一些操作
# print(pd_dataframe.index)
# print(pd_dataframe.columns)
# print(pd_dataframe.values)
# print(pd_dataframe.describe())
# print(pd_dataframe.T)
# print(pd_dataframe.sort_index(axis=0, ascending=False))
# print(pd_dataframe.sort_values(by=0, ascending=False))


# pandas 索引
# pd_dates = pd.date_range(start='20180808', periods=3, normalize=True)
# pd_dataframe
# = pd.DataFrame(data=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3), index=pd_dates, columns=np.arange(1, 4))
# print(pd_dataframe)
# print(pd_dataframe[0])
# print(pd_dataframe[0: 2])
# print(pd_dataframe['2018-08-08': '2018-08-10'])
# print(pd_dataframe.iloc[1, 2])
# print(pd_dataframe.iloc[:, 1: 3])
# print(pd_dataframe.ix[:, 1: 3])
# print(pd_dataframe[pd_dataframe[2] > 3])


# pandas 处理nan值
# pd_dates = pd.date_range(start='20180808', periods=3, normalize=True)
# pd_dataframe = pd.DataFrame(data=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape(3, 3), index=pd_dates,
#                             columns=np.arange(1, 4))
# pd_dataframe.iloc[0, 0] = np.nan
# pd_dataframe.iloc[1, 1] = np.nan
# print(pd_dataframe)
# print(pd_dataframe.dropna(axis=0))
# print(pd_dataframe.dropna(axis=1))
# print(pd_dataframe.fillna(value=0))
# pd_dataframe[4] = np.nan
# 给DataFrame添加列
# pd_dataframe[5] = pd.Series(data=np.arange(3), index=pd_dates)
# print(pd_dataframe)
# print(np.any(pd_dataframe.isnull()) == True)
# print(np.all(pd_dataframe.isnull()) == True)


# pandas 读取文件
# pd_dataframe2 = pd.read_csv('student.csv')
# print(pd_dataframe2)
# pd_dataframe2.to_pickle('students.pickle')
# print(pd.read_pickle('students.pickle'))

# pandas堆叠
# pd_dataframe3 = pd.DataFrame(np.ones((3, 4)) * 0, columns=np.arange(1, 5))
# pd_dataframe4 = pd.DataFrame(np.ones((3, 4)) * 1, columns=np.arange(1, 5))
# pd_dataframe5 = pd.DataFrame(np.ones((3, 4)) * 2, columns=np.arange(1, 5))
# print(pd_dataframe3)
# print(pd_dataframe4)
# print(pd_dataframe5)
# mixed = pd.concat([pd_dataframe3, pd_dataframe4, pd_dataframe5], axis=0, ignore_index=True)
# print(mixed)

# pd_dataframe3 = pd.DataFrame(np.ones((3, 4)) * 0, columns=np.arange(1, 5))
# pd_dataframe4 = pd.DataFrame(np.ones((3, 4)) * 1, columns=np.arange(2, 6))
# print(pd.concat([pd_dataframe3, pd_dataframe4], axis=0, ))






