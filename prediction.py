import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pm2.5_data = pd.read_excel('789.xlsx')
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error #均方误差
from sklearn.metrics import mean_absolute_error #平方绝对误差
from sklearn.metrics import r2_score#R square
from sklearn.metrics import explained_variance_score  #解释方差
X = pm2.5_data.iloc[:,:-1]          #提前特征和标签
Y = pm2.5_data.iloc[:,-1]
scaler = preprocessing.StandardScaler().fit(X)          #数据标准化
x_transformed = scaler.transform(X)
d1 = list(range(2000))          #对数据分组
d2 = list(range(2001,3214))
train_list = []      #放入训练和测试的数据
test_list = []
train_list.extend(d1)  #更改训练集样本
test_list.extend(d2)   #更改测试集样本
import time
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
print('开始运行时间')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
rfr = RandomForestRegressor(max_depth = 4,n_estimators=64) #max_depth = 2,n_estimators=10
rfr.fit(pm2.5_data.iloc[train_list,:-1],pm2.5_data.iloc[train_list,-1])
rfr_pre = rfr.predict(pm2.5_data.iloc[test_list,:-1])
mae_rfr = mean_absolute_error(pm2.5_data.iloc[test_list,-1],rfr_pre)
r2_rfr = r2_score(pm2.5_data.iloc[test_list,-1],rfr_pre)
mse_rfr = mean_squared_error(pm2.5_data.iloc[test_list,-1],rfr_pre)
# rmse_svr = np.sqrt(mean_squared_error(y_test,svr_pre))
# evs_svr = explained_variance_score(y_test, svr_pre)
print("测试数据预测值")
print(rfr_pre)
print('真实值')
print('')
print('结束运行时间')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('')
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
print('开始运行时间')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
knn = KNeighborsRegressor(n_neighbors =32)
knn.fit(pm2.5_data.iloc[train_list,:-1],pm2.5_data.iloc[train_list,-1])
knn_pre = knn.predict(pm2.5_data.iloc[test_list,:-1])
mae_knn = mean_absolute_error(pm2.5_data.iloc[test_list,-1],knn_pre)
r2_knn = r2_score(pm2.5_data.iloc[test_list,-1],knn_pre)
mse_knn = mean_squared_error(pm2.5_data.iloc[test_list,-1],knn_pre)
# rmse_svr = np.sqrt(mean_squared_error(y_test,svr_pre))
# evs_svr = explained_variance_score(y_test, svr_pre)
print("测试数据预测值")
print(knn_pre)
print('真实值')
print('')
print('结束运行时间')
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print('')
df = {'rfr_pre':rfr_pre,'knn_pre':knn_pre,'true':pm2.5_data.iloc[test_list,-1],'knn_mae':mae_knn,"knn_mse":mse_knn,"knn_r2":r2_knn
     , r2":r2_svr,"rfr_mae":mae_rfr,"rfr_mse":mse_rfr,"rfr_r2":r2_rfr}
df = pd.DataFrame(df)
df.to_excel('结果.xlsx')