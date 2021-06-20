import csv

import json



# Opening JSON file

json_obj = open('Files/state_to_region.json', 'r')



# returns JSON object as a dictionary

json_data = json.load(json_obj)



temp_lst = []



# open file in read mode 'r'

with open('Files/people.csv', 'r') as read_obj:

    # pass the file object to reader() to get the reader object

    csv_reader = csv.reader(read_obj)

    next(csv_reader) #skips headers

    # Iterates over each row in the csv using reader object

    for each_csv_row in csv_reader:

        # check state value in json file on step 47

        temp_row = {'Name': each_csv_row[0],

                    'Title': each_csv_row[1],

                    'City': each_csv_row[2],

                    'State': each_csv_row[3],

                    'Region': json_data.get(each_csv_row[3])} #checks if json file has csv state region value

        temp_lst.append(temp_row)



print(temp_lst)

#updates values
new_csv_cols = temp_lst[0].keys()

print(new_csv_cols)

# updating original csv file in write mode 'w'

with open('Files/people.csv', 'w', newline='') as f:

    w = csv.DictWriter(f, new_csv_cols)

    w.writeheader() #write keys

    w.writerows(temp_lst)


