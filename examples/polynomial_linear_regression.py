import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Position_Salaries.csv')
X = data.iloc[:, 1:-1].values
y = data.iloc[:, -1].values
print(X)
print(y)

# split the data into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Train the model, use linear regression
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

Y_pred = lin_reg.predict(X_test)

#print y_test and Y_pred in vertical order
print(np.concatenate((y_test.reshape(len(y_test),1), Y_pred.reshape(len(Y_pred),1)),1))

#Now tain the model using polynomial regression
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
# need to update the  feature set to include the polynomial terms
X_poly = poly_reg.fit_transform(X)
lin_reg2 = LinearRegression()
lin_reg2.fit(X_poly, y)

Y_pred2 = lin_reg2.predict(poly_reg.fit_transform(X_test))
print(np.concatenate((y_test.reshape(len(y_test),1), Y_pred2.reshape(len(Y_pred2),1)),1))

# Visualize the linear regression results v/s polynomial regression results
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.scatter(X, y, color='red')
plt.plot(X, lin_reg.predict(X), color='blue')
# should pass X_poly instead of X
plt.plot(X, lin_reg2.predict(X_poly), color='green')
plt.savefig("plot.png")  # Saves as an image file

# predicting the salary for a specific level
level = 6.5
print(lin_reg.predict([[level]]))
print(lin_reg2.predict(poly_reg.fit_transform([[level]])))