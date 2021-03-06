import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score, recall_score, precision_score, roc_curve, auc, matthews_corrcoef
from sklearn.model_selection import train_test_split

file_read = open("data_retrieved_from_blockchain.txt","r")
input_data = file_read.readlines()
input_data[0]


for i in range(len(input_data))
    input_data[i] = (input_data[i].split(":")[1].split('"')[1]).split(',')

input_data = np.array(input_data)

total_labels = input_data[:,-1].astype(np.float).astype(np.int)
total_data  = input_data[:,:-1].astype(np.float)

for i in range(len(total_labels)):
    if(total_labels[i] <= 3):
        total_labels[i] = 1

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(total_data, total_labels, test_size=0.33, random_state=100)


nbclf = GaussianNB()
rfclf = RandomForestClassifier(n_estimators=100)
svmclf = svm.SVC(kernel='linear') #Linear Kernel


def classify_and_report(classifier,X_train, X_test, y_train, y_test):
    classifier.fit(X_train,y_train)
    y_predicted = classifier.predict(X_test)
    print("Multiclass classification: ")
    print('Accuracy:', accuracy_score(y_test, y_predicted))
    print('Recall:', recall_score(y_test, y_predicted,average='macro'))
    print("Matthews Correlation Coefficient: ",matthews_corrcoef(y_test, y_predicted))
    print('Classification report:', classification_report(y_test, y_predicted))


print ("Naive Bayes")
classify_and_report(nbclf,X_train, X_test, y_train, y_test)


print ("Random Forest")
classify_and_report(rfclf,X_train, X_test, y_train, y_test)


print ("SVM")
classify_and_report(svmclf,X_train, X_test, y_train, y_test)

