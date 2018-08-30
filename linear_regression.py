#coding:utf-8
import tensorflow as tf 
import numpy as np 

# 生成数据
data_x = np.linspace(-1, 1, 200)
data_y = data_x * 3 + np.random.randn(*data_x.shape) * 0.33

train_x, train_y = data_x[:170], data_y[:170]
test_x, test_y = data_x[170:], data_y[170:]

# 显示生成的数据 
import matplotlib.pyplot as plt 
plt.scatter(train_x, train_y)
plt.xlabel("Close View, Training Beigin")
plt.show()


# 构建模型
from tensorflow import keras
model = keras.Sequential()
model.add(keras.layers.Dense(units=1, activation='linear', kernel_initializer='uniform', input_dim=1))
print('------------初始化数据-------------')
weights = model.layers[0].get_weights()
print('Trained Weight = %.2f' % weights[0][0][0])
print('Trained Bias = %.2f' % weights[1][0])

# 损失函数方差， 优化函数随机梯度下降
model.compile(loss='mse', optimizer='sgd')

# 训练模型，因为是随机梯度，所以500次训练
model.fit(train_x, train_y, epochs=500)
print('------------训练数据-------------')
weights = model.layers[0].get_weights()
print('Trained Weight = %.2f' % weights[0][0][0])
print('Trained Bias = %.2f' % weights[1][0])

# 预测与对照
prediction_y = model.predict(test_x)
plt.scatter(test_x, test_y)
plt.plot(test_x,prediction_y)
plt.xlabel("Weight = {:2.0f}, Bias = {:2.0f}".format(weights[0][0][0], weights[1][0]))
plt.show()
