import pandas as pd
import os
import numpy as np


# 筛选 all中的数据
path = ['F:/beijing_20180101-20181231',
        'F:/beijing_20190101-20191231',
        'F:/beijing_20200101-20201231',
        'F:/beijing_20210101-20211231',
        'F:/beijing_20220101-20220507', ]
for p in path:
    os.chdir(p)
    # 1.
    qidian = []  # pm25
    date = []  # 年月日
    pm_10 = []  # pm10
    index1 = []  # 小时
    time = [17, 18, 19]  # 需要筛选的时间
    for file in os.listdir(): # 遍历整个文件夹

        if 'all' in file:

            df = pd.read_csv(file)

            # print(df.columns.tolist())
            if '海淀万柳' in df.columns.tolist():
                df.rename(columns={'海淀万柳': '万柳'}, inplace=True)
            else:
                pass
            pm25 = df[df['type'] == 'PM2.5']  # pm2.5
            pm25_7 = pm25[pm25['hour'] == time[0]]
            pm25_8 = pm25[pm25['hour'] == time[1]]
            pm25_9 = pm25[pm25['hour'] == time[2]]

            pm10 = df[df['type'] == 'PM10']
            pm10_7 = pm10[pm10['hour'] == time[0]]
            pm10_8 = pm10[pm10['hour'] == time[1]]
            pm10_9 = pm10[pm10['hour'] == time[2]]

            if pm25_7['万柳'].shape[0] == 0 or pd.isnull(pm25_7['万柳'].values) == 1:  # 如果数据中有空值跳过当天
                continue
            elif pm25_8['万柳'].shape[0] == 0 or pd.isnull(pm25_8['万柳'].values) == 1:
                continue
            elif pm25_9['万柳'].shape[0] == 0 or pd.isnull(pm25_9['万柳'].values) == 1:
                continue
            elif pm10_7['万柳'].shape[0] == 0 or pd.isnull(pm10_7['万柳'].values) == 1:
                continue
            elif pm10_8['万柳'].shape[0] == 0 or pd.isnull(pm10_8['万柳'].values) == 1:
                continue
            elif pm10_9['万柳'].shape[0] == 0 or pd.isnull(pm10_9['万柳'].values) == 1:
                continue
            else:

                wl_pm25_7 = pm25_7['万柳']
                wl_pm25_8 = pm25_8['万柳']
                wl_pm25_9 = pm25_9['万柳']

                date.append(file.split('_', -1)[2].split('.', 1)[0])
                date.append(file.split('_', -1)[2].split('.', 1)[0])
                date.append(file.split('_', -1)[2].split('.', 1)[0])
                qidian.append(wl_pm25_7.values[0])
                qidian.append(wl_pm25_8.values[0])
                qidian.append(wl_pm25_9.values[0])
                pm_10.append(pm10_7['万柳'].values[0])
                pm_10.append(pm10_8['万柳'].values[0])
                pm_10.append(pm10_9['万柳'].values[0])
                index1.append(str(time[0]))
                index1.append(str(time[1]))
                index1.append(str(time[2]))

            # print(wl_pm25.values)

    print(qidian)
    print(date)
    df1 = pd.DataFrame(
        data={'date': date,
              'hour': index1,
              'PM2.5': qidian,
              'PM10': pm_10}
    )
    filename = 'res-' + str(time[0]) + str(time[1]) + str(time[2]) + '.csv'  # 文件夹名
    df1.to_csv(filename, index=None)  # 保存函数  ，其中index = None 作用：取消第一列自动生成的序号
