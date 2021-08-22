import numpy as np
from tensorflow import keras

# units - neiron, input_shape- input qanak
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
# optomizacia u korust
model.compile(optimizer='sgd', loss='mean_squared_error')

inarray = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
outarray = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)
# input = 2*output - 1

model.fit(inarray, outarray, epochs=500)
out = model.predict([10.0])
# 18.98
print(np.round(out))
# 19.


