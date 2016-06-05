poi_names = open("/Users/mbai/Downloads/ud120-projects-master/final_project/poi_names.txt", "r")

count = 0
for line in poi_names:
    if ',' in line:
        count += 1
print count