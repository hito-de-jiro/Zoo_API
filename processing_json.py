import csv
import json

with open('json_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

result_data = data['results'][0]
# name
name = data['results'][0]['name']
# rating recommendations
count_reviews = data['results'][0]['count_reviews']
avg_review_score = data['results'][0]['avg_review_score']
recommendations = f"{count_reviews} recommendations"
review_score = f"{avg_review_score} stars in Google"
# description
description = data['results'][0]['subtitle']
# address
address = data['results'][0]['address']
zip_code = data['results'][0]['zip']
city = data['results'][0]['city']
full_address = f'{address}, {city}, {zip_code}'
# open time
open_time = data['results'][0]['open_time']
open_days = {'mo': [], 'di': [], 'mi': [], 'do': [], 'fr': [], 'sa': [], 'so': []}
working_hours = []  # -- working hours in week
for days in open_time:
    for k, v in days.items():
        if days['day'] == 1 and len(str(v)) > 1:
            open_days['mo'].append(v)
        elif days['day'] == 2 and len(str(v)) > 1:
            open_days['di'].append(v)
        elif days['day'] == 3 and len(str(v)) > 1:
            open_days['mi'].append(v)
        elif days['day'] == 4 and len(str(v)) > 1:
            open_days['do'].append(v)
        elif days['day'] == 5 and len(str(v)) > 1:
            open_days['fr'].append(v)
        elif days['day'] == 6 and len(str(v)) > 1:
            open_days['sa'].append(v)
        elif days['day'] == 7 and len(str(v)) > 1:
            open_days['so'].append(v)

for k, v in open_days.items():
    if len(v) == 4:
        first = f"{k}: {str(v[0]).replace('00', ':00')}-{str(v[1]).replace('00', ':00')}"
        second = f"/{str(v[2]).replace('00', ':00')}-{str(v[3]).replace('00', ':00')}"
        working_hours.append(first + second)

    elif len(v) == 2:
        first = f"{k}: {str(v[0]).replace('00', ':00')}-{str(v[1]).replace('00', ':00')}"
        working_hours.append(first)
# create format string for data opening
hours = ''.join(working_hours)

# Create dictionary for all data
all_data_dict = {'name': name, 'rating': review_score, 'recommendations': recommendations,
                 'description': description, 'address': full_address, 'working_hours': hours}

print(all_data_dict)


# Write getting data to CSV-file
def csv_write(data_dict):
    data_csv = open('csv_data.csv', 'w', newline='', encoding='utf-8')
    # create headers in CSV-document
    csv_dict_writer = csv.DictWriter(data_csv,
                                     ['name', 'rating', 'recommendations', 'description', 'address', 'working_hours'])
    csv_dict_writer.writeheader()
    # write to CSV
    csv_dict_writer.writerow(data_dict)
    data_csv.close()


csv_write(all_data_dict)
