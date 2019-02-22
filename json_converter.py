import json

import csv

with open ('reuslts.json', 'r') as f:
    sessions_dict = json.load(f)

ses_data = sessions_dict[0]['sessions']

print(ses_data)

# open a file for writing

session_data = open('NSLV19-SessionList-Now.csv', 'w')

#create the csv writer object

csvwriter = csv.writer(session_data)

count = 0

for session in ses_data:

    if count == 0:

        header = session.keys()

        csvwriter.writerow(header)

        count += 1

    csvwriter.writerow(session.values())

session_data.close()


