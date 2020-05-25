import csv
import pandas as pd
import numpy as np
import copy
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score, recall_score, \
    precision_score, roc_curve, auc, matthews_corrcoef
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_selection import RFE, SelectKBest, chi2
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn import svm
from sklearn.feature_selection import RFE, SelectKBest, chi2

filename = "processed.cleveland.csv"
# to preprocess data
# remove columns 0(index),1(id),2(ssn),76(name), columns with -9(missing data) more than 50%, 69 to 75, 52 to 54, 45 to 46, 40
dataset = pd.read_csv(filename, index_col=0)
# dataset.pop(0)
dataset.replace(["?"], np.NaN,inplace=True)
dataset.dropna(thresh=(dataset.shape[0]*0.5), axis=1,inplace=True)
print(dataset.columns)

for colindex in dataset.columns:
    med = dataset[colindex].median()
    dataset[colindex].fillna(med,inplace=True)


# print(dataset.isnull().sum().sum())
# print(dataset.shape[0],dataset.shape[1])
# print(dataset.columns)
# print(dataset.shape)
#Y = dataset.values[:,:-1]
Y = dataset.iloc[:,-1]

X = dataset.values[:, 0:12]
listx = list(X)
# chi2f = SelectKBest(chi2, k=12)
# X = chi2f.fit_transform(X, Y)

sc_x = StandardScaler()
X = sc_x.fit_transform(X)

def printmulti(clf, X, Y, name, figname):
    print('\nMulticlass class classification ' + name)
    train_score = cross_val_score(estimator=clf, X=X, y=Y, cv=5)
    Y_predicted = cross_val_predict(estimator=clf, X=X, y=Y, cv=5)
    conf_matrix = confusion_matrix(Y, Y_predicted)
    print("Accuaracy", train_score.mean())
    print('F1 score:', f1_score(Y, Y_predicted, average='macro',labels=np.unique(Y_predicted)))
    print('Sensitivity:', recall_score(Y, Y_predicted, average='macro'))
    print('Precision:', precision_score(Y, Y_predicted, average='macro',labels=np.unique(Y_predicted)))
    print("Matthews Correlation Coefficient: ", matthews_corrcoef(Y, Y_predicted))
    print('Classification report: \n', classification_report(Y, Y_predicted))
    # print("Confusion matrix: \n", confusion_matrix(Y, Y_predicted))
    Y_new_test = copy.copy(Y)
    Y_new_predicted = copy.copy(Y_predicted)
    Y_new_test[Y_new_test > 0] = 1
    Y_new_predicted[Y_new_predicted > 0] = 1
    fpr, tpr, threshold = roc_curve(Y_new_test, Y_new_predicted)
    roc_auc = auc(fpr, tpr)
    printbinary(Y_new_test, Y_new_predicted, name)
    plt.title('Receiver Operating Characteristic( ' + name + ' ) for All Patients')
    plt.plot(fpr, tpr, 'b', label='AUC = %0.2f' % roc_auc)
    plt.legend(loc='lower right')
    plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    figname = figname + 'pic.png'
    plt.show()
    plt.savefig(figname, dpi='figure')


def printbinary(Y_new_test, Y_new_predicted, name):
    print('\nBinary class classification(1,2,3,4 classified as 1) for ' + name)
    print('Accuracy:', accuracy_score(Y_new_test, Y_new_predicted))
    print('F1 score:', f1_score(Y_new_test, Y_new_predicted,labels=np.unique(Y_new_predicted)))
    print('Sensitivity:', recall_score(Y_new_test, Y_new_predicted))
    print('Precision:', precision_score(Y_new_test, Y_new_predicted,labels=np.unique(Y_new_predicted)))
    print("Matthews Correlation Coefficient: ", matthews_corrcoef(Y_new_test, Y_new_predicted))
    print('Classification report: \n', classification_report(Y_new_test, Y_new_predicted))
    # print("Confusion matrix: \n", confusion_matrix(Y_new_test, Y_new_predicted))


# Models
clf = DecisionTreeClassifier(max_depth=3)
printmulti(clf, X, Y, "Decision Tree Classifier[depth=7]", "decisiontree")

gb_clf = GradientBoostingClassifier(n_estimators=20, learning_rate=0.75, max_features=2, max_depth=2, random_state=0)
printmulti(gb_clf, X, Y, "Gradient Boosting", "gradientboosting")

lrclf = LogisticRegression(solver='lbfgs', multi_class='auto', random_state=0)
printmulti(clf, X, Y, "Logistic Regression Classifier", "logisticregression")

nbclf = GaussianNB()
printmulti(clf, X, Y, "Gaussian Classifier", "gaussianclassifier")

rfclf = RandomForestClassifier(n_estimators=80)
printmulti(clf, X, Y, "Random Forest Classifier", "randomforest")

svmclf = svm.SVC(kernel='linear')  # Linear Kernel
printmulti(clf, X, Y, "Support Vector Machine Classifier", "svm")