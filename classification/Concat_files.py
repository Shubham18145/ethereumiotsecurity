import csv
import pandas as pd
import numpy as np
# filename1 = "X_test.txt"
# filename2 = "X_train.txt"

# df_data_test = pd.read_csv(filename1,header=None, error_bad_lines=False)
# df_data_train = pd.read_csv(filename1,header=None, error_bad_lines=False)
# df_data.to_csv("X_test_2.csv",index=False)
# print (df_data.head(1).shape)

filename3 = "X_train_cleaned.csv"
filename4 = "y_train.csv"
filename5 = "X_test_cleaned.csv"
filename6 = "y_test.csv"

df_train_data = pd.read_csv(filename3)
df_train_labels = pd.read_csv(filename4)
df_test_data = pd.read_csv(filename5)
df_test_labels = pd.read_csv(filename6)

df_train_total = pd.concat([df_data,df_labels],axis=1)
df_test_total = pd.concat([df_data,df_labels],axis=1)

# np.array(df_train_data)
