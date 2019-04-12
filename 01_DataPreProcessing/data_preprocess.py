'''
This code is the simple template for preprocessing the data

Input : dataset
Output : pre-processed dataset

'''

#importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing the dataset using pandas library
dataset = pd.read_csv("./Data.csv")

# Defrentiating between dependent variables and independent variable (target Variable)
# Matrix of Dependent variables
X = dataset.iloc[:,0:3]
y = dataset.iloc[:,3:4]


