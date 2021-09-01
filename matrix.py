import numpy as np
from tensorflow import keras


model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')
x = np.array([[1,1,1,1,1,1,1,1,1,0,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
              [1,1,1,1,1,1,1,1,1,1,1,1,1,1]])
y = np.array([3, 1])

model.fit(x, y, epochs=500)
out = model.predict([[1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                     [1,1,1,1,1,1,1,1,1,1,1,1,0,1]])

print(np.round(out))
