#!/usr/bin/python

import sys
import pickle
from time import time
sys.path.append("../tools/")

from feature_format import featureFormat, targetFeatureSplit
from tester import dump_classifier_and_data
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.naive_bayes import GaussianNB


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "poi".
features_list = ['poi', 'deferred_income', 'long_term_incentive', 'shared_receipt_with_poi',
                'loan_advances','bonus', 'total_stock_value', 'restricted_stock', 'salary',
                'total_payments', 'exercised_stock_options']
                 # You will need to use more features

### Load the dictionary containing the dataset.
with open("final_project_dataset.pkl", "r") as data_file:
    data_dict = pickle.load(data_file)

### Task 2: Remove outliers

del data_dict['TOTAL']

### Task 3: Create new feature(s)
import math
for k in data_dict:
    from_ratio = float(data_dict[k]['from_poi_to_this_person'])/float(data_dict[k]['from_messages'])
    to_ratio = float(data_dict[k]['from_this_person_to_poi'])/float(data_dict[k]['to_messages'])

    if math.isnan(from_ratio):
        # print "NaN FROM"
        data_dict[k]['from_poi_ratio'] = 0.0
    else:
        data_dict[k]['from_poi_ratio'] = from_ratio
    if math.isnan(to_ratio):
        # print "NaN TO"
        data_dict[k]['to_poi_ratio'] = 0.0
    else:
        data_dict[k]['to_poi_ratio'] = to_ratio

### Store to my_dataset for easy export below.
my_dataset = data_dict

### Extract features and labels from dataset for local testing
data = featureFormat(my_dataset, features_list, sort_keys = True)
labels, features = targetFeatureSplit(data)

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting point. Try a variety of classifiers.

cv = StratifiedShuffleSplit(labels, random_state = 42)
for train_idx, test_idx in cv:
    features_train = []
    features_test  = []
    labels_train   = []
    labels_test    = []
    for ii in train_idx:
        features_train.append( features[ii] )
        labels_train.append( labels[ii] )
    for jj in test_idx:
        features_test.append( features[jj] )
        labels_test.append( labels[jj] )

from sklearn.tree import DecisionTreeClassifier
clf = GaussianNB()
clf.fit(features_train, labels_train)



### Task 5: Tune your classifier to achieve better than .3 precision and recall
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info:
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting point. Try investigating other evaluation techniques!

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of poi_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
