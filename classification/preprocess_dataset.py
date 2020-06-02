import csv
import pandas as pd
import numpy as np
from sklearn.utils import shuffle


filename1 = "X_train_cleaned.csv"
filename2 = "y_train.csv"

filename3 = "X_test_cleaned.csv"
filename4 = "y_test.csv"

df_train_data = pd.read_csv(filename1)
df_train_labels = pd.read_csv(filename2)
df_test_data = pd.read_csv(filename3)
df_test_labels = pd.read_csv(filename4)

df_train_total = pd.concat([df_train_data,df_train_labels],axis=1)
df_test_total = pd.concat([df_test_data,df_test_labels],axis=1)

np_train = np.array(df_train_total)
np_test = np.array(df_test_total)

np_train = shuffle(np_train)
np_test = shuffle(np_test)

np_full = np.concatenate((np_train,np_test))

np_full.shape

new_data_train_dict = [5,5,5,5,5,5,5]
new_data_train = []
for i in np_full:
    if(new_data_train_dict[int(i[-1])] > 0):
        new_data_train.append(i)
        new_data_train_dict[int(i[-1])] -= 1
    continue

new_data_train = np.array(new_data_train)

new_data_train.shape

list_data = new_data_train.tolist()

new_format_data = []
for i in list_data:
    data = map(str,i[:20])
    data = ",".join(data)
    data = '"' + data + ','
    data += str(i[-1]) +'"\n'
    new_format_data.append(data)

f = open("preprocessed_data_to_blockchain.txt","w")

for i in new_format_data:
    f.write(i)

f.close()

