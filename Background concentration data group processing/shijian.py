import pandas as pd
import os
# os.chdir('E:/python/data/123')
df = pd.read_csv("./123/545110-99999-2022.csv")
df['h'] = df['hour']+8
df['c'] = df['date']+df['h']//24
df['bj_h'] = df['h']%24
del df['date']
del df['h']
del df['hour']
df_id = df['c']
df = df.drop('c', axis=1)
df.insert(0, 'date', df_id)
df_id = df['bj_h']
df = df.drop('bj_h', axis=1)
df.insert(1, 'hour', df_id)
df.to_csv("./qx/qx_2022.csv")
print(df)
