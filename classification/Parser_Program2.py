import csv
import pandas as pd
filename = "complete_data.csv"
#to get count of labels 0,1,2,3,4
#Database:              0   1   2   3   4 Total
#Cleveland(modified):  404 191  132  130  42 899

df = pd.read_csv(filename,header=None)
print(df.shape[0],df.shape[1])

#label = df.iloc[:,57:58]
print(df[58].value_counts())
