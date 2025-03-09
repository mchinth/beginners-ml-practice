# Data Preprocessing Tools

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset Note, data should be , separated
# X is the matrix of features, y is the dependent variable vector
print("Importing the dataset")
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
print(X)
print(y)

print("Taking care of missing data")
# Taking care of missing data
from sklearn.impute import SimpleImputer
# Create an object of the SimpleImputer class, missing_values is the value of the missing data, strategy is the method to replace the missing data
# mean, median, most_frequent, constant
SimpleImputer = SimpleImputer(missing_values=np.nan,strategy='mean')
# Fit the SimpleImputer object to the matrix of features X
# X[:, 1:3] means that we want to replace the missing data in the columns 1 and 2
SimpleImputer.fit(X[:, 1:3])
# Transform the matrix of features X by replacing the missing data
X[:, 1:3] = SimpleImputer.transform(X[:, 1:3])
# print(X)

# Fit and transform in one line
# X[:,1:3] = SimpleImputer.fit_transform(X[:, 1:3])
print(X)

print("Encoding categorical data")
# Encoding categorical data
# If we have data like place names, country names, etc shift them into columns and assign 1 or 0 based on the presence of the data
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

ColumnTransformer = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X = np.array(ColumnTransformer.fit_transform(X))
print(X)

print("Encoding the dependent variable")
# Encoding the dependent variable
# If the dependent variable is categorical, we need to encode it yes or no to 1 or 0
from sklearn.preprocessing import LabelEncoder
LabelEncoder_y = LabelEncoder()
y = LabelEncoder_y.fit_transform(y)
print (y)

print("Splitting the dataset into the Training set and Test set")
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
# test_size is the proportion of the dataset to include in the test split
# random_state is the seed for the random number generator
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

print(X_train)
print(X_test)
print(y_train)
print(y_test)

print("Feature Scaling")
# Feature Scaling
# We don't want influence of tarin set on test set, so feature scaling happens after testsplit
# Standardization and Normalization
# Standardization: X_stand = (X - mean(X))/std(X)
# Normalization: X_norm = (X - min(X))/(max(X) - min(X))
from sklearn.preprocessing import StandardScaler
StandardScaler_X = StandardScaler()

# Fit and transform the training set
# skipping dependent variable as it is already encoded
X_train[:, 3:] = StandardScaler_X.fit_transform(X_train[:, 3:])
print(X_train)

# Transform the test set, X_stand already calculated from training set and saved in StandardScaler_X object
X_test[:, 3:] = StandardScaler_X.transform(X_test[:, 3:])
print(X_test)

# Feature scaling is not required for y as it is already encoded


