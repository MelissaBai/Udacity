#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
print "Number of people %d" %len(enron_data.keys())

'''
# Counts in enron dataset
for item in enron_data:
    if item.startswith("SKIL"):
        print item
        break
# Counts of features in each item of enron_dataset
print "features available: %d" %len(enron_data[item].keys())

# Counts poi
poi_count = 0
for item in enron_data:
    if enron_data[item]["poi"] == 1:
        poi_count += 1
print poi_count  


#for item in enron_data:
#    for feature in enron_data[item]:
#        print feature
print enron_data['PRENTICE JAMES']['total_stock_value']   
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']    
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']


for item in enron_data:
    if item.startswith("SKILL") or item.startswith("LAY") or item.startswith("FASTOW"):
        print item
        
LAY = enron_data["LAY KENNETH L"]['total_payments']
FAS = enron_data['FASTOW ANDREW S']['total_payments']
SKIL = enron_data['SKILLING JEFFREY K']['total_payments']

print LAY, FAS, SKIL
print max(LAY, FAS, SKIL)

for item in enron_data:
    for feature in enron_data[item]:
        print feature, enron_data[item][feature]
    break

count_poi = 0
count_nan = 0
for item in enron_data:
    if enron_data[item]['poi'] == 1:
        count_poi += 1
        if enron_data[item]['total_payments'] == 'NaN':
            count_nan += 1
print count_poi, count_nan, count_nan/count_poi
'''

result = []
for item in enron_data:
    for feature in enron_data[item]: 
        if feature == 'exercised_stock_options' and enron_data[item]['exercised_stock_options'] != 'NaN':
            result.append(enron_data[item]['exercised_stock_options'])
print sorted(result)

    