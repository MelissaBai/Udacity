#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import pprint
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#data_dict.pop('TOTAL')
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


for k in data_dict:
    if k == 'TOTAL':
        print k, data_dict[k]
### your code below



for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
