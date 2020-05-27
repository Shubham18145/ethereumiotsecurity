import csv
import pandas as pd
filename1 = "X_train.txt"
filename2 = "y_train.txt"

#to get count of labels 0,1,2,3,4
#Database:              0   1   2   3   4 Total
#Cleveland(modified):  404 191  132  130  42 899

df_data = pd.read_csv(filename1,sep=" ",header=None)
df_labels = pd.read_csv(filename2,header=None)
print(df.shape[0],df.shape[1])

#label = df.iloc[:,57:58]
#print(df[58].value_counts())
df_total = pd.concat([df_data,df_labels],axis=1)
print(df_total)
