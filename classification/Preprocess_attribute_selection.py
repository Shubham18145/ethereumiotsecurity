import csv
import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score, recall_score, \
    precision_score, roc_curve, auc
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

filename = "complete_data.csv"
#to preprocess data
#remove columns 0(index),1(id),2(ssn),76(name), columns with -9(missing data) more than 50%, 69 to 75, 52 to 54, 45 to 46
df = pd.read_csv(filename,header=None)

#print(df.head())
#df.drop(df.columns[[0,1,44,45,51,52,53,68,69,70,71,72,73,74,75]], inplace = True, axis = 1)

df.drop(df.iloc[:, 69:76], inplace = True, axis = 1)
df.drop(df.iloc[:, 52:55], inplace = True, axis = 1)
df.drop(df.iloc[:, 45:47], inplace = True, axis = 1)
df.drop(df.columns[[0,1,2,40,64]], inplace = True, axis = 1)#75th column ia 63rd column, 29th column contains 69 nan values
df.replace([-9,-9.], np.NaN,inplace=True)
df.dropna(thresh=(df.shape[0]*0.5), axis=1,inplace=True)
#print(df[40].value_counts(dropna=False))
#df.drop(df.columns[[40]], inplace = True, axis = 1)#40th columnn contains negative values
#print(df[40].value_counts(dropna=False))
#df.drop(df.iloc[:,0:48], inplace = True, axis=1)
print(df.columns)
for colindex in df.columns:
    med = df[colindex].median()
    df[colindex].fillna(med,inplace=True)


print(df.isnull().sum().sum())
print(df.shape[0],df.shape[1])

df.to_csv("cleaned_data.csv")
df2 = copy.copy(df)
#print(len(df)-df.count())0
df.drop(df[df[4] == 1].index, inplace = True)#4th column- sex:0(female),1(male)
#drop all male patient related rows
df.to_csv("cleaned_female_data.csv")

df2.drop(df2[df2[4] == 0].index, inplace = True)#4th column- sex:0(female),1(male)
#drop all female patient related rows
df2.to_csv("cleaned_male_data.csv")