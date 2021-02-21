import csv

# Create frequency dictionary
datasetNumber = 2
believabilityColStr = "True"  # Change what value of row you're looking for (In this case True or False)
filePrefix = believabilityColStr.upper()

myDict = {}
with open(f'./data/dataset_{datasetNumber}_with_urls.csv') as csv_file: # Choose which dataset to read from
    csv_reader = csv.reader(csv_file, delimiter=',')

    # The count verify that the entire file is being read

    for row in csv_reader:
        if(row[10].strip(" ") == believabilityColStr): 

            if(not (row[12] in myDict)): # If not in row and boolean you're checking for
                myDict[row[12]] = [1,[row[8][1:-6]]]

            else:
                myDict[row[12]][0] += 1
                myDict[row[12]][1].append(row[8][1:-6])

sortedDict = sorted(myDict.items(), key = lambda x: x[1], reverse=True)

oneBigList = []
# Write Frequency dictionary to separate .csv
# Choose the Output file based on inputs
with open(f'./data/{filePrefix}_Dataset{datasetNumber}.csv', mode='w' , newline='') as csv_file1: 
    fieldnames = ['URLs', 'Frequency','Dates']
    writer = csv.DictWriter(csv_file1, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in sortedDict:
        if y=="":
            print(x, y)

        if x == "":
            continue
        else:
            # Cleans the URLs of the https:// and the www.
            if(x[8:11] == "www"):
                writer.writerow({fieldnames[0]: x[12:26], fieldnames[1]: y[0], fieldnames[2]:y[1]})
            else:
                writer.writerow({fieldnames[0]: x[8:23], fieldnames[1]: y[0], fieldnames[2]:y[1]})
            oneBigList.extend(y[1])


from datetime import datetime
import pytz
import time
import json
central_tz = pytz.timezone("America/Chicago")

def epoch(dts):
    dateObj = datetime.strptime(dts, "%Y-%m-%dT%H:%M:%S")
    dateObjWithTZ = central_tz.localize(dateObj)
    return time.mktime(dateObjWithTZ.timetuple())



oneBigListEpoch = [int(epoch(dts)) for dts in oneBigList if dts != ""]

# print(oneBigList)
# assert epoch(oneBigList[0]) == "
# print(oneBigList[0], epoch(oneBigList[0]), oneBigListEpoch[0])
# print(oneBigListEpoch)

print(sorted(oneBigListEpoch))
with open(f"{filePrefix}dataset{datasetNumber}Epochs.json","w") as f:
    json.dump(oneBigListEpoch, f)