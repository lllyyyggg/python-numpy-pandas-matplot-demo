import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# np_array = np.array([
#     [1, 2, 3],
#     [3, 4, 5]
# ])
# print(np_array)
# print(np_array.reshape((3, 2)))


# np_array2 = np.linspace(1, 10, 6)
# print(np_array2)
# print(np_array2.reshape((6, 1)))


# X = np.arange(2, 14).reshape(3, 4)

# print(X)
# print(np.argmin(X))
# print(np.mean(X))
# print(np.average(X))
# print(np.median(X))
# print(np.cumsum(X, axis=0))  # 0表示列， 1表示行
# print(np.diff(X))
# print(np.nonzero(X))
# print(np.clip(X, 6, 7))

# a = np.array([1, 2, 3, 4])[:, np.newaxis]
# b = np.array([4, 3, 2, 1])[:, np.newaxis]
# print(a, b)
# print(np.vstack((a, b)))
# print(np.hstack((a, b)))
# print(np.concatenate((a, b, b, a), axis=1))

# A = np.arange(12).reshape((3, 4))
# print(A)
# print(np.split(A, 3, axis=1))
# print(np.array_split(A, 3, axis=1))
# print(np.vsplit(A, 3))
# print(np.hsplit(A, 2))

# c = np.copy(a)
# print(c)

# s = pd.Series([1, 2, 6, np.nan, 44 , 11])
# print(s)


# dates = pd.date_range("2019-01-15", periods=6)
# print(dates)

# df = pd.DataFrame(np.arange(24).reshape(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
# print(df)
# print(df.index)
# print(df.columns)
# print(df.values)
# print(df.describe())
# print(df.T)
# print(df.T.sort_index(axis=0, ascending=False))
# print(df.sort_values(by='a'))

# print(df['A'])
# print(df.A)
# print(df[0: 3])
# print(df["2019-01-17": "2019-01-20"])
# print(df.loc['2019-01-17'])
# print(df.loc['2019-01-17', ['A', 'B']])

# print(df.iloc[3, 1])
# print(df.iloc[[1, 2, 3], 1: 3])

# print(df.ix[:3, ['A', 'B']])
# print(df[df['A'] > 6])


# df.iloc[0, 0] = 1111
# df['A'][df['A'] == 1111] = 0
# df['F'] = np.nan
# df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index=dates)
# print(df)


# dates = pd.date_range("20190118", periods=6)
# df2 = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])
# df2.iloc[0, 1] = np.nan
# df2.iloc[1, 2] = np.nan
# print(df2)
# print(df2.dropna(axis=0, how="any"))
# print(df2.dropna(axis=1, how="any"))


# print(df2.fillna(value=0))
# print(df2.isnull())
# print(np.any(df2.isnull()) == True)


# data = pd.read_csv('student.csv')
# print(data)
# data.to_pickle('student.pickle')
# data = pd.read_pickle('student.pickle')
# print(data)


# concatenating

# df3 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'])
df4 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['A', 'B', 'C', 'D'])
# df5 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['A', 'B', 'C', 'D'])
# print(df3)
# print(df4)
# print(df5)


# mixed = pd.concat([df3, df4, df5], axis=0, ignore_index=True)
# print(mixed)


# df6 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['A', 'B', 'C', 'D'], index=[1, 2, 3])
# df7 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['B', 'C', 'D', 'E'], index=[2, 3, 4])
# print(df6)
# print(df7)

# mixed = pd.concat([df6, df7], axis=1, join_axes=[df6.index])
# print(mixed)

# print(df6.append([df7], ignore_index=True))

# s1 = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
# print(df6.append(s1, ignore_index=True))
# print(df6)

# merge

# left = pd.DataFrame({
#     'key': ['K0', 'K1', 'K2', 'K3'],
#     'A': ['A0', 'A1', 'A2', 'A3'],
#     'B': ['B0', 'A1', 'B2', 'B3']
# })
#
# right = pd.DataFrame({
#     'key': ['K0', 'K4', 'K2', 'K3'],
#     'C': ['C0', 'C1', 'C2', 'C3'],
#     'D': ['D0', 'D1', 'D2', 'D3']
# })

# print(left)
# print(right)
# res = pd.merge(left, right, on=['key'], how='left')
# print(res)


# data = pd.Series(np.random.randn(1000), index=np.arange(1000))
# data = data.cumsum()
# print(data)
# data.plot()
# plt.show()
# data = pd.DataFrame(np.random.random((1000, 4)), index=np.arange(1000), columns=list("ABCD"))
# ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
# data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)

# plt.show()
