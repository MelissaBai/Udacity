#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
def svmAccuracy(features_train, labels_train, features_test, labels_test):
    from sklearn import svm
    clf = svm.SVC(C=10000, kernel='rbf', gamma='auto')
    #features_train = features_train[:len(features_train)/100]
    #labels_train = labels_train[:len(labels_train)/100]
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"
    #t0 = time()
    pred = clf.predict(features_test)
    print pred.sum()
    #print "training time:", round(time()-t0, 3), "s"
    from sklearn.metrics import accuracy_score
    accuracy = clf.score(features_test, labels_test)
    print accuracy
    return accuracy
    
svmAccuracy(features_train, labels_train, features_test, labels_test)
#########################################################


