from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


train = pd.read_csv("台灣電力公司_過去電力供需資訊.csv")
target = train["備轉容量(MW)"]
X1 = train.iloc[:,1:3]
X2 = train.iloc[:,4:7]
X = pd.concat( [X1, X2], axis=1 )
predict_list = []

X = np.array(X)
target = np.array(target)
last = X[396,:]

# 3/23
new_x = X[0:345,:]
new_y = target[51:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/24
new_x = X[0:344,:]
new_y = target[52:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/25
new_x = X[0:343,:]
new_y = target[53:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/26
new_x = X[0:342,:]
new_y = target[54:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/27
new_x = X[0:341,:]
new_y = target[55:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/28
new_x = X[0:340,:]
new_y = target[56:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

# 3/29
new_x = X[0:339,:]
new_y = target[57:396]
model = LinearRegression()
model.fit(new_x,new_y)
predict = model.predict(last.reshape(1,5))
predict_list.append(predict)

date = ["20210323","20210324","20210325","20210326","20210327","20210328","20210329"]
date = np.array(date)
df = pd.DataFrame(date,columns = ["date"])
df.insert(1,"MW",predict_list)

df.to_csv("submission.csv")    
