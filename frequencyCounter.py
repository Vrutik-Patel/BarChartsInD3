import csv

# Create frequency dictionary

myDict = {}
with open('./data/dataset_1_with_urls.csv') as csv_file: # Choose which dataset to read from
    csv_reader = csv.reader(csv_file, delimiter=',')

    # The count verify that the entire file is being read

    for row in csv_reader:
        if(row[10].strip(" ") == "True"):  # Change what value of row you're looking for (In this case True or False)

            if(not (row[12] in myDict)): # If not in row and boolean you're checking for
                myDict[row[12]] = [1,[row[8][1:-6]]]

            else:
                myDict[row[12]][0] += 1
                myDict[row[12]][1].append(row[8][1:-6])

sortedDict = sorted(myDict.items(), key = lambda x: x[1], reverse=True)

# Write Frequency dictionary to separate .csv
# Choose the Output file based on inputs
with open('./data/TRUE_Dataset1.csv', mode='w' , newline='') as csv_file1: 
    fieldnames = ['URLs', 'Frequency','Dates']
    writer = csv.DictWriter(csv_file1, fieldnames=fieldnames)

    writer.writeheader()
    for x,y in sortedDict:
        if x == "":
            continue
        else:
            # Cleans the URLs of the https:// and the www.
            if(x[8:11] == "www"):
                writer.writerow({fieldnames[0]: x[12:26], fieldnames[1]: y[0], fieldnames[2]:y[1]})
            else:
                writer.writerow({fieldnames[0]: x[8:23], fieldnames[1]: y[0], fieldnames[2]:y[1]})

