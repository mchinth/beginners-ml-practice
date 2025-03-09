import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the data
data = pd.read_csv('50_Startups.csv')
X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

# Encoding categorical data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ColumnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ColumnTransformer.fit_transform(X))

# Avoiding the dummy variable trap X = X[:, 1:]
# this is taken care of by the library, no need to explicitly do it in python

# Split the dataset into training and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train the multiple linear regression model on the training set
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# in python libay does all the work, no need to calculate the coefficients and intercept manually
# print(regressor.coef_)
# print(regressor.intercept_)

#predict the test set results
y_pred = regressor.predict(X_test)

#print the predicted and actual values in vertical format
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test),1)), 1))
