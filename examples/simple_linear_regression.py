import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
print("Importing the dataset")
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

#split the dataset into training and test set
print("Splitting the dataset into the Training set and Test set")
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

print("Training the simple linear regression model on the training set")
#train the simple linear regression model on the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print("Predicting the test set results")
#predict the test set results
y_pred = regressor.predict(X_test)

# print("Plotting the training set results")
# #visualize the training set results
# plt.scatter(X_train, y_train, color='red')
# plt.plot(X_train, regressor.predict(X_train), color='blue')
# plt.title('Salary vs Experience (Training Set)')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

# print("Plotting the test set results")
# #visualize the test set results
# plt.scatter(X_test, y_test, color='red')
# plt.plot(X_train, regressor.predict(X_train), color='blue')
# plt.title('Salary vs Experience (Test Set)')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

print("Comparing the predicted and actual values")
#set pecision to 2 decimal places
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))