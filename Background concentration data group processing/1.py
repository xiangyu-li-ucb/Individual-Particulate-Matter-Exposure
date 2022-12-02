import pandas as pd


# 合并用的
df1 = pd.read_csv('./11-13/res-111213.csv')
df2 = pd.read_csv('qxi_2018-2022.csv')
df2.columns = ['date', 'hour', '气温', '露点', '海平面气压', '风向', '风速', ' Sky Condition Total Coverage Code',
               'Liquid Precipitation Depth', 'Liquid Precipitation Depth']
print(df1.shape)
df1['c'] = df1['date'] * 100 + df1['hour']  # 通过共同的'c'合并表格
df2['c'] = df2['date'] * 100 + df2['hour']
print(df2.columns.values)
print(df1.columns.values)

df = pd.merge(df1, df2, on='c', how='inner')  # merge合并函数 inner内连接--取交集
del df['c']  # 删除多余的列
del df['date_y']
del df['hour_y']

# print(df)
df = df[df['date_x'] > 20180101]  # 20180101数据缺少7-8-9
df.rename(columns={'date_x': 'date'}, inplace=True)  # 更换列名
df.rename(columns={'hour_x': 'hour'}, inplace=True)
df['气温'] = df['气温'] / 10  # 温度有温度因子
df.to_csv('./end/all-111213.csv', index=None)
