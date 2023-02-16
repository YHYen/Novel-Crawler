import numpy as np
from scipy import stats
import tensorflow
import pandas
import matplotlib.pyplot as plt
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Bidirectional
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from numpy.random import seed
seed(1)
tensorflow.random.set_seed(1)


n_timestamp = 12
n_epochs = 2000

# choose model
model_type = 1

# Load Training Data
dataFrame = pandas.read_csv(r'C:\Users\User\PycharmProjects\ProjectS\DataToLSTMTest.csv',
                            usecols=['Predicate', 'StartOfDialogueAgent', 'EndOfDialogueAgent', 'StartOfDialogue',
                                     'EndOfDialogue'], encoding='unicode_escape')
training_set = dataFrame.iloc[0:772-200, 2:3].values
testing_set = dataFrame.iloc[772-200:, 2:3].values

# dataset normalization
scaler = MinMaxScaler(feature_range=(0, 1))
training_set_scaled = scaler.fit_transform(training_set)
testing_set_scaled = scaler.transform(testing_set)

# timestamp function
def data_split(sequence, n_timestamp):
    X = []
    Y = []
    for i in range(len(sequence)):
        end_ix = i + n_timestamp
        if end_ix > len(sequence)-1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        Y.append(seq_y)
    return np.array(X), np.array(Y)

X_train, Y_train = data_split(training_set_scaled, n_timestamp)
X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

X_test, Y_test = data_split(testing_set_scaled, n_timestamp)
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)

# constructor LSTM
if model_type == 1:
    model = Sequential()
    model.add(LSTM(units=50, activation='relu', input_shape=(X_train.shape[1], 1)))
    model.add(Dense(units=1))
if model_type == 2:
    model = Sequential()
    model.add(LSTM(units=50, activation='relu', return_sequences=True, input_shape=(X_train.shape[1], 1)))
    model.add(LSTM(units=50, activation='relu'))
    model.add(Dense(1))
if model_type == 3:
    model = Sequential()
    model.add(Bidirectional(LSTM(units=50, activation='relu'), input_shape=(X_train.shape[1], 1)))
    model.add(Dense(1))
model.summary()

model.compile(optimizer=tensorflow.keras.optimizers.Adam(0.001), loss='mean_squared_error')

history = model.fit(X_train, Y_train,
                    batch_size=64,
                    epochs=n_epochs,
                    validation_data=(X_test, Y_test),
                    validation_freq=1)
model.summary()

plt.plot(history.history['loss'], label = 'Training Loss')
plt.plot(history.history['val_loss'], label = 'Validation Loss')
plt.title('Training and Validation Loss')
plt.legend()
plt.show()

predicted_Agent = model.predict(X_test)
predicted_Agent = scaler.inverse_transform(predicted_Agent)
real_Agent = scaler.inverse_transform(Y_test)

plt.plot(real_Agent, color='red', label='Real_Agent')
plt.plot(predicted_Agent, color='blue', label='Predicted_Agent')
plt.title('Agent Prediction')
plt.xlabel('Time')
plt.ylabel('Agent')
plt.legend()
plt.show()

MSE   = metrics.mean_squared_error(predicted_Agent, real_Agent)
RMSE  = metrics.mean_squared_error(predicted_Agent, real_Agent)**0.5
MAE   = metrics.mean_absolute_error(predicted_Agent, real_Agent)
R2    = metrics.r2_score(predicted_Agent, real_Agent)

print('均方誤差: %.5f' % MSE)
print('均方根誤差: %.5f' % RMSE)
print('平均絕對誤差: %.5f' % MAE)
print('R2: %.5f' % R2)