#import the modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import the data
data=pd.read_csv('data/student.csv')
print(data.head())
print(data.isnull().sum()) #check if there is any null value or not
