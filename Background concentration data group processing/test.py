import pandas as pd  # 库函数用来处理csv
import os
import numpy as np

# 筛选 extra中的数据
path = ['F:/beijing_20180101-20181231',
        'F:/beijing_20190101-20191231',
        'F:/beijing_20200101-20201231',
        'F:/beijing_20210101-20211231',
        'F:/beijing_20220101-20220507', ]
for p in path:
    os.chdir(p)
    date = []   # 时间列表
    so2 = []
    no2 = []
    o3 = []
    co = []
    index1 = []
    time = [11, 12, 13]  # 需要筛选的时间
    for file in os.listdir():  # 遍历整个文件夹

        if 'extra' in file:

            df = pd.read_csv(file)

            print(df.columns.tolist())
            if '海淀万柳' in df.columns.tolist():
                df.rename(columns={'海淀万柳': '万柳'}, inplace=True)  # 有些数据中是海淀万柳，有些是万柳，全部替换为万柳
            else:
                pass
            # print(df)
            so_2 = df[df['type'] == 'SO2']  # pm2.5
            # print(pm25)
            so_2_7 = so_2[so_2['hour'] == time[0]]  # 筛选11点的SO2
            so_2_8 = so_2[so_2['hour'] == time[1]]  # 筛选12点的SO2
            so_2_9 = so_2[so_2['hour'] == time[2]]  # 13

            no_2 = df[df['type'] == 'NO2']
            no_2_7 = no_2[no_2['hour'] == time[0]]
            no_2_8 = no_2[no_2['hour'] == time[1]]
            no_2_9 = no_2[no_2['hour'] == time[2]]

            o_3 = df[df['type'] == 'O3']
            o_3_7 = o_3[o_3['hour'] == time[0]]
            o_3_8 = o_3[o_3['hour'] == time[1]]
            o_3_9 = o_3[o_3['hour'] == time[2]]

            co_ = df[df['type'] == 'CO']
            co__7 = co_[co_['hour'] == time[0]]
            co__8 = co_[co_['hour'] == time[1]]
            co__9 = co_[co_['hour'] == time[2]]

            if so_2_7['万柳'].shape[0] == 0 or pd.isnull(so_2_7['万柳'].values) == 1:  # 如果数据中有空值跳过当天
                continue
            elif so_2_8['万柳'].shape[0] == 0 or pd.isnull(so_2_8['万柳'].values) == 1:
                continue
            elif so_2_9['万柳'].shape[0] == 0 or pd.isnull(so_2_9['万柳'].values) == 1:
                continue
            elif no_2_7['万柳'].shape[0] == 0 or pd.isnull(no_2_7['万柳'].values) == 1:
                continue
            elif no_2_8['万柳'].shape[0] == 0 or pd.isnull(no_2_8['万柳'].values) == 1:
                continue
            elif no_2_9['万柳'].shape[0] == 0 or pd.isnull(no_2_9['万柳'].values) == 1:
                continue
            elif o_3_7['万柳'].shape[0] == 0 or pd.isnull(o_3_7['万柳'].values) == 1:
                continue
            elif o_3_8['万柳'].shape[0] == 0 or pd.isnull(o_3_8['万柳'].values) == 1:
                continue
            elif o_3_9['万柳'].shape[0] == 0 or pd.isnull(o_3_9['万柳'].values) == 1:
                continue

            elif co__7['万柳'].shape[0] == 0 or pd.isnull(co__7['万柳'].values) == 1:
                continue
            elif co__8['万柳'].shape[0] == 0 or pd.isnull(co__8['万柳'].values) == 1:
                continue
            elif co__9['万柳'].shape[0] == 0 or pd.isnull(co__9['万柳'].values) == 1:
                continue
            else:

                date.append(file.split('_', -1)[2].split('.', 1)[0])
                date.append(file.split('_', -1)[2].split('.', 1)[0])
                date.append(file.split('_', -1)[2].split('.', 1)[0])

                so2.append(so_2_7['万柳'].values[0])
                so2.append(so_2_8['万柳'].values[0])
                so2.append(so_2_9['万柳'].values[0])
                no2.append(no_2_7['万柳'].values[0])
                no2.append(no_2_8['万柳'].values[0])
                no2.append(no_2_9['万柳'].values[0])
                o3.append(o_3_7['万柳'].values[0])
                o3.append(o_3_8['万柳'].values[0])
                o3.append(o_3_9['万柳'].values[0])
                co.append(co__7['万柳'].values[0])
                co.append(co__8['万柳'].values[0])
                co.append(co__9['万柳'].values[0])
                index1.append(str(time[0]))
                index1.append(str(time[1]))
                index1.append(str(time[2]))

            # print(wl_pm25.values)

    print(date)
    df1 = pd.DataFrame(
        data={'date': date,
              'hour': index1,
              'SO2': so2,
              'NO2': no2,
              'O3': o3,
              'CO': co}
    )
    df1.to_csv('res-wr-11.csv', index=None)
