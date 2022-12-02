import pandas as pd
import numpy as np
import os
import time

# 先将气象文件转换txt，txt转为csv

root_path = 'C:/Users/Witt_N/Documents/WeChat Files/wxid_5858028580012/FileStorage/File/2022-05/中国气象数据/中国气象数据'
os.chdir(root_path)
for root, dirs, files in os.walk(root_path):
    for f in files:
        os.renames(os.path.join(root, f), os.path.join(root, f) + '.txt')

time.sleep(20)  # 等待上边的处理完
for root, dirs, files in os.walk(root_path):
    for f in files:
        txt = np.loadtxt(os.path.join(root, f))
        print(txt.ndim)
        if txt.ndim == 1:
            txt = np.array([txt])
        print(txt.shape[1])
        df = pd.DataFrame(txt)
        df['date'] = df[0] * 10000 + df[1] * 100 + df[2]
        del df[0], df[1], df[2]
        df.columns = ['hour', '气温', '露点', '海平面气压', '风向', '风速', ' Sky Condition Total Coverage Code',
                      'Liquid Precipitation Depth', 'Liquid Precipitation Depth', 'date']  # 重新定义列索引
        # 更换date的位置
        df_id = df['date']
        df = df.drop('date', axis=1)
        df.insert(0, 'date', df_id)
        # 保存函数
        df.to_csv(os.path.join(root, f).split('.', 2)[0] + '.csv', encoding='utf-8', index=None)
