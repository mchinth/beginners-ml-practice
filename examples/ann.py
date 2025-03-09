import numpy as np
import pandas as pd

# Data Preprocessing
# load the dataset
dataset= pd.read_csv('Churn_Modelling.csv')
X= dataset.iloc[:, 3:-1].values
y= dataset.iloc[:, -1].values

# Encoding categorical data and label data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
labelencoder= LabelEncoder()
X[:, 2]= labelencoder.fit_transform(X[:, 2])

ColumnTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [1])], remainder= 'passthrough')
X= ColumnTransformer.fit_transform(X)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state= 0)

# feature scaling , in ANN model we need to do feature scaling for all the features
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
X_train= sc.fit_transform(X_train)
X_test= sc.transform(X_test)

# Building the ANN
# Initializing the ANN
from tensorflow.keras.models import Sequential
ann= Sequential()

# Adding the input layer and the first hidden layer
from tensorflow.keras.layers import Dense
# Dense is used to add the hidden layer,
# it takes the number of units of Neuron/nodes, no rule on how to select this number
# and activation function as input, rectifier activation function code name is relu
ann.add(Dense(units= 6, activation= 'relu'))
# Adding the second hidden layer
ann.add(Dense(units= 6, activation= 'relu'))
# you can add more hidden layers if you want

# add output layer
# For output layer we use sigmod activation function, because we have binary output
# if we have more than 2 categories in output we use softmax activation function
# Sigmod returns the probability as the result of the output
ann.add(Dense(units= 1, activation= 'sigmoid'))

# Compiling the ANN
# Optimizer is used to find the optimal weights, we use adam optimizer
# loss is used to find the error, we use binary_crossentropy for binary output
ann.compile(optimizer= 'adam', loss= 'binary_crossentropy', metrics= ['accuracy'])

# Training the ANN on the Training set
# batch size is the number of observation after which we update the weights
# Epoch is number of iterations on the whole dataset
ann.fit(X_train, y_train, batch_size= 32, epochs= 20)

# Making the predictions and evaluating the model
# Predicting the Test set results
y_pred= ann.predict(X_test)
y_pred= (y_pred > 0.5) # if y_pred is greater than 0.5 it will return true else false
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1))
