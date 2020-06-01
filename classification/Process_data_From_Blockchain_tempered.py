#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# In[ ]:


file_read = open("data_retrieved_from_blockchain.txt","r")
input_data = file_read.readlines()


# In[ ]:


for i in range(len(input_data)):
    input_data[i] = (input_data[i].split(":")[1].split('"')[1]).split(',')


# In[ ]:


input_data = np.array(input_data)


# In[ ]:


total_labels = input_data[:,-1].astype(np.float).astype(np.int)
total_data  = input_data[:,:-1].astype(np.float)


# In[ ]:


for i in range(len(total_labels)):
    if(total_labels[i] <= 3):
        total_labels[i] = 1


# In[ ]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(total_data, total_labels, test_size=0.33, random_state=40)


# In[ ]:


for i in range(len(y_train)):
    if(y_train[i] == 1):
        y_train[i] = 4
    elif(y_train[i] == 4):
        y_train[i] = 1


# In[ ]:


nbclf = GaussianNB()
rfclf = RandomForestClassifier(n_estimators=100)
svmclf = svm.SVC(kernel='linear')


# In[ ]:


def classify_and_report(classifier,X_train, X_test, y_train, y_test):
    classifier.fit(X_train,y_train)
    y_predicted = classifier.predict(X_test)
    print("Multiclass classification: ")
    print('Accuracy:', accuracy_score(y_test, y_predicted))
    print('F1 score:', f1_score(y_test, y_predicted,average='macro'))
    print('Recall:', recall_score(y_test, y_predicted,average='macro'))
    print('Precision:', precision_score(y_test, y_predicted,average='macro'))
    print("Matthews Correlation Coefficient: ",matthews_corrcoef(y_test, y_predicted))
    print('Classification report:', classification_report(y_test, y_predicted))


# In[ ]:


print ("Naive Bayes")
classify_and_report(nbclf,X_train, X_test, y_train, y_test)


# In[ ]:


print ("Random Forest")
classify_and_report(rfclf,X_train, X_test, y_train, y_test)


# In[ ]:


print ("SVM")
classify_and_report(svmclf,X_train, X_test, y_train, y_test)


# In[ ]:




