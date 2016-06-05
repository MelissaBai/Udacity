#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 


from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(
features, labels, test_size=0.3, random_state=42)

  
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

clf = DecisionTreeClassifier()
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print precision_score(labels_test, pred)
print recall_score(labels_test, pred)


#print clf.score(features_test, labels_test)
'''
cpp = [1 for j in zip(labels_test, pred) if j[0] == j[1] and j[1] == 1]

cpp = []
for i in range(len(labels_test)):
    if labels_test[i] == pred[i] == 1:
        cpp.append(1)

cpp = []
for l, p in zip(labels_test, pred):
    if l == p == 1:
        cpp.append(1)
        
print cpp
'''