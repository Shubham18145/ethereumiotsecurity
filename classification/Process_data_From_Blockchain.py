#!/usr/bin/env python
# coding: utf-8

# In[130]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score, recall_score,     precision_score, roc_curve, auc, matthews_corrcoef
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# In[97]:


file_read = open("new_processed_from_blockchain.txt","r")
input_data = file_read.readlines()
input_data[0]


# In[98]:


for i in range(len(input_data)):
    input_data[i] = (input_data[i].split(":")[1].split('"')[1]).split(',')


# In[99]:


input_data = np.array(input_data)


# In[100]:


# input_data[0].split('"')


# In[191]:


total_labels = input_data[:,-1].astype(np.float).astype(np.int)
total_data  = input_data[:,:-1].astype(np.float)


# In[192]:


total_labels


# In[193]:


# total_labels = total_labels.tolist()
for i in range(len(total_labels)):
    if(total_labels[i] <= 3):
        total_labels[i] = 1
# total_labels = np.array(total_labels)


# In[194]:


total_labels


# In[195]:


total_data


# In[208]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(total_data, total_labels, test_size=0.33, random_state=100)


# In[209]:


nbclf = GaussianNB()
rfclf = RandomForestClassifier(n_estimators=100)
svmclf = svm.SVC(kernel='linear') #Linear Kernel


# In[210]:


def classify_and_report(classifier,X_train, X_test, y_train, y_test):
    classifier.fit(X_train,y_train)
    y_predicted = classifier.predict(X_test)
    #print(confusion_matrix(Y_test, Y_predicted))
#     print("Naive Bayes Classifier: \n")
    print("Multiclass classification: ")
    print('Accuracy:', accuracy_score(y_test, y_predicted))
    #print('F1 score:', f1_score(Y_test, Y_predicted,average='macro'))
    #print('F1 score:', f1_score(Y_test, Y_predicted,average='weighted'))
    print('F1 score:', f1_score(y_test, y_predicted,average='macro'))
    print('Recall:', recall_score(y_test, y_predicted,average='macro'))
    print('Precision:', precision_score(y_test, y_predicted,average='macro'))
    print("Matthews Correlation Coefficient: ",matthews_corrcoef(y_test, y_predicted))
    print('Classification report:', classification_report(y_test, y_predicted))


# In[211]:


print ("Naive Bayes")
classify_and_report(nbclf,X_train, X_test, y_train, y_test)


# In[212]:


print ("Random Forest")
classify_and_report(rfclf,X_train, X_test, y_train, y_test)


# In[213]:


print ("SVM")
classify_and_report(svmclf,X_train, X_test, y_train, y_test)


# In[ ]:





# In[ ]:




